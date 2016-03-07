#include <stdio.h>
#include <stdlib.h>

// @reference https://www.cs.rit.edu/~ark/lectures/gc/03_03_02.html

#define HEAP_SIZE 1024

typedef struct MemBlock {
    int start, size;
    struct MemBlock *next;
} MemBlock;

const size_t MBISZ = sizeof(MemBlock);

char __heap[HEAP_SIZE];
typedef char* pointer;

char* ff_init(size_t heap_size) {
	if (HEAP_SIZE <= MBISZ) {
		printf("Memory too small. Cannnot initialize. Failed totally");
		exit(1);
	}
	MemBlock* block_info = (MemBlock*)__heap;
	block_info->start = MBISZ;
	block_info->size = HEAP_SIZE - MBISZ;
	block_info->next = NULL;
	return (char*)block_info;
}

MemBlock *free_list;

char* ff_malloc(size_t size) {
	MemBlock *p = free_list, *q = NULL;  // q->next == p
	while (p != NULL) {
		if (p->size > size + MBISZ) {  // split and alloc
			MemBlock* block_info = (MemBlock*)(__heap + (p->start + p->size - size - MBISZ));
			block_info->start = p->start + p->size - size;
			block_info->size = size;
			block_info->next = NULL;
			p->size -= size + MBISZ;
			return __heap + block_info->start;
		} else if (p->size >= size) {  // remove p from free list
			if (q == NULL) { // update head
				free_list = p->next;
			} else {
				q->next = p->next;
			}
			return __heap + p->start;
		} else {
			q = p;
			p = p->next;
		}
	}
	printf("No available memory. GC would start");
	return NULL;
}

int ff_free(char *addr) {
	// No strong check if addr is not valid address
	MemBlock *block_info = (MemBlock*)(addr - MBISZ);
	if (__heap + block_info->start != addr) {  // weak check
		printf("Bad addr to free");
		return 0;
	}
	MemBlock *p = free_list, *q = NULL;
	while (p != NULL) {
		if (p->start > block_info->start) {  // insert here
			if (q == NULL)
				free_list = block_info;  // insert before head
			else
				q->next = block_info;
			block_info->next = p;
			return 1;
		}
		q = p;
		p = p->next;
	}
	q->next = block_info;  // insert after tail
	return 1;
}

void show_free_list() {
	MemBlock *p = free_list;
	while (p != NULL) {
		printf("(%d, %d) ", p->start, p->size);
		p = p->next;
	}
	printf("\n=======\n");
}

int main() {
	free_list = (MemBlock*)ff_init(HEAP_SIZE);
	show_free_list();
	char *a1 = ff_malloc(100);  // a1
	show_free_list();
	char *a2 = ff_malloc(80);  // a1, a2
	show_free_list();
	char *a3 = ff_malloc(100);  // a1, a2, a3
	show_free_list();
	ff_free(a2);
	show_free_list();
	char *a4 = ff_malloc(50);
	show_free_list();
	char *a5 = ff_malloc(550);
	show_free_list();
	char *a6 = ff_malloc(50);
	show_free_list();
	char *a7 = ff_malloc(48);
	show_free_list();
	char *a8 = ff_malloc(30);
	show_free_list();
	return 0;
}