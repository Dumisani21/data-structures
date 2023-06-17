
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }
    
    add(value) {
        if (this.head == null) {
            this.head = new Node(value);
            return;
        }
        
        let node = this.head;
        
        while (node.next != null) {
            node = node.next;
        }
        
        node.next = new Node(value);
    }
}

let listNums = new LinkedList();
listNums.add(1);
listNums.add(2);
listNums.add(3);
listNums.add(4);

let node = listNums.head;
while (node != null) {
    console.log(`node: [${node.data}]`);
    node = node.next;
}