
class Linkedlists {
    public static void main(String[] args) {
        LinkedList listNums = new LinkedList();
        listNums.add(1);
        listNums.add(2);
        listNums.add(3);
        listNums.add(4);
        
        Node node = listNums.head;
        while (node != null) {
            System.out.println(String.format("node: [%d]", node.data));
            node = node.next;
        }
        
    }
}

class Node {
    public int data;
    public Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    public Node head;
    
    public LinkedList() {
        this.head = null;
    }
    
    public void add(int value) {
        if (this.head == null) {
            this.head = new Node(value);
            return;
        }
        
        Node node = this.head;
        
        while (node.next != null) {
            node = node.next;
        }
        
        node.next = new Node(value);
    }
}