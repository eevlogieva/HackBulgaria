
public class MainCar {
    public static void main(String[] args){
        Car a = new Car("Audi", "red", 2000);
        Car b = new Car("BMW", "blue", 1000);
        Car c = new Car("Wolkswagen", "green", 0);
        Car d = new Car("Volvo", "yellow", 0);
        System.out.println(a.getModel() + " - " + a.getMileage());
        System.out.println(b.getModel() + " - " + b.getMileage());
        System.out.println(c.getModel() + " - " + c.getMileage());
        System.out.println(d.getModel() + " - " + d.getMileage());
   }
}
