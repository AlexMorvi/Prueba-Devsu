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
- Java 17 o superior (JDK Temurin recomendado)
- Apache Maven 3.8+ (incluido via Maven Wrapper)
- Karate DSL 1.4.1 (framework de API Testing)
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
   +-- mvnw / mvnw.cmd                  # Maven Wrapper (Linux/Windows)
   +-- .mvn/wrapper/                    # Configuracion del Maven Wrapper
   +-- src/test/java/
   |   +-- karate-config.js             # Configuracion Karate e inyección de datos
   |   +-- petstore/
   |       +-- PetStoreTest.java        # Runner de ejecucion
   |       +-- petstore-tests.feature   # Escenarios de prueba consolidados
   |       +-- schemas/                 # Contratos de validacion
   |           +-- pet.schema.flex.json
   |           +-- pet.schema.strict.json
   +-- src/main/java/                   # Estructura Maven estándar (vacío)
   +-- conclusiones.txt                 # Hallazgos tecnicos
   +-- readme.txt                       # Documentacion (este archivo)

GUIA DE INSTALACION
-------------------
1. Clonar o acceder al repositorio.
2. Navegar a la carpeta "Ejercicio API".
3. Validar las instalaciones previas en el sistema:
   - java -version    (debe ser Java 17 o superior)
4. Descargar y resolver las dependencias (compilar las fuentes de test):
   - mvn clean test-compile
   O usar el Maven Wrapper incluido (no requiere Maven instalado):
   - ./mvnw clean test-compile          (Linux/Mac)
   - mvnw.cmd clean test-compile        (Windows)

REQUISITOS PREVIOS
------------------
- Java JDK 17 o superior configurado en las variables de entorno (JAVA_HOME).
  Se recomienda Eclipse Temurin (https://adoptium.net/).
- Maven 3.8+ ruteado correctamente (M2_HOME / PATH).
  ALTERNATIVA: Usar el Maven Wrapper incluido (mvnw / mvnw.cmd) que no
  requiere una instalación global de Maven.
- Acceso a internet para resolución de plugins de Maven y alcance a
  petstore.swagger.io.

EJECUCION DE PRUEBAS
--------------------
Opcion 1: Ejecucion completa de la suite
  mvn test
  O con Maven Wrapper:
  ./mvnw test               (Linux/Mac)
  mvnw.cmd test              (Windows)

Opcion 2: Ejecucion selectiva por etiquetas (tags)
  mvn test -Dkarate.options="--tags @addPet"
  mvn test -Dkarate.options="--tags @getPetById"
  mvn test -Dkarate.options="--tags @updatePet"
  mvn test -Dkarate.options="--tags @findPetsByStatus"

Opcion 3: Ejecucion de suite completa excluyendo ignorados
  mvn test -Dkarate.options="--tags ~@ignore"

EJECUCION DESDE IDE
--------------------
IntelliJ IDEA:
  1. Abrir la carpeta "Ejercicio API" como proyecto Maven (File > Open).
  2. IntelliJ detectará automáticamente el pom.xml.
  3. Asegurar que el JDK del proyecto sea 17+ (File > Project Structure > SDK).
  4. Click derecho sobre PetStoreTest.java > Run 'PetStoreTest'.

Eclipse:
  1. File > Import > Existing Maven Projects.
  2. Seleccionar la carpeta "Ejercicio API".
  3. Asegurar que el JRE del workspace sea 17+ (Window > Preferences > Java).
  4. Click derecho sobre PetStoreTest.java > Run As > JUnit Test.

VS Code:
  1. Instalar extensiones: "Extension Pack for Java" y "Test Runner for Java".
  2. Abrir la carpeta "Ejercicio API".
  3. Usar el panel de Testing para ejecutar PetStoreTest.

REPORTES
--------
Tras ejecutar las pruebas, los reportes se generan en:
  - target/karate-reports/karate-summary.html  (reporte visual de Karate)
  - target/surefire-reports/                   (reporte estándar de Maven)

Para ver el reporte de Karate en el navegador:
  Abrir el archivo target/karate-reports/karate-summary.html

SOLUCION DE PROBLEMAS
---------------------
1. Error "java.lang.UnsupportedClassVersionError":
   Causa: Se está usando un JDK inferior a 17.
   Solución: Instalar JDK 17+ y configurar JAVA_HOME correctamente.
   Verificar con: java -version

2. Error "No sources to compile" al ejecutar mvn compile:
   Esto es NORMAL. El proyecto solo tiene fuentes de test (src/test/java).
   Use "mvn test" o "mvn test-compile" en su lugar.

3. Error "Tests run: 0":
   Causa: La clase runner no fue detectada por Surefire.
   Solución: Verificar que se ejecuta desde la carpeta "Ejercicio API"
   y que Maven Surefire plugin está correctamente configurado en pom.xml.

4. Problemas de red/SSL con la API de PetStore:
   La API pública en petstore.swagger.io puede tener latencia variable.
   La configuración SSL está habilitada en karate-config.js.

INTEGRACION CONTINUA
--------------------
El proyecto incluye un pipeline de GitHub Actions (.github/workflows/api-tests.yml)
que ejecuta automáticamente las pruebas en cada push al repositorio.
Los reportes de Karate se archivan como artifacts del workflow.

INFORMACION DEL PROYECTO
------------------------
- Ultima actualizacion: 31 de Mayo, 2026
- Version: 1.1
- Autor: Alexander Morales