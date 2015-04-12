
public class Pair<T, K>{
    private T object1;
    private K object2;
    
    public T getObject1() {
        return object1;
    }
    public K getObject2() {
        return object2;
    }
    @Override
    public String toString(){
        return object1.toString() + object2.toString();
    }
    //@Override
    public boolean equals(Pair<T, K> other){
        if (object1 == other.getObject1() && object2 == other.getObject2()){
            return true;
        }
        return false;
    }
    
}
