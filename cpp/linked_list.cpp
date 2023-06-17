#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int value) {
        this->data = value;
        this->next = NULL;
    }
};

class LinkedList {
public:
    Node* head;
    
    LinkedList() {
        head = NULL;
    }
    
    void add(int value) {
        if (head == NULL) {
            head = new Node(value);
            return;
        }
        
        Node* node = head;
        while (node->next != NULL) {
            node = node->next;
        }
        node->next = new Node(value);
    }
};

int main() {
    LinkedList nums;
    nums.add(1);
    nums.add(2);
    nums.add(3);
    
    Node* itr = nums.head;
    while (itr) {
        cout << itr->data << endl;
        itr = itr->next;
    }

    return 0;
}
