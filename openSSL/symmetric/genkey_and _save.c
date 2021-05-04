#include <stdio.h>
#include </usr/include/stdlib.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

//argument 1 : a valid openssl cipher filename
//argument 2 : the name of the file where to write the key 
//generate valid key for the cipher selected

int main(int argc, char **argv) {
	unsigned char key[EVP_MAX_KEY_LENGTH];//alocate the room in stack for accepting the key
	FILE *key_file;
	int key_size;
//checks
	if(argc < 3) {
			fprintf(stderr, "Usage: %s algorithm outfile\n",argv[0]);
			exit(-1);
	}


  if((key_file = fopen(argv[2],"w")) == NULL) {
          fprintf(stderr, "Problems with the output file\n");
          exit(-2);
  }


  const EVP_CIPHER *algo; //this is output
//aes128 --> program pass the 128 bits key file
//aes 256 --> pass the 256 bits key
//ask openssl for correct bit for a key 

  //const EVP_CIPHER *EVP_get_cipherbyname(const char *name); this is a string --> aes-128-cbc des3 
  if ((algo = EVP_get_cipherbyname(argv[1])) == NULL){ //argv1 contain the name 
    fprintf(stderr, "Unknown algorithm\n");
    exit(-3);
}
//ask openssl the key size
  key_size=EVP_CIPHER_key_length(algo); //pass the EVP_cipher pointer
//init the random generator properly
	int rc = RAND_load_file("/dev/random", 32);
	if(rc != 32) {
		fprintf(stderr, "Couldnt initialize the PRNG\n");
    exit(-4);
	}


//allocate the key variable and ask the generate key size bytes
//genrate the correct number of bytes
  RAND_bytes(key,key_size);


//take key key_size byte and save the output in the key_file
  if(fwrite(key , 1 , key_size , key_file) != key_size){
    fprintf(stderr, "Error writing on file\n");
    exit(-5);
  }

	return 0;
}
//gcc -o gen.exe genkey.c -lcrypto 
//./gen.exe aes-256-cbc .key
//hexdump .key