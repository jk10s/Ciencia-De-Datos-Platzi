import java.util.ArrayList;
import java.util.Map;


public class UberVan extends Car {
    Map<String, ArrayList<Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    
    public UberVan(String license, Account driver,
    Map<String, ArrayList<Integer>> typeCarAccepted,
    ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted=typeCarAccepted;
        this.seatsMaterial=seatsMaterial;

    }
}
 