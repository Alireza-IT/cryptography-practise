//this program generates a sequence of random bytes
// whose length is passed as a first argument
//gcc -o random.exe random.c -lcrypto to link the library while compiling
//./random.exe 24 

#include <stdio.h>
#include <openssl/rand.h> // .h is important 

#define MAX_BUF 2048

int main(int argc,char **argv) {

  int n;
  int i;
  unsigned char random_string[MAX_BUF];
// add check 
  if(argc < 2){
    fprintf(stderr,"Missing parameter, usage %s nbytes\n",argv[0]);
    exit(1);
  }

  if(sscanf(argv[1],"%d",&n)==0){
    fprintf(stderr,"Problems scanning argv[1]\n");
    exit(1);
  }

  if(n>MAX_BUF){
    printf("Maximum size allowed exceeded. Set to %d\n",MAX_BUF);
    n=MAX_BUF;
  }

//init the random generator
//to perform the initialization just only copy and paste 
//32 is number of bytes from the location of /dev/random and cosider as seed ..32 is best practice
//high entropy means high randomness
 //length of key is same as length of the 32
  int rc = RAND_load_file("/dev/random", 32);
  if(rc != 32) {
    printf("Couldnt initialize PRNG\n");
    exit(1);
  }
//function that is needed to genrated random bytes string
//first parameters is where to save the ramdom bytes
//second is number of bytes
  RAND_bytes(random_string,n); //n is integer conversion of argv[1]

//print

  printf("Sequence generated: ");
  for(i = 0; i < n; i++)
    printf("%02x", random_string[i]);
  printf("\n");

  return 0;
}