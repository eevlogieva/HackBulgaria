
public class UniqueStack extends StackImpl {
    @Override
    public void push(int newElem){
        for (int i = 0; i < size; i++){
            if(arr[i] == newElem){
                System.out.println("The stack must be unique!");
                break;
            }
            super.push(newElem);
        }
    }
}
