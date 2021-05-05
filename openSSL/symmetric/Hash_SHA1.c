#include <stdio.h>
#include <openssl/evp.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 1024
//argument : filename
//useful contants can be gound in the evp.h library 
int main(int argc,char **argv) {
        EVP_MD_CTX *md;//allocate varibale and should be this type EVP_MD_ctx
        unsigned char md_value[EVP_MAX_MD_SIZE]; //where to store digest ...this is constant 
        int n,i,md_len;
        unsigned char buf[BUF_SIZE];
        FILE *fin;



        if(argc < 2) {
            printf("Please give a filename to compute the SHA-1 digest on\n");
            exit(1);
        }

        if((fin = fopen(argv[1],"r")) == NULL) { //open file for reading 
                printf("Couldnt open input file, try again\n");
                exit(1);
        }

        //create a message digest context

        //EVP_MD_CTX *EVP_MD_CTX_new(void);
		    md = EVP_MD_CTX_new(); // create the context to variable name for computing message digest...empty context ready for computing digest


        //int EVP_DigestInit(EVP_MD_CTX *ctx, const EVP_MD *type);
        // int EVP_DigestInit_ex(EVP_MD_CTX *ctx, const EVP_MD *type, ENGINE *impl);
        EVP_DigestInit_ex(md, EVP_sha1(),NULL); //name of context and pointer of digest algorithm and null 


        //reading info from the file using the fread and allocate the buffer and need (1) size of object and need buffer size and file namewhere to take input
        //return number of bytes > 0 it means there is still the data to read
        //int EVP_DigestUpdate(EVP_MD_CTX *ctx, const void *d, size_t cnt);
        while((n = fread(buf,1,BUF_SIZE,fin)) > 0)
			       EVP_DigestUpdate(md, buf, n);
        //perform finalization
        //where to store actual digest(md_value) and where to store size of message digest to variable(md_len)
        //int EVP_DigestFinal_ex(EVP_MD_CTX *ctx, unsigned char *md, unsigned int *s);
        if(EVP_DigestFinal_ex(md, md_value, &md_len) != 1) {
				      printf("Digest computation problem\n");
				          exit(1);
        }

        // void EVP_MD_CTX_free(EVP_MD_CTX *ctx);
		    EVP_MD_CTX_free(md);

        printf("The digest is: ");
        for(i = 0; i < md_len; i++)
			     printf("%02x", md_value[i]);
        printf("\n");

	return 0;
}
//gcc -o sha1.exe hash.c -lcrypto 
//./sha1.exe fileeee
// openssl dgst -sha1 file

