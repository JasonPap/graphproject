#pragma once
class listnode
{
public:
	//functions
	listnode(void*);
	~listnode();
	void* GetValue();

	//variables
	listnode * next;

private:
	void* data;
};

