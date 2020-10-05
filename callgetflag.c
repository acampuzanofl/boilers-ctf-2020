#include <stdio.h>
#include <dlfcn.h>


int main(){

	void *handle;
	void (*getflag)(int);

	handle = dlopen("./libflag.so", RTLD_LAZY);
	if (!handle){
		printf("error getting handle %s", dlerror());
		return 0;
	}

	getflag = dlsym(handle, "getflag");
	if (!getflag){
		printf("error getting symbol getflag %s", dlerror());
		return 0;
	}

	printf("this program works\n\n");	
	(*getflag)(0x1a0a);

	return 1;
		
}
