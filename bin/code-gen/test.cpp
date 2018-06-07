#include <iostream>
#include <cstdio>
#include <memory>

#include <stddef.h>
#include <string>
#include <vector>
#include <map>
#include <list>

using namespace std;

//#include "engine.h"
#include "test.h"

//DLLEXPORT FuncScriptTransformSetPropertyVector3 PTransformSetPropertyVector3 = NULL;
//DLLEXPORT FuncScriptTransformGetPropertyVector3 PTransformGetPropertyVector3 = NULL;

DLLEXPORT int (*PTransformSetPropertyVector3)(int obj, const char *propName, float x, float y, float z) = NULL;
DLLEXPORT int (*PTransformGetPropertyVector3)(int obj, const char *propName, float *x, float *y, float *z) = NULL;



#include "object.h"
#include "engine.h"


class EActor : public $__object__$ {
public:
  virtual int Update() {
    return 0;
  }
};


class MoveActor  : public EActor {
protected:  
int man;
TransformGroup* T;
Vector3 Pos;

public:
  int Update() {
    float x;
    float y;
    float z;
    Vector3 Pos;

    
    Pos = T->GetPosition();
    Pos.x = Pos.x + 0.01;
    T->SetPosition(Pos);

#if 0
    if (PTransformGetPropertyVector3 == NULL)
      return 3;
    
    if (PTransformSetPropertyVector3 == NULL)
      return 4;
    
    PTransformGetPropertyVector3(man, "Position", &x, &y, &z);
    x += 0.01;
    PTransformSetPropertyVector3(man, "Position", x, y, z);
#endif    
    return 1;
  }

  //======================================================//
public:
  virtual const char* __GetClassName__() {
    return "MoveActor";
  }
  
  virtual unsigned int __GetFieldNum__() {
    return 3;
  }

virtual const char* __GetFieldName__(unsigned int i) {
  static const char* tbl[3] = { "man", "T", "Pos"};
  return (0 <= i  && i < 3) ? tbl[i] : NULL;
}
  
virtual const char* __GetFieldType__(unsigned int i) {
  static const char* tbl[] = {"int", "TransformGroup", "Vector3"};
  return (0 <= i  && i < 3) ? tbl[i] : NULL;
}
  
  virtual int __ReadField__(string fieldname, void* ptr, int* len) {
    if (fieldname == "man") {
      memcpy(ptr, (void*)&man, sizeof(man));
      *len = sizeof(man);
      return 1;
    }
    
    if (fieldname == "T") {
      memcpy(ptr, (void*)&T, sizeof(T));
      *len = sizeof(T);
      return 1;
    }
    
    if (fieldname == "Pos") {
      memcpy(ptr, (void*)&Pos, sizeof(T));
      *len = sizeof(T);
      return 1;
    }
    
    return 0;
  }


  virtual int __WriteField__(string fieldname, void* ptr, int len) {
    if (fieldname == "man") {
      memcpy((void*) &man, ptr, len);
      return 1;
    }
    
    if (fieldname == "T") {
      memcpy((void*) &T, ptr, len);
      return 1;
    }
    
    if (fieldname == "Pos") {
      memcpy((void*) &Pos, ptr, len);
      return 1;
    }
    
    return 0;
  }
};


extern "C" DLLEXPORT int hello(char* name)
{
  printf("%s\n", name);
}


extern "C" DLLEXPORT void*  Fl2Es_ActorCreate(char* classname, unsigned long UID)
{
  string cls = classname;
  if (cls == (string) "MoveActor") {
    return new MoveActor;
  }
  
  cout << "unknown class" << endl;
  return NULL;
}

extern "C" DLLEXPORT void Fl2Es_ActorDelete(void* actor) {
  EActor* eactor = (EActor*) actor;
  delete (eactor);
}

extern "C" DLLEXPORT int Fl2Es_ActorFieldRead (void* actor, char* fieldname, void* val, int* len) {
  EActor* eactor = (EActor*) actor;
  return (eactor != NULL) ? eactor->__ReadField__(fieldname, val, len) : 0;
}

extern "C" DLLEXPORT int Fl2Es_ActorFieldWrite(void* actor, char* fieldname, void*  val, int  len) {
  EActor* eactor = (EActor*) actor;
return (eactor != NULL) ? eactor->__WriteField__(fieldname, val, len) : 0;
}

extern "C" DLLEXPORT int Fl2Es_ActorMethodUpdate(void* actor) {
  EActor* eactor = (EActor*) actor;
  return (eactor != NULL) ? eactor->Update() : 0;
}

extern "C" DLLEXPORT int Fl2Es_VRLangBegin() {
  return 1;
}

extern "C" DLLEXPORT int Fl2Es_VRLangEnd() {
  return 1;
}

extern "C" DLLEXPORT int  Fl2Es_ExportFunction(void* fun_ptr, char* fun_name, char* fun_type) {
  puts("export-functions");
  return 0;
}

extern "C" DLLEXPORT const char* Fl2Es_GetClassName(void* ptr) {
  EActor* obj = (EActor*) ptr;
  return (obj != NULL) ? obj->__GetClassName__() : "";
}

extern "C" DLLEXPORT unsigned int Fl2Es_GetFieldNum(void* ptr) {
  EActor* obj = (EActor*) ptr;
  return (obj != NULL) ? obj->__GetFieldNum__() : 0;
}

extern "C" DLLEXPORT const char* Fl2Es_GetFieldName(void* ptr, unsigned int i) {
  EActor* obj = (EActor*) ptr;
return (obj != NULL) ? obj->__GetFieldName__(i) : "";
}

extern "C" DLLEXPORT const char* Fl2Es_GetFieldType(void* ptr, unsigned int i) {
  EActor* obj = (EActor*) ptr;
return (obj != NULL) ? obj->__GetFieldType__(i) : "";
}
