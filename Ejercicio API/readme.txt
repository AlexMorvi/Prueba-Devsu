INSTRUCCIONES PASO A PASO PARA EJECUTAR LAS PRUEBAS DE API PETSTORE CON KARATE
================================================================================

PRERREQUISITOS
--------------
✓ Java 11
✓ Maven 3.9.9
✓ Conexión a internet (para acceder a la API de PetStore)

INSTALACIONES COMPLETADAS AUTOMÁTICAMENTE:
- Java JDK: C:\Program Files\Eclipse Adoptium\jdk-11.0.28.6-hotspot
- Maven: C:\Maven\apache-maven-3.9.9
- Variables de entorno configuradas para el usuario actual

VERIFICACIÓN DE PRERREQUISITOS
------------------------------
Ejecutar los siguientes comandos en PowerShell para verificar las instalaciones:

java -version
mvn -version

ESTRUCTURA DEL PROYECTO
-----------------------
petstore-api-tests/
├── pom.xml                              # Configuración Maven con dependencias de Karate
├── src/test/java/petstore/
│   ├── PetStoreRunner.java             # Clase runner para ejecutar los tests
│   ├── karate-config.js                # Configuración base de Karate
│   └── petstore-tests.feature          # Archivo con todos los escenarios de prueba
├── readme.txt                          # Este archivo
└── conclusiones.txt                    # Hallazgos y conclusiones

PASOS PARA EJECUTAR LAS PRUEBAS
-------------------------------

1. NAVEGAR AL DIRECTORIO DEL PROYECTO
   Abrir PowerShell y navegar a la carpeta del proyecto:
   cd "c:\Users\ariel.morales\Documents\GitHub\Ejercicios-E2E-y-API\Ejercicio API"

2. INSTALAR DEPENDENCIAS
   Ejecutar el siguiente comando para descargar las dependencias de Maven:
   mvn clean compile

3. EJECUTAR TODAS LAS PRUEBAS
   Para ejecutar todos los escenarios de prueba:
   mvn test

4. EJECUTAR CON REPORTES DETALLADOS
   Para generar reportes HTML detallados:
   mvn test -Dkarate.options="--tags ~@ignore"

5. VER RESULTADOS
   Los resultados se mostrarán en la consola y también se generarán reportes HTML en:
   target/karate-reports/

DESCRIPCIÓN DE LOS ESCENARIOS DE PRUEBA
---------------------------------------

Los tests implementan 4 escenarios INDEPENDIENTES siguiendo patrones estándar de API testing:

📋 COMPORTAMIENTO ESTÁNDAR DE LA API:
La API de PetStore sigue patrones REST estándar:
- GET a un ID inexistente: Retorna 404 (Pet not found)
- Los pets deben crearse explícitamente usando POST /pet
- Los tests siguen el patrón estándar de setup → ejecución → validación
- Cada test crea sus propios datos de prueba para garantizar independencia

TEST 1: Añadir una mascota a la tienda (@addPet)
- Endpoint: POST /pet
- Entrada: JSON con datos completos generados dinámicamente
- ID único: Generado usando timestamp para evitar conflictos
- Variables: petId, petName, categoryName, tagName generados automáticamente
- Validaciones: ID, nombre, status, categoría devueltos correctamente
- Salida: Mascota creada exitosamente con respuesta HTTP 200

TEST 2: Consultar mascota por ID - Patrón estándar (@getPetById)
- Setup: Crea un pet usando POST /pet con datos de prueba específicos
- Endpoint: GET /pet/{petId}
- Comportamiento: Consulta el pet previamente creado en el mismo escenario
- Validaciones: Verifica que los datos devueltos coincidan exactamente con los creados
- Salida: Pet consultado exitosamente con validación completa de datos

TEST 3: Actualizar el nombre de la mascota y el estatus a "sold" (@updatePet)
- Endpoint: PUT /pet  
- Entrada: JSON con datos actualizados dinámicamente
- Precondición: Crea mascota inicial con ID único generado
- Proceso: Actualiza nombre y cambia status de "available" a "sold"
- Variables: updatedPetName generado, transición de status documentada
- Validaciones: Cambios aplicados correctamente, campos no modificados preservados
- Salida: Mascota actualizada con nuevos datos confirmados y auditados

TEST 4: Consultar mascotas por estatus con validación flexible (@findPetsByStatus)
- Endpoint: GET /pet/findByStatus?status=sold
- Entrada: Parámetro query status="sold"
- Precondición: Crea y actualiza mascota a "sold" con delay para consistencia
- Comportamiento: Validación flexible para manejar datos variables de la API demo
- Variables: Lista de mascotas, validación de schema adaptable
- Validaciones: Estructura correcta, todos los pets tienen status="sold"
- Salida: Lista validada de mascotas "sold" con verificación de consistencia

CARACTERÍSTICAS DE LA IMPLEMENTACIÓN PROFESIONAL:
- Sintaxis nativa de Karate (sin step definitions externas)
- Cada escenario es completamente INDEPENDIENTE y autocontenido
- Patrón create-first para tests de consulta, garantizando datos disponibles
- IDs únicos generados dinámicamente usando timestamps para evitar conflictos
- Test data factory pattern para generación consistente de datos
- Tags profesionales (@addPet, @getPetById, @updatePet, @findPetsByStatus)
- Validación de schema flexible para manejar variabilidad de la API
- Documentación completa de objetivos, reglas de negocio y outcomes esperados
- Configuración por entornos centralizada en karate-config.js
- Delays estratégicos para manejar consistencia eventual de datos

VARIABLES Y DATOS DE PRUEBA (TEST DATA FACTORY)
-----------------------------------------------
- baseTimestamp: java.lang.System.currentTimeMillis() (timestamp base para sesión)
- sessionPetId: Math.floor(baseTimestamp % 1000000) (ID base único por sesión)
- generateScenarioId(offset): Genera IDs únicos por escenario evitando conflictos
- buildPetData(petId, name, status): Función factory para crear objetos pet consistentes

DATOS GENERADOS DINÁMICAMENTE:
- petId: Único por escenario (sessionPetId + offset)
- petName: "API Test Pet - {petId}" o variaciones por escenario
- categoryId: 1 (fijo)
- categoryName: "Automation Test Category" (descriptivo)
- tagId: 100 (fijo)
- tagName: "automated-test" (identificador de tests automatizados)
- photoUrls: Array con URL única por pet
- baseUrl: "https://petstore.swagger.io/v2" (API demo endpoint)

EJECUCIÓN POR ESCENARIOS INDIVIDUALES:
- Todos los tests: mvn test
- Solo creación: mvn test -Dkarate.options="--tags @addPet"
- Solo consulta con patrón create-first: mvn test -Dkarate.options="--tags @getPetById"
- Solo actualización: mvn test -Dkarate.options="--tags @updatePet"
- Solo búsqueda por status: mvn test -Dkarate.options="--tags @findPetsByStatus"
- Tests de smoke: mvn test -Dkarate.options="--tags @smoke"
- Tests CRUD completos: mvn test -Dkarate.options="--tags @create,@read,@update,@query"

COMANDOS ÚTILES ADICIONALES
---------------------------

Para ejecutar tests con reportes detallados:
mvn clean test

Para ejecutar solo un escenario específico por nombre:
mvn test -Dkarate.options="--name '1. Añadir una mascota'"

Para ejecutar con logs más detallados:
mvn test -Dkarate.env=dev

Para generar reportes HTML completos:
mvn test (los reportes se generan automáticamente en target/karate-reports/)

RESOLUCIÓN DE PROBLEMAS COMUNES
-------------------------------

1. Error de conexión a la API:
   - Verificar conexión a internet
   - Comprobar que https://petstore.swagger.io/v2 esté disponible
   - Verificar que el endpoint responda: curl https://petstore.swagger.io/v2/pet/findByStatus?status=available

2. Error de compilación Maven:
   - Verificar que Java 11+ esté instalado: java -version
   - Verificar que Maven esté instalado: mvn -version
   - Limpiar y recompilar: mvn clean compile

3. Tests fallan (Exit Code: 1):
   - Verificar que la API esté disponible
   - Revisar logs detallados en la consola
   - Verificar reportes en target/surefire-reports/

4. Error "no step-definition method match found":
   - Este error indica mezcla de sintaxis Cucumber con Karate
   - En Karate solo usar: Given path, When method, Then status
   - No usar: Given I want to..., When I send..., Then I should...

5. Problemas de permisos:
   - Asegurar que el directorio target/ tenga permisos de escritura
   - En Windows: Ejecutar PowerShell como administrador si es necesario

CONTACTO Y SOPORTE
------------------
En caso de problemas, revisar:
1. Los logs en target/karate.log
2. Los reportes HTML en target/karate-reports/
3. La documentación oficial de Karate: https://github.com/karatelabs/karate

NOTA IMPORTANTE
---------------
Este proyecto utiliza la API pública de PetStore (https://petstore.swagger.io/v2).
Los datos son reales pero temporales, por lo que pueden ser modificados o eliminados
por otros usuarios de la API.