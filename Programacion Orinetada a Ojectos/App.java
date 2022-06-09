public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World! como andas");
        Car car = new Car("jk",new Account("jhas","jh"));
        car.license="123";
        car.imprima();
        
        
        
        Car car2 = new Car("jk",new Account("julio","3546"));
        car2.license="123";
        
        System.out.println("nombre del sr " + car2.driver.name  +" "+  car2.license);

    }
}
