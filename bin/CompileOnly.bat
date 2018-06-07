
@echo off



set stripstr=%3
set stripstr=%stripstr:~1%
set stripstr=%stripstr:~0,-1%

path=%stripstr%;%path%


rem go to project folder


pushd %1
rem pause
call esc.bat %1 %2 


popd 
rem pause







