package petstore;

import com.intuit.karate.junit5.Karate;

public class PetStoreTest {
    
    @Karate.Test
    public Karate testPetStore() {
        return Karate.run("petstore-tests").relativeTo(getClass());
    }
}