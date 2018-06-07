#ifndef __OBJECT_H__
#define __OBJECT_H__
#include <string>

using namespace std;



class $__object__$ {
 protected:
  
 public:
  virtual const char* __GetClassName__() {
    return "$__object__$";
  }
  
  virtual unsigned int __GetFieldNum__() {
    return 0;
  }
  
  virtual const char* __GetFieldName__(unsigned int i) {
    return NULL;
  }
  
  virtual const char* __GetFieldType__(unsigned int i) {
    return NULL;
  }

  virtual int __ReadField__ (string fieldname, void* ptr, int* len) { return 0; }
  virtual int __WriteField__(string fieldname, void* ptr, int len)  { return 0; }
};
#endif
