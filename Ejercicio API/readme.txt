EJERCICIOS E2E Y API - PETSTORE API AUTOMATION
==============================================

DESCRIPCION DEL PROYECTO
------------------------
Este proyecto contiene pruebas automatizadas para la API REST pública de 
Swagger Petstore utilizando el framework Karate DSL y Java.

OBJETIVO
--------
Automatizar el flujo completo de vida (CRUD) de la entidad Pet, validando:
- Inserción de nuevas mascotas en la plataforma.
- Consulta y extracción de mascotas por identificador.
- Actualización de los atributos y estado de mascotas existentes.
- Búsqueda generalizada y validación modular por el estado de las mascotas.

TECNOLOGIAS Y FRAMEWORK
-----------------------
- Java 11 o superior
- Apache Maven 3.9+
- Karate DSL (framework de API Testing)
- JUnit 5 / Surefire Plugin

ARQUITECTURA
------------
- Behavior Driven Development (BDD) adaptado a sintaxis implícita de Karate.
- Patrón Create-First para garantizar independencia total entre tests.
- Centralización de configuraciones dinámicas (Test Data Factory) vía JavaScript.
- Esquemas de validación de contratos JSON segregados (strict y flex).

ESTRUCTURA DEL PROYECTO
-----------------------
Ejercicios-E2E-y-API/
+-- Ejercicio API/
   +-- pom.xml                          # Dependencias y Build (Maven)
   +-- src/test/java/
   |   +-- karate-config.js             # Configuracion Karate e inyección de datos
   |   +-- petstore/
   |       +-- PetStoreTest.java        # Runner de ejecucion
   |       +-- petstore-tests.feature   # Escenarios de prueba consolidados
   |       +-- schemas/                 # Contratos de validacion
   |           +-- pet.schema.flex.json
   |           +-- pet.schema.strict.json
   +-- target/                          # Compilación y reportes generados
   +-- conclusiones.txt                 # Hallazgos tecnicos
   +-- readme.txt                       # Documentacion (este archivo)

GUIA DE INSTALACION
-------------------
1. Clonar o acceder al repositorio.
2. Navegar a la carpeta "Ejercicio API".
3. Validar las instalaciones previas en el sistema:
   - java -version
   - mvn -version
4. Descargar y resolver las dependencias:
   - mvn clean compile

REQUISITOS PREVIOS
------------------
- Java JDK 11 configurado en las variables de entorno (JAVA_HOME).
- Maven correctamente ruteado (M2_HOME / PATH).
- Acceso a internet para resolucion de plugins de Maven y alcance a petstore.swagger.io.

EJECUCION DE PRUEBAS
--------------------
Opcion 1: Ejecucion completa de la suite
  mvn test

Opcion 2: Ejecucion selectiva por etiquetas (tags)
  mvn test -Dkarate.options="--tags @addPet"
  mvn test -Dkarate.options="--tags @getPetById"
  mvn test -Dkarate.options="--tags @updatePet"
  mvn test -Dkarate.options="--tags @findPetsByStatus"

Opcion 3: Ejecucion de suite completa excluyendo ignorados
  mvn test -Dkarate.options="--tags ~@ignore"
