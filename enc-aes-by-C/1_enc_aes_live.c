#include <stdio.h>
#include <openssl/evp.h>
#include </usr/include/stdlib.h>
#include <string.h>

//define micro
#define ENCRYPT 1
#define DECRYPT 0

#define BUF_SIZE 1024

int main(int argc, char **argv)
{

	unsigned char ibuf[BUF_SIZE], obuf[BUF_SIZE];

	int key_size, ilen, olen, tlen;

	// purpose : taking input AS string
	//encrypt with AES-128-CBC
	//output: encrypted string
	//

	// first create key and must pass to ssl as unsigned char and becuase
	// it is 128 bits we need 16 bytes
	//asci code correspond
	//gcc -o enc.exe nameof the file -lcrypto
	//./enc.exe
	unsigned char *key = (unsigned char *)"0123456789012345"; //for instance 0123.
	//these are not character and are ASCII code 
	// -K 012345 --> 01 0000 0001 0000 0010 ... -k encoded as byte 
	//3031 like 30 is asci code of 0 31 is asci of 1 when you get final output
	// iv
	unsigned char *iv = (unsigned char *)"aaaaaaaaaaaaaaaa";
	// 1010 1010 1010...
	int i;
	printf("key is: ");
	for (i = 0; i < 16; i++) //print 16 bytes of characters
		printf("%02x", key[i]);
	printf("\n");

	printf("IV is: ");
	for (i = 0; i < 16; i++)
		printf("%02x", iv[i]);
	printf("\n");

	/* algorithm EVP_aes_128_cbc()  openssl enc*/ //all algorithms are stored in EVP part of library
												  //openssl enc -e -aes-128-cbc --> EVP_CIPHER
												  //can see the name of algorithms
												  //in evp we have mode cipher and loading the enc module
	key_size = EVP_CIPHER_key_length(EVP_aes_128_cbc()); //for example can see the key size
	printf("key size = %d\n", key_size);

	/**
 start Encryption
**/
	//first we have to create the context to build environment to encryption
	//https://www.openssl.org/docs/man1.1.0/man3/EVP_CipherInit_ex.html
	// creating the object --> which is in C named context
	EVP_CIPHER_CTX *ctx; //allocate the variable(space) and object is type of EVP....
	//is data structure to store all type of attribure inside the class
	//after allocate the context and it is pointer to the objects
	/*
EVP_CIPHER_CTX *EVP_CIPHER_CTX_new(void);
*/
	ctx = EVP_CIPHER_CTX_new(); //this is pointer to context that created.masinly contrsrutture
	//allocate the space to receive the data (create the empty obj)
	//simulate oob in pure C

	/*
void EVP_CIPHER_CTX_init(EVP_CIPHER_CTX *a);
*/
	EVP_CIPHER_CTX_init(ctx); //new constructure method...initialise the variables
	// an object ready to do something with symmetric crypto
	//pass the obj to it 
	/*
int EVP_CipherInit_ex(EVP_CIPHER_CTX *ctx, const EVP_CIPHER *type,
         ENGINE *impl, const unsigned char *key, const unsigned char *iv, int enc);
*/
	//context is object that perform encryption operation

	// plug-in: AES 128 EVP_aes_128_cbc is pointer refers to algorithms that we want to use
	// use this key
	// use this IV
	// use this ENGINE which is null
	//define encryption is 0 or decrytion is 1 ...use micro
	EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, ENCRYPT);

	/* message: 16 bytes = 1 block */
	unsigned char *message = (unsigned char *)"this is amessage";//msg is 16 bytes so single blcok
	printf("message is: ");
	for (i = 0; i < strlen(message); i++)
		printf("%02x", message[i]);
	printf("\n");

	//at this point performing 2 operations passing the piece of the data to the machines and we do it with update funcstions.
	//after passed all data we have to close the operaion with final and generate final message
	//must define the buffer for output
	//length of data in olen variable that must save in buffer (cpunting the )
	/*
int EVP_CipherUpdate(EVP_CIPHER_CTX *ctx, unsigned char *out,
         int *outl, const unsigned char *in, int inl);
 int EVP_CipherFinal_ex(EVP_CIPHER_CTX *ctx, unsigned char *outm,
         int *outl);
*/
	//passing the data
	//obuf addresst of buffer to save the result
	//&olen is number of bytes that produced in output and save inside the variable and this is reference
	//take message as input and save in obuf as output and provide the the number
	//bytes that you save in buffer  
	int tot = 0;
	// char obuf[2048];
	EVP_CipherUpdate(ctx, obuf, &olen, message, strlen(message));
	printf("olen = %d\n", olen);
	tot += olen;
	// obuf [ 1111111111111111 1010101010101 ]
	// tot == 16 byte of padding
	EVP_CipherFinal_ex(ctx, obuf + tot, &olen); //saving and adding the padding right after the buffer
	//write the olen after tot characters in buffer
	tot += olen;

	printf("tot = %d\n", tot);
	printf("olen = %d\n", tlen);

	printf("output is: ");
	for (i = 0; i < tot; i++)
		printf("%02x", obuf[i]);
	printf("\n");

	/* free the context */ //to destroy the obj
	EVP_CIPHER_CTX_free(ctx);

	/////////////////////////////////////////////////////////////////
	// decrypt what has just been encrypted
	/////////////////////////////////////////////////////////////////

	ctx = EVP_CIPHER_CTX_new();
	EVP_CIPHER_CTX_init(ctx);
	EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, DECRYPT);

	int tot_dec = 0;
	unsigned char decrypted[BUF_SIZE];
//tot is 32 bytes
	EVP_CipherUpdate(ctx, decrypted, &olen, obuf, tot);
	printf("olen = %d\n", olen);
	tot_dec += olen;

	EVP_CipherFinal_ex(ctx, decrypted + tot_dec, &tlen); //compute the padding and generate the last part
	tot_dec += tlen;

	printf("tot = %d\n", tot_dec);
	printf("olen = %d\n", tlen);

	printf("decrypted is: ");
	for (i = 0; i < tot_dec; i++)
		printf("%02x", decrypted[i]);
	printf("\n");

	/* free the context */
	EVP_CIPHER_CTX_free(ctx);

	return 0;
}