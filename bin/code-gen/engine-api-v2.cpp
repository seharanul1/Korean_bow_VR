///Component

// following interface needs 
// predefined E# Library classes
//    Math3D inc. Vectors, Matrix
//    Path 
//    Texture  ( or Path )
//    BoundingBox
//    several Enums 
//        DrawSort
//        CullType
//        AlphaBlending 
//        BackgroundType
//        SamplerMagFilter
//        SamplerMinFilter
//        FogType
//        VRDIDeviceStatus
// 
// 
// 
// 

public class ComponentBase
{
	public long UID;
	public class PropertyInstance
	{
		string Name;
		bool Locked;
		bool Expanded;
		bool Selected;
	};

	public PropertyInstance PropInstance;

	public bool LoadFromFile(string fname);
	public bool SaveToFile(string fname);

};



public class ComponentNode : ComponentBase
{
	public int GetChildrenCount();
	public ComponentNode GetChild(int idx);
	public ComponentNode DetachChild(int idx);
	public void DeleteChild(int idx);
	public void RemoveAllChildren();
	public void Insert(ComponentNode a);
};


public class PropertyGroup : ComponentBase
{
	public bool SetProperty(string key, ref string value);
	public bool SetProperty(string key, string value);
};


public class TransformGroup : ComponentNode
{
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
	public BoundingBox GetWorldBox(); //
	public BoundingBox GetSumBox();
	
};




public class Camera : TransformGroup
{
	public class PropertyCamera
	{
		public float NearViewPlane;
		public float FarViewPlane;
		public float FarViewPlaneSky;
		public float FocalLength;  // mm focus distance 35mm // film camera 환산
		public float ZoomTangent;  // maps to GetZoomTangent()

		public float AspectRatio;  // 가로 세로 비율
		public float DepthOfField;

		public float FocusingDistance;
		public float OrthographicViewSize;


		public Vector2 Offset;

		public bool EnableCulling;

		public bool Lighting;
		public int LightCount;

		public Color BackColor;
		public BackgroundType BackgroundType; // enum 
		public bool DrawGrid;
		public Texture BackgroundTextureFile;

	};


	public PropertyCamera PropCamera;

	public bool GetPickRay(int x, int y, int w, int h, float length, Vector3* pickRayOrig, Vector3* pickRayDir);
	public void ViewPerspective(Vector3 target, float distance);
	public void ViewUser(Vector3 target, float distance);
	public void Pan(float x, float y);
	public Matrix GetProjectionMatrix();
	public Matrix GetViewMatrix();
	public Matrix GetViewProjectionMatrix();
	public float GetZoomTangent();
	public bool IsOrthographic();
	public Matrix GetProjectionMatrix();
	public Matrix GetViewMatrix();
	public Matrix GetViewProjectionMatrix();
	public Plane GetClipPlane();
};




public class Light : TransformGroup
{
	public bool IsEffective(TransformGroup obj);
};




public class FrameTimer 
{
	public double GetSystemTime();
	public double GetSystemFrameElapseTime();

	public void Advance(); // just need to be called only from Root Timer
	public void Step(double stepValue);

	public double GetFPS();

	public double GetTime();
	public void Reset(); // reset timer to start (zero)
	public void SetSpeed(double speed); // 1.0 normal time 

	public void Start();
	public void Stop();

	public double GetFrameElapseTime();
};






public class World : TransformGroup
{

	public class PropertyFog
	{
		public FogType FogMode;

		public float FogNearPlane;
		public float FogFarPlane;
		public float FogDensity;
		public Color FogColor;
	};

	public PropertyFog PropFog;
	public FrameTimer WorldTime;

	public Camera DefaultCamera; // maps to GetDefaultCamera()
	public Light DefaultLight;

	public void UpdateDynamicLight();
};



public class DeviceScreen : ComponentBase
{
	public int GetLogicalWidth();
	public int GetLogicalHeight();
	public int GetDeviceWidth();
	public int GetDeviceHeight();
	public Vector2 GetLogicalCoord(Vector2 screenp);
	public Vector2 GetDeviceCoord(Vector2 logicalp);
	public void SetWidthHeight(int width, int height);
	public void SetViewOrientation(int v);
	public int GetViewOrientation();
	public void ConvertOrientation(Vector2 point);
	public bool XYSwitched();
	public bool MirroredOrientation();
	public Matrix GetMatrixOrientation();
	public Matrix GetMatrixOrientationInverse();
	public Vector2 GetLogicalSize(Vector2 v);
	public Vector2 GetDeviceSize(Vector2 v);
	public Vector2 GetViewportCoord(Vector2 pos);

};




/// MaterialFile 
public class ResourceMaterial 
{
	public class PropertyMaterial
	{
		public string VertexShader;
		public string PixelShader;
		public Color FlatColor;
		public Color AmbientColor;
		public float AmbientColorRate;
		public float AnimationStartTime;
		public int AnimationLoop;
		public int AnimationSpeed; // frame per second
		public float Opacity;  // W90
		public AlphaBlending AlphaBlending;  //  EnumAlphaBlending  // enum 
		public float Glossiness;
		public CullMode CullBackFace;       // 0 : NULL  1 : D3DCULL_CW  2: D3DCULL_CCW    
		public float AlphaTest;
		public float Diffuse;
		public float Ambient;
		public float Specular;
		public Color EdgeColor;
		public float EdgeThickness;
		public SamplerMagFilter MagFilter;   // SamplerMagFilter
		public SamplerMinFilter MinFilter;   // SamplerMagFilter
		public float ShadowDarkness;
		public bool WireFrame;
		public Texture TextureFileDiffuse;
		public Texture TextureFileEnv;
		public Texture TextureFileNormal;
		public Texture TextureFileSpecular;
		public Texture TextureFileGlossiness;
		public Texture TextureFileEtc1;
		public Texture TextureFileEtc2;
		public Texture TextureFileEtc3;
		public Texture TextureFileEtc4;
		public Vector4 NormalMapDirection;
	};

	public PropertyMaterial PropMaterial;


};
  


// fbx manipulation

public class ResourceFbx 
{
	public ResourceFbxAnimation GetResourceFbxAnimation(string animationName);
	public bool AddResourceFbxAnimation(string animationName, ResourceFbxAnimation anim);

	public ResourceFbxMesh GetResourceFbxMesh(int meshIndex );

	public ResourceMaterial GetResourceFbxMaterial(int materialIndex);
	public bool SetResourceFbxMaterial(int materialIndex, ResourceMaterial mat); 

};



///Fbx

public class ResourceFbxMesh
{
	// access to vertex
	public Path MeshFile; // get set access of mesh file
};




public class ResourceFbxAnimation
{
	// access to keyframe info
	public Path AnimationFile; // get set access of ani file
};




public class FbxNode : TransformGroup
{
	public ResourceFbx GetResourceFbx();

	public int GetChildCount();
	public FbxNode GetChild(int idx);

	public class PropertyFbxFile
	{
		public Path FbxFile;
	};
	public PropertyFbxFile PropFbxFile;

	public int FbxNodeID;

	public ResourceFbx GetResourceFbx();
};





public class FbxNodeMesh : FbxNode
{

	public ResourceFbxMesh GetResourceFbxMesh();

};



public class FbxNodeBone : FbxNode
{
// no bone function currently
};





public class Fbx : TransformGroup
{
	public class PropertyFbxFile 
	{
		public Path FbxFile;
	};
	public PropertyFbxFile PropFbxFile;

	public class PropertyFbxAnimation
	{
		public string ActiveAnimation;
		public float AnimationSpeed;
	};
	public PropertyFbxAnimation PropFbxAnimation;

	public void ClearActiveAnimation();
	public bool SetActiveAnimation(string animationName);
	public bool SetActiveAnimation(int idx);
	public void Play();
	public void Pause();
	public void Stop();

	// node enumaration
	public int GetNodeCount(); // 
	public FbxNode GetNode(long nodeid); // 

	public ResourceFbx GetResourceFbx();
	public ResourceFbxNode GetResourceFbxNode();
	public ResourceFbxAnimation GetResourceFbxAnimation(string animationName);

	public int GetChildCount();
	public FbxNode GetChild(int idx);
	public FbxNode GetChild(string nodename);

};





// device 


public class VRMessage
{
	public void SetParameterValueCount( string  name, VRMessageParameterType type);

	public void SetParameter(string  name, string value);
	public void SetParameters(string  name, string *values, int count);

	public int GetParameterValueCount(string  name);
	public bool GetParameter(string  name, string *value, int idx = 0);
	public bool GetParameters(string  name, string *value, int count );

};





public class VRDIClient
{
	public VRDIDeviceStatus GetDeviceStaus(string  deviceUUID);
	public VRDIDeviceStatus OpenStatus;

	public bool Open(string deviceUUID);
	public bool Close();
	public bool IsOpened();

	public bool SendMessage(VRMessage sendmsg);
	public bool SendRecvMessage(VRMessage send, ref VRMessage recv);
	public bool PeekMessage(ref VRMessage recv);

	public bool PollMessage( );
	public bool GetLastError( ref string errmsg );

};

