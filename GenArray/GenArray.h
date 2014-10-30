class GenArray
{

private:

	int size;

public:

	void** arrayPtr;
	int num_of_items;

	GenArray(int);
	~GenArray();
	bool addCell();
	bool doubleCells();
	int getSize();
	int fillIt();

};
