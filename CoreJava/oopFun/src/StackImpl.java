
public class StackImpl implements Stack{
    protected int[] arr;
    protected int capacity;
    protected int size;
    
    StackImpl(){
        capacity = 20;
        size = 0;
        arr = new int[capacity];
    }
    
    StackImpl(int capacity, int size){
        this.capacity = capacity;
        this.size = size;
        arr = new int[capacity];
    }
    
    public boolean isEmpty(){
        return size == 0;
    }
    
    public void push(int newElem){
        if (size == capacity){
            capacity *= 2;
            int[] b = arr;
            arr = new int[capacity];
            arr = b;
        }
        arr[size++] = newElem;
    }
    
    public int pop(){
        size -= 1;
        return arr[size + 1];
    }
    
    public int length(){
        return size;
    }
    
    public void clear(){
        size = 0;
    }
}

