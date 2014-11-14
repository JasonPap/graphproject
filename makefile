CC = g++
CFLAGS = -O3
all:	graphproject
graphproject: 
	   $(CC) -o graphproject main.cpp Queue/Queue.cpp Queue/QueueNode.cpp Node/Node.cpp list/list.cpp list/listIterator.cpp list/listnode.cpp HashMap/HashMap.cpp HashMap/ResultSet/Result.cpp HashMap/ResultSet/ResultSet.cpp GenArray/GenArray.cpp Edge/Edge.cpp

clean: 
	rm -f graphproject
