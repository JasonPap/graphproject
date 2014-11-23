#include "BinarySearch.h"

/*

Returns the index where the x paremeter is

*/

int binarySearch(int * array, int size, int x)
{
	int min = 0, max = size - 1;
	int mid = (max + min) / 2;


	while (min <= max)
	{
		if (array[mid] == x)
		{
			return mid;
		}
		else if (array[mid] < x)
		{
			min = mid + 1;
			mid = (min + max) / 2;
		}
		else if (array[mid] > x)
		{
			max = mid - 1;
			mid = (min + max) / 2;
		}
	}
	return -1;
}
