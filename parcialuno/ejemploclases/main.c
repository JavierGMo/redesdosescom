#include "Helper.h"

int** matrixA;
int** matrixB; 
int** matrixC;


int main(int argc,char** argv){

    if(argc<4){
        printf("Faltan parametros");
        exit(1);
    }
    int filasA=atoi(argv[1]);
    int columnasA=atoi(argv[2]);
    int columnasB=atoi(argv[3]);
    int numHilos=atoi(argv[4]);
    int NF=filasA/numHilos;
    int NR=filasA%numHilos;
    
    matrixA=createMatrix(filasA,columnasA);
    matrixB=createMatrix(columnasA,columnasB);
    fillMatrix(filasA,columnasA,matrixA);
    fillMatrix(columnasA,columnasB,matrixB);
    displayMatrix(filasA,columnasA,matrixA);
    displayMatrix(columnasA,columnasB,matrixB);


    int aux0=0;
    pthread_t threads[numHilos];
    for(;aux0<numHilos;aux0++){
        int inicio=aux0*(NF-1)+aux0;
        int final=inicio+(NF-1);
        //pthread_create(&threads[aux0],NULL,(void*),NULL);
        //pthread_create(&threads[aux0],NULL,(void*)aux0,NULL);
    }

    aux0=0;
    for(;aux0<numHilos;aux0++){
        pthread_join(threads[aux0],NULL);
    }
}