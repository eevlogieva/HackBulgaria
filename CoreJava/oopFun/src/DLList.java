
public class DLList {
    class Node{
        private Node previous;
        private Node next;
        private int inf;
        Node(Node prev, Node next, int inf){
            this.previous = prev;
            this.next = next;
            this.inf = inf;
        }
        Node(){
            this.previous = this.next = null;
            this.inf = 0;
        }
        Node(int inf){
            this.previous = this.next = null;
            this.inf = inf;
        }
        public Node getPrevious(){
            return previous;
        }
        public Node getNext(){
            return next;
        }
        public int getInf(){
            return inf;
        }
    }
        
        private Node head;
        
        public void add(int newInf){
            Node a = new Node(newInf);
            Node current = head;
            while(current.next != null){
                current = current.next;
            }
            current.next = a;
            a.previous = current;
        }
        public boolean remove(int elem){
            
        }
}
    
    

