#include "ESharp.h"
#include "ESDllInterface.h"
#include "Engine.h"
#include "BGM.h"
#include "Math3D.Range.h"
#include "Math3D.BoundingBox2D.h"
#include "Math3D.Color.h"
#include "Math3D.Polygon.h"
#include "Math3D.Vector4.h"
#include "Math3D.Line.h"
#include "Math3D.Plane.h"
#include "Math3D.Frustum.h"
#include "Math3D.Collision.h"
#include "Math3D.Vector2.h"
#include "Math3D.Util.h"
#include "Math3D.BoundingBox.h"
#include "Math3D.Point.h"
#include "Math3D.Matrix4x4.h"
#include "Math3D.Quaternion.h"
#include "Math3D.Rect.h"
#include "Math3D.Matrix3.h"
#include "Math3D.Vector3.h"


int BGM::Update()
{
    if ((SoundComponent==nullptr))
    {
        SoundComponent = (Sound*)SoundContainer->FindComponentByType(L"Sound");
    }
    if ((SoundComponent!=nullptr))
    {
        if ((SoundLoad==false))
        {
            SoundComponent->PropSound->SetSoundFilePath(L"$project/Assets/wind.wav");
            SoundComponent->Play();
            Log(L"Sound Loaded", 0, 0.0f);
            SoundLoad = true;
        }
    }
    return 0;
}


BGM::BGM()
{
    SoundComponent = nullptr;
    SoundLoad = false;

}


const vector<string> BGM::mFieldNames = {"SoundContainer", "SoundComponent", "SoundLoad"};
const vector<string> BGM::mFieldTypes = {"Container", "Sound", "bool"};
const vector<string> BGM::mFieldAccessors = {"public", "private", "private"};


const char* BGM::__GetClassName__()
{
    return "BGM";
}


unsigned int BGM::__GetFieldNum__()
{
    return 3;
}


const char* BGM::__GetFieldName__(unsigned int i)
{
    if (i >= mFieldNames.size())	return nullptr;
    else							return mFieldNames[i].c_str();
}


const char* BGM::__GetFieldType__(unsigned int i)
{
    if (i >= mFieldTypes.size())	return nullptr;
    else							return mFieldTypes[i].c_str();
}


const char* BGM::__GetFieldAccessor__(unsigned int i)
{
    if (i >= mFieldAccessors.size())	return nullptr;
    else								return mFieldAccessors[i].c_str();
}


int BGM::__ReadField__(string fieldName, void* ptr, int* len)
{
    string arrayFieldName = "";
    int arrayIndex = 0;
    SeparateArrayFieldName(fieldName, arrayFieldName, arrayIndex);

    if (fieldName == "SoundContainer")
    {
        if (SoundContainer)
        {
            memcpy(ptr, (void*)&SoundContainer->id, sizeof(SoundContainer->id));
            *len = sizeof(SoundContainer->id);
            return 1;
        }
        else
        {
            return 0;
        }
    }

    if (fieldName == "SoundComponent")
    {
        memcpy(ptr, (void*)&SoundComponent, sizeof(SoundComponent));
        *len = sizeof(SoundComponent);
    }

    if (fieldName == "SoundLoad")
    {
        memcpy(ptr, (void*)&SoundLoad, sizeof(SoundLoad));
        *len = sizeof(SoundLoad);
    }

    return 0;
}


int BGM::__WriteField__(string fieldName, void* ptr, int len, int typeInfo)
{
    void* buf = nullptr;

    string arrayFieldName = "";
    int arrayIndex = 0;
    SeparateArrayFieldName(fieldName, arrayFieldName, arrayIndex);

    if (fieldName == "SoundContainer")
    {
        SoundContainer = new Container(0);
        SoundContainer->id = *((eng_obj_ptr*)ptr);
        return 0;
    }

    if (fieldName == "SoundComponent")
    {
        buf = &SoundComponent;
    }

    if (fieldName == "SoundLoad")
    {
        buf = &SoundLoad;
    }

    if (buf == nullptr)
    {
        return 1;
    }

    memcpy(buf, ptr, len);
    return 0;
}
