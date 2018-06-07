#include "ESharp.h"
#include "ESDllInterface.h"
#include "Engine.h"
#include "Assets\BGM.h"


const char* Fl2Es_GetCompilerVersion()
{
    return "20170719-001";
}


int Fl2Es_VRLangBegin()
{
    return 1;
}


void* Fl2Es_ActorCreate(char* classname, unsigned long UID)
{
    string classNameInString = classname;

    if (classNameInString == "BGM")
    {
        BGM* actor = new BGM;
        return actor;
    }

    cout << "unknown class" << endl;
    return nullptr;
}
