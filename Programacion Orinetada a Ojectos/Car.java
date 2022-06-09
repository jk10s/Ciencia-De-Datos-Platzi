public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passengenger;

    public Car(String license,Account driver) {
        this.license=license;
        this.driver=driver;
        
    }

    public void imprima() {
        System.out.println("metodo y el nombre es"+driver.name);
        
    }
    
}
