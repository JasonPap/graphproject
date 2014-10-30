class GenArray
{

private:

	int size;
	int currentSize;
	void** arr;

public:
	GenArray(int);
	~GenArray();
	bool addCell();
	bool doubleCells();
	int getSize();
	int fillIt();

};
