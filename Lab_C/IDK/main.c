#include <stdio.h>
#include <stdlib.h>

struct node{
    int val;
    struct node *next;
};

struct list{
    struct node *first;
    struct node *last;
    int size;
};

void read(int *val) { scanf("%d", val); }
void print(int val) { printf("%d", val); printf("\n"); }

void add_elm_to_end(struct list *List, int val)
{
    struct node *Node = NULL;
    Node = malloc(sizeof(struct node));
    Node -> val = val;
    Node -> next = NULL;
    List -> last -> next = Node;
    List -> last = Node;
}


void del_elm(struct list List, int pos)
{
    pos --;
    int i = 0;
    struct node *Node = List.first;
    struct node a = *Node;

    while(i < pos && (Node -> next != List.last))
    {
        Node = Node -> next;
        a = *Node;
        i ++;
    }

    struct node *Next = (Node -> next) -> next;
    free(Node -> next);
    Node -> next = Next;
}



void print_list(struct node *Node)
{
    print(Node -> val);
    if (Node -> next != NULL)
        print_list(Node -> next);
}

int main()
{
    int n, nr;
    read(&n);

    struct list  List;
    List.first = NULL;
    List.last = NULL;
    List.size = 0;

    struct node *Node = NULL;
    Node = malloc(sizeof(struct node));
    Node -> next = NULL;
    List.size = 1;

    read(&(Node -> val));

    List.first = Node;
    List.last = List.first;

    for(int i = 1; i < n; i ++)
    {
        List.size ++;
        int nr;
        read(&nr);
        add_elm(&List, nr);
    }
    del_elm(List, 1);

    print_list(List.first);

    return 0;
}
