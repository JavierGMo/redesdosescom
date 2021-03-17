#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define FROM 1
#define TO 4

typedef struct params{
    int inicio;
    int fin;
} params;

int** createMatrix(int rows,int columns){
    int** matrix=(int**)malloc(sizeof(int*)*rows);
    int i=0;
    for(;i<rows;i++)
        matrix[i]=(int*)malloc(sizeof(int)*columns);
    return matrix;
}

void displayMatrix(int rows,int columns,int** matrix){
    int i=0;
    for(;i<rows;i++){
        int j=0;
        for(;j<columns;j++)
            printf("%d\t",matrix[i][j]);
        printf("\n");
    }
}

int createRandomValue(){
    
    return rand()%(TO-FROM+1)+FROM;
}

void fillMatrix(int rows,int columns,int** matrix){
    srand(time(NULL));
    int i=0;
    for(;i<rows;i++){
        int j=0;
        for(;j<columns;j++)
            matrix[i][j]=createRandomValue();
    }
}

