#include <stdio.h> 
#include <stdlib.h> 
#include <stdbool.h> 
#define ROW 4 
#define COL 5 


typedef struct Node 
{ 
	bool isEndOfCol; 
	struct Node *child[2];
} Node; 

Node* newNode() 
{ 
	Node* temp = (Node *)malloc( sizeof( Node ) ); 
	temp->isEndOfCol = 0; 
	temp->child[0] = temp->child[1] = NULL; 
	return temp; 
} 

bool insert( Node** root, int (*M)[COL], int row, int col ) 
{ 
	if ( *root == NULL ) 
		*root = newNode(); 

	if ( col < COL ) 
		return insert ( &( (*root)->child[ M[row][col] ] ), M, row, col+1 ); 

	else 
	{ 
		if ( !( (*root)->isEndOfCol ) ) 
			return (*root)->isEndOfCol = 1; 

		return 0; 
	} 
} 


void printRow( int (*M)[COL], int row ) 
{ 
	int i; 
	for( i = 0; i < COL; ++i ) 
		printf( "%d ", M[row][i] ); 
	printf("\n"); 
} 



void findUniqueRows( int (*M)[COL] ) 
{ 
	Node* root = NULL;  
	int i; 
	for ( i = 0; i < ROW; ++i ) 
		if ( insert(&root, M, i, 0) ) 
			printRow( M, i ); 
} 

int main() 
{ 
	int M[ROW][COL] = {{0, 1, 0, 0, 1}, 
		{1, 0, 1, 1, 0}, 
		{0, 1, 0, 0, 1}, 
		{1, 0, 1, 0, 0} 
	}; 
	findUniqueRows( M ); 
	return 0; 
} 
