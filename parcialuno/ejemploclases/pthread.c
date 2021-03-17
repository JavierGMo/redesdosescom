#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

#define numHilos 20

typedef struct valor {
    int i;
    char* msj;
} valor;


void *printHilo(void *arg) {
    valor aux = *((valor*)arg);
    int salida = 9;

    printf("%s: %i\n", aux.msj, aux.i);
    free(arg);
    pthread_exit((void*) &salida);
}
    
int  main (int  argc , char *argv []) {

    pthread_t  *hilos;
    valor *hilosValor;
    int **retorno;
    hilos = (pthread_t*) malloc (sizeof(pthread_t)*numHilos);

    for (int i = 0; i < numHilos; i++) {
        hilosValor = (valor*) malloc (sizeof(valor));
        hilosValor->i = i;
        hilosValor->msj = "Hola Mundo! :D";
        pthread_create(&hilos[i], NULL, printHilo, (void*)hilosValor);
    }
    
    for (int i = 0; i < numHilos; i++){
        pthread_join(hilos[i], (void**)&retorno[0]);
        printf("%i\n", retorno[0]);
    }

    free(hilos);
    
    printf ("\nFin\n");
    
    return 0;    
}