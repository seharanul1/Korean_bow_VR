#include "test.h"
#include "object.h"
#include "engine.h"



DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetPosition)(eng_obj_ptr) = NULL;
DLLEXPORT void   (*ENG_CAPI_TransformGroup_SetLocalRotation)(eng_obj_ptr,Quaternion) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAtLocalDirection)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAtPosition)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_LookAt)(eng_obj_ptr,Vector3,Vector3,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ShiftPosition)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewTop)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewBottom)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewLeft)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewRight)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewFront)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_ViewRear)(eng_obj_ptr,Vector3,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_MoveForward)(eng_obj_ptr,float) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_Rotate)(eng_obj_ptr,float,float,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_SetScale)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT void (*ENG_CAPI_TransformGroup_SetPosition)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT Quaternion (*ENG_CAPI_TransformGroup_GetLocalRotation)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetScale)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetLocalPosition)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetLocalScale)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetUp)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_GetTarget)(eng_obj_ptr) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_WorldToLocalPosition)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_WorldToLocalDirection)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_LocalToWorldPosition)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT Vector3 (*ENG_CAPI_TransformGroup_LocalToWorldDirection)(eng_obj_ptr,Vector3) = NULL;
DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsVisible)(eng_obj_ptr) = NULL;
DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsTransparent)(eng_obj_ptr) = NULL;
DLLEXPORT int     (*ENG_CAPI_TransformGroup_IsCullable)(eng_obj_ptr) = NULL;
DLLEXPORT int     (*ENG_CAPI_TransformGroup_FindNearCollision)(eng_obj_ptr, Vector3, Vector3, Vector3*, float*) = NULL;
DLLEXPORT eng_obj_ptr (*ENG_CAPI_TransformGroup_Find)(eng_obj_ptr, const char*) = NULL;
DLLEXPORT eng_obj_ptr (*ENG_CAPI_TransformGroup_FindNearestCollision)(eng_obj_ptr, Vector3, Vector3, Vector3*, float*) = NULL;

DLLEXPORT void* (*ENG_CAPI_TransformGroup_GetWorld)(eng_obj_ptr) = NULL;
DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetLocalBox)(eng_obj_ptr) = NULL;
DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetWorldBox)(eng_obj_ptr) = NULL;
DLLEXPORT BoundingBox (*ENG_CAPI_TransformGroup_GetSumBox)(eng_obj_ptr) = NULL;

Vector3
TransformGroup::GetPosition() {
  return ENG_CAPI_TransformGroup_GetPosition(uid);
}


TransformGroup*
TransformGroup::Find(const char* objectNamePath) {
  TransformGroup* obj = new TransformGroup;
  if (obj == NULL)
    return NULL;
  else {
    obj->uid = ENG_CAPI_TransformGroup_Find(uid, objectNamePath);
    return obj;
  }
}


void
TransformGroup::SetLocalRotation(Quaternion q) {
  ENG_CAPI_TransformGroup_SetLocalRotation(uid, q);
}

void
TransformGroup::LookAtLocalDirection(Vector3 direction) {
  ENG_CAPI_TransformGroup_LookAtLocalDirection(uid, direction);
}

void
TransformGroup::LookAtPosition(Vector3 position) {
  ENG_CAPI_TransformGroup_LookAtPosition(uid, position);
}

void
TransformGroup::LookAt(Vector3 position, Vector3 target, Vector3 up) {
  ENG_CAPI_TransformGroup_LookAt(uid, position, target, up);
}


void
TransformGroup::ShiftPosition(Vector3 shift) {
  ENG_CAPI_TransformGroup_ShiftPosition(uid, shift);
}


void
TransformGroup::ViewTop(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewTop(uid, target, distance);
}


void
TransformGroup::ViewBottom(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewBottom(uid, target, distance);
}


void
TransformGroup::ViewLeft(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewLeft(uid, target, distance);
}


void
TransformGroup::ViewRight(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewRight(uid, target, distance);
}

void
TransformGroup::ViewFront(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewFront(uid, target, distance);
}

void
TransformGroup::ViewRear(Vector3 target, float distance) {
  ENG_CAPI_TransformGroup_ViewRear(uid, target, distance);
}

void
TransformGroup::MoveForward(float dist) {
  ENG_CAPI_TransformGroup_MoveForward(uid, dist);
}


void
TransformGroup::Rotate(float x, float y, Vector3 center) {
  ENG_CAPI_TransformGroup_Rotate(uid, x, y, center);
}

void
TransformGroup::SetScale(Vector3 scale) {
  ENG_CAPI_TransformGroup_SetScale(uid, scale);
}

void
TransformGroup::SetPosition(Vector3 pos) {
  ENG_CAPI_TransformGroup_SetScale(uid, pos);
}


Quaternion
TransformGroup::GetLocalRotation() {
  return ENG_CAPI_TransformGroup_GetLocalRotation(uid);
}

Vector3
TransformGroup::GetScale() {
  return ENG_CAPI_TransformGroup_GetScale(uid);
}

Vector3
TransformGroup::GetLocalPosition() {
  return ENG_CAPI_TransformGroup_GetLocalPosition(uid);
}

Vector3
TransformGroup::GetLocalScale() {
  return ENG_CAPI_TransformGroup_GetLocalScale(uid);
}


Vector3
TransformGroup::GetUp() {
  return ENG_CAPI_TransformGroup_GetUp(uid);
}


Vector3
TransformGroup::GetTarget() {
  return ENG_CAPI_TransformGroup_GetTarget(uid);
}

Vector3
TransformGroup::WorldToLocalPosition(Vector3 world) {
  return ENG_CAPI_TransformGroup_WorldToLocalPosition(uid, world);
}


Vector3
TransformGroup::WorldToLocalDirection(Vector3 world) {
  return ENG_CAPI_TransformGroup_WorldToLocalDirection(uid, world);
}


Vector3
TransformGroup::LocalToWorldPosition(Vector3 local) {
  return ENG_CAPI_TransformGroup_LocalToWorldPosition(uid, local);
}


Vector3
TransformGroup::LocalToWorldDirection(Vector3 local) {
  return ENG_CAPI_TransformGroup_LocalToWorldDirection(uid, local);
}

int
TransformGroup::IsVisible() {
  return ENG_CAPI_TransformGroup_IsVisible(uid);
}


int
TransformGroup::IsTransparent(){
  return ENG_CAPI_TransformGroup_IsTransparent(uid);
}

int
TransformGroup::IsCullable() {
  return ENG_CAPI_TransformGroup_IsCullable(uid);
}


int
TransformGroup::FindNearCollision(Vector3 posfrom, Vector3 posto, Vector3* intersectnew, float* dist) {
  return ENG_CAPI_TransformGroup_FindNearCollision(uid,posfrom,posto,intersectnew,dist);
}


TransformGroup*
TransformGroup::FindNearestCollision(Vector3 from, Vector3 to, Vector3* intersect, float* distr) {
  TransformGroup* obj = new TransformGroup;
  if (obj == NULL)
    return NULL;
  else {
    obj->uid = ENG_CAPI_TransformGroup_FindNearestCollision(uid, from, to, intersect, distr);
    return obj;
  }
}


void* //World*
TransformGroup::GetWorld() {
  return ENG_CAPI_TransformGroup_GetWorld(uid);
}


BoundingBox
TransformGroup::GetLocalBox() {
  return ENG_CAPI_TransformGroup_GetLocalBox(uid);
}

BoundingBox
TransformGroup::GetWorldBox() {
  return ENG_CAPI_TransformGroup_GetWorldBox(uid);
}

BoundingBox
TransformGroup::GetSumBox() {
  return ENG_CAPI_TransformGroup_GetSumBox(uid);
}




#if 0
class TransformGroup {
  class PropertyTransform  {
    bool Show;
    Vector3 Position;
    Quaternion Rotation;
    Vector3 Scale;
    //DrawSort SortType;  // enum 
    int SortType;  // enum 
    int FixedOrder;
    //CullType CullType;  // enum 
    int CullType;  // enum 
  };
   
   public PropertyTransform PropTransform;
					 
					 
  public void SetLocalRotation(Quaternion q);
  public void LookAtLocalDirection(Vector3 direction);
  public void LookAtPosition(Vector3 position);
  public void LookAt(Vector3 position, Vector3 target, Vector3 up);
  public void ShiftPosition(Vector3 shift);
  public void ViewTop(Vector3 target, float distance);
  public void ViewBottom(Vector3 target, float distance);
  public void ViewLeft(Vector3 target, float distance);
  public void ViewRight(Vector3 target, float distance);
  public void ViewFront(Vector3 target, float distance);
  public void ViewRear(Vector3 target, float distance);
  public void MoveForward(float dist);
  public void Rotate(float x, float y, Vector3 center);
  public void SetScale(Vector3 scale);
  public void SetPosition(Vector3 pos);
  public void SetLocalPosition(Vector3 pos);

  public Quaternion GetLocalRotation();

  public Vector3 GetScale();
  public Vector3 GetLocalPosition();
  public Vector3 GetLocalScale();
  public Vector3 GetPosition();
  public Vector3 GetDirection();
  public Vector3 GetUp();
  public Vector3 GetTarget();
  public Vector3 WorldToLocalPosition(Vector3 world);
  public Vector3 WorldToLocalDirection(Vector3 world);
  public Vector3 LocalToWorldPosition(Vector3 local);
  public Vector3 LocalToWorldDirection(Vector3 local);

  public bool IsVisible();
  public bool IsTransparent();
  public bool IsCullable();
  public bool FindNearCollision(Vector3 posfrom, Vector3 posto, ref Vector3 intersectnew, ref float dist);
  public TransformGroup FindNearestCollision(Vector3 from, Vector3 to, ref Vector3 intersect, ref float distr);

  public TransformGroup Find(string objectNamePath );

  public World GetWorld();

  public BoundingBox GetLocalBox();
  public BoundingBox GetWorldBox(); 
  public BoundingBox GetSumBox();
};
#endif	

