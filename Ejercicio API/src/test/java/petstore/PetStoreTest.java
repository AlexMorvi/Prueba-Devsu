package petstore;

import com.intuit.karate.junit5.Karate;

/**
 * Karate Test Runner for PetStore API Tests.
 *
 * Execution:
 *   mvn test                                           - run all scenarios
 *   mvn test -Dkarate.options="--tags @addPet"         - run by tag
 *   mvn test -Dtest=PetStoreTest#testPetStore          - run from IDE or CLI
 */
class PetStoreTest {

    @Karate.Test
    Karate testPetStore() {
        return Karate.run("petstore-tests").relativeTo(getClass());
    }
}