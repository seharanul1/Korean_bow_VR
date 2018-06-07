
all: out  test.dll

out: server.o test.dll
	g++ -o server.exe server.o -L ./ -ltest

server.o: server.cpp
	g++ -c -g server.cpp

test.o : test.cpp test.h engine.h object.h 
	g++ -c -g -DBUILD_DLL test.cpp 

engine.o : engine.cpp engine.h test.h object.h
	g++ -c -g -DBUILD_DLL engine.cpp

test.dll: test.o engine.o
	g++ -shared -o test.dll test.o engine.o -Wl,--output-def,test.def,--out-implib,libtest.a


clean:
	$(RM) server.o test.o




	
