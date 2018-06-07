#ifndef __TEST_H__
#define __TEST_H__


#ifdef BUILD_DLL
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT __declspec(dllimport)
#endif


//#ifndef __FuncScriptTransform__
//#define __FuncScriptTransform__
//typedef int (*FuncScriptTransformSetPropertyVector3)(int obj, const char *propName, float x, float y, float z);
//typedef int (*FuncScriptTransformGetPropertyVector3)(int obj, const char *propName, float *x, float *y, float *z);
//#endif

extern "C" DLLEXPORT int (*PTransformSetPropertyVector3)(int obj, const char *propName, float x, float y, float z);
extern "C" DLLEXPORT int (*PTransformGetPropertyVector3)(int obj, const char *propName, float *x, float *y, float *z);


extern "C" DLLEXPORT int   hello(char*);
extern "C" DLLEXPORT int   Fl2Es_VRLangBegin();
extern "C" DLLEXPORT int   Fl2Es_VRLangEnd();
extern "C" DLLEXPORT int   Fl2Es_ExportFunction(void* fun_ptr, char* fun_name, char* fun_type);
extern "C" DLLEXPORT void* Fl2Es_ActorCreate(char* classname, unsigned long UID);
extern "C" DLLEXPORT void  Fl2Es_ActorDelete(void* es_obj);

extern "C" DLLEXPORT int   Fl2Es_ActorMethodUpdate(void* es_obj);
extern "C" DLLEXPORT int   Fl2Es_ActorFieldRead (void* es_obj, char* fieldname, void* val, int* len);
extern "C" DLLEXPORT int   Fl2Es_ActorFieldWrite(void* es_obj, char* fieldname, void* val, int  len);

extern "C" DLLEXPORT const char* Fl2Es_GetClassName(void* ptr);
extern "C" DLLEXPORT unsigned int Fl2Es_GetFieldNum(void* ptr);
extern "C" DLLEXPORT const char* Fl2Es_GetFieldName(void* ptr, unsigned int i);
extern "C" DLLEXPORT const char* Fl2Es_GetFieldType(void* ptr, unsigned int i);

#endif
