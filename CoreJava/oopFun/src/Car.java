
public class Car {
    private String model;
    private String color;
    private int mileage;
    
    Car(){
        model = "";
        color = "";
        mileage = 0;
    }
    
    Car(String model, String color, int mileage){
        this.model = model;
        this.color = color;
        this.mileage = mileage;
    }
    
    public String getModel(){
        return model;
    }
    
    public String getColor(){
        return color;
    }
    
    public int getMileage(){
        return mileage;
    }
    
    public void setModel(String model) {
        this.model = model;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setMileage(int mileage) {
        this.mileage = mileage;
    }

}
