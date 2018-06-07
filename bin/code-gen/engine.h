#ifndef __ENGINE_H__
#define __ENGINE_H__
#include "object.h"


typedef unsigned long long eng_obj_ptr;


#if 0
public class PropertyTransform
{
  bool Show;
  Vector3 Position;
  Quaternion Rotation;
  Vector3 Scale;
  DrawSort SortType;  // enum 
  int FixedOrder;
  CullType CullType;  // enum 
};
#endif

struct Vector3 {
  float x;
  float y;
  float z;
};


struct Quaternion {
  float x;
  float y;
  float z;
  float w;
};


struct BoundingBox {
  Vector3 Vertex[2];
};




//class TransformGroup  : ComponentNode
class TransformGroup : public $__object__$ {
public:
  virtual const char* __GetClassName__() {
    return "TransformGroup";
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
  
  virtual int __ReadField__(string fieldname, void* ptr, int* len) {
    return 0;
  }
  
  virtual int __WriteField__(string fieldname, void* ptr, int len) {
    return 0;
  }
  
  
 private:
  eng_obj_ptr uid;
  
 public:
  TransformGroup* Find(char* objectNamePath);
  void SetLocalRotation(Quaternion q);
  void LookAtLocalDirection(Vector3 direction);
  void LookAtPosition(Vector3 position);
  void LookAt(Vector3 position, Vector3 target, Vector3 up);
  void ShiftPosition(Vector3 shift);
  void ViewTop(Vector3 target, float distance);
  void ViewBottom(Vector3 target, float distance);
  

  void ViewLeft(Vector3 target, float distance);
  void ViewRight(Vector3 target, float distance);
  void ViewFront(Vector3 target, float distance);
  void ViewRear(Vector3 target, float distance);
  void MoveForward(float dist);
  void Rotate(float x, float y, Vector3 center);
  void SetScale(Vector3 scale);
  void SetPosition(Vector3 pos);
  void SetLocalPosition(Vector3 pos);

  Quaternion GetLocalRotation();

  Vector3 GetScale();
  Vector3 GetLocalPosition();
  Vector3 GetLocalScale();
  Vector3 GetPosition();
  Vector3 GetDirection();
  Vector3 GetUp();
  Vector3 GetTarget();
  Vector3 WorldToLocalPosition(Vector3 world);
  Vector3 WorldToLocalDirection(Vector3 world);
  Vector3 LocalToWorldPosition(Vector3 local);
  Vector3 LocalToWorldDirection(Vector3 local);

  int IsVisible();
  int IsTransparent();
  int IsCullable();
  int FindNearCollision(Vector3 posfrom, Vector3 posto, Vector3* intersectnew, float* dist);
  TransformGroup* FindNearestCollision(Vector3 from, Vector3 to, Vector3* intersect,  float* distr);

  TransformGroup* Find(const char* objectNamePath );

  void* GetWorld();

  BoundingBox GetLocalBox();
  BoundingBox GetWorldBox(); //
  BoundingBox GetSumBox();
};



extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetPosition)(eng_obj_ptr);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_SetLocalRotation)(eng_obj_ptr,Quaternion);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAtLocalDirection)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAtPosition)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAt)(eng_obj_ptr,Vector3,Vector3,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ShiftPosition)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewTop)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewBottom)(eng_obj_ptr,Vector3,float);

extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewBottom)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewLeft)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewRight)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewFront)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewRear)(eng_obj_ptr,Vector3,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_MoveForward)(eng_obj_ptr,float);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_Rotate)(eng_obj_ptr,float,float,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_SetScale)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT void (*ENG_CAPI_TransformGroup_SetPosition)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT Quaternion (*ENG_CAPI_TransformGroup_GetLocalRotation)(eng_obj_ptr);
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetScale)(eng_obj_ptr) ;
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetLocalPosition)(eng_obj_ptr);
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetLocalScale)(eng_obj_ptr);
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetUp)(eng_obj_ptr);
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetTarget)(eng_obj_ptr) ;
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_WorldToLocalPosition)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_WorldToLocalDirection)(eng_obj_ptr,Vector3) ;
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_LocalToWorldPosition)(eng_obj_ptr,Vector3) ;
extern "C" DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_LocalToWorldDirection)(eng_obj_ptr,Vector3);
extern "C" DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsVisible)(eng_obj_ptr);
extern "C" DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsTransparent)(eng_obj_ptr);
extern "C" DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsCullable)(eng_obj_ptr) ;

extern "C" DLLEXPORT int     (*ENG_CAPI_TransformGroup_FindNearCollision)(eng_obj_ptr, Vector3, Vector3, Vector3*, float*);
extern "C" DLLEXPORT eng_obj_ptr (*ENG_CAPI_TransformGroup_Find)(eng_obj_ptr, const char*);
extern "C" DLLEXPORT eng_obj_ptr (*ENG_CAPI_TransformGroup_FindNearestCollision)(eng_obj_ptr, Vector3, Vector3, Vector3*, float*);

extern "C" DLLEXPORT void*       (*ENG_CAPI_TransformGroup_GetWorld)(eng_obj_ptr);
extern "C" DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetLocalBox)(eng_obj_ptr);
extern "C" DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetWorldBox)(eng_obj_ptr);
extern "C" DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetSumBox)(eng_obj_ptr);

#endif

