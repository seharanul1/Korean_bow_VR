#include <cstdio>
#include <memory>

#include "test.h"


int main() {
  hello((char*) "Hello World");

  Fl2Es_VRLangBegin();


#if  0
  if (PTransformGetPropertyVector3 != NULL) {
    printf("Value = OK\n");
  }

  Fl2Es_ExportFunction(NULL, (char*) "GetProperty", (char*) "");
#endif

  void* obj = Fl2Es_ActorCreate((char*) "MoveActor", 0L);

  printf("class-name::%s\n", Fl2Es_GetClassName(obj));

  unsigned int n = Fl2Es_GetFieldNum(obj);
  printf("class-field-num::%u\n", n);
#if 1
  for (int i=0; i<n; i++) {
    const char* field_name = Fl2Es_GetFieldName(obj, i);
    const char* field_type = Fl2Es_GetFieldType(obj, i);
    printf("field-name::%s::%s\n", field_name, field_type);
  }
#endif
  printf("end--of--field-name::\n");

  
  for (int i=0; i<100; i++) {
    int len;
    int j;
    Fl2Es_ActorFieldWrite(obj, (char*) "man", (void*) &i, sizeof(i));
    Fl2Es_ActorFieldRead(obj,  (char*) "man", (void*) &j, &len);

    //Fl2Es_ActorMethodUpdate(NULL);
  
    

    printf("man::value::%d\n", j);
  }

  

  Fl2Es_ActorDelete(obj);

  Fl2Es_VRLangEnd();
  return 0;
}
