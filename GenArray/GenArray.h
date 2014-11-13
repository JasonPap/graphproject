#ifndef GENARRAY_H
#define GENARRAY_H


class GenArray
{

private:

	int size;
	void CopyArray(void* B[], int iBegin, int iEnd, void* A[]);
    void TopDownSplitMerge(void* A[],int iBegin, int iEnd, void* B[]);
    void TopDownMerge(void* A[], int iBegin, int iMiddle, int iEnd, void* B[]);
public:

	void** arrayPtr;
	int num_of_items;

	GenArray(int);
	~GenArray();
	bool addCell();
	bool doubleCells();
	int getSize();
	int getNumOfItems();
	int fillIt();
	bool isFull();
    void Empty();
	void merge_sort();
	void print();

};
#endif // GENARRAY_H
