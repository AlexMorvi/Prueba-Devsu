# Prueba Técnica — Automatización E2E y API

Este repositorio contiene dos ejercicios independientes de automatización de pruebas. Cada uno tiene su propia configuración, dependencias y documentación.

> **⚠️ Importante:** Cada ejercicio se ejecuta desde su propia carpeta. No ejecute comandos desde la raíz del repositorio.

## Estructura del Repositorio

```
Prueba-Devsu/
├── Ejercicio API/          → Pruebas de API REST (Karate + Java)
├── Ejercicio E2E/          → Pruebas End-to-End (Selenium + Python)
├── .github/workflows/      → Pipelines de CI (GitHub Actions)
├── .editorconfig           → Estilos de código para IDEs (ambos ejercicios)
└── README.md               → Este archivo
```

---

## Ejercicio 1: API Tests

| | |
|---|---|
| **Stack** | Java 17 · Maven · Karate DSL 1.4.1 · JUnit 5 |
| **API** | [Swagger Petstore](https://petstore.swagger.io) |
| **Docs** | [`Ejercicio API/readme.txt`](Ejercicio%20API/readme.txt) |

### Inicio Rápido

```bash
cd "Ejercicio API"
mvn clean test
```

O con el **Maven Wrapper** incluido (no requiere Maven instalado):

```bash
cd "Ejercicio API"
./mvnw clean test          # Linux/Mac
mvnw.cmd clean test        # Windows
```

**Requisito:** Java JDK 17+ ([descargar Temurin](https://adoptium.net))

---

## Ejercicio 2: E2E Tests

| | |
|---|---|
| **Stack** | Python 3.12 · Selenium WebDriver · Pytest · Page Object Model |
| **Sitio** | [Demoblaze](https://www.demoblaze.com) |
| **Docs** | [`Ejercicio E2E/README.txt`](Ejercicio%20E2E/README.txt) |

### Inicio Rápido

```bash
cd "Ejercicio E2E"
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate             # Windows CMD
.venv\Scripts\Activate.ps1         # Windows PowerShell
source .venv/bin/activate          # Linux/Mac

pip install -r requirements.txt
python run_tests.py
```

**Requisitos:** Python 3.8+ ([descargar](https://python.org)) · Chrome o Edge instalado

---

## Ejecución desde IDE

| IDE | Ejercicio API | Ejercicio E2E |
|-----|---------------|---------------|
| **IntelliJ IDEA** | Open → `Ejercicio API` (detecta pom.xml). SDK: JDK 17+ | Requiere plugin Python. Open → `Ejercicio E2E` |
| **Eclipse** | Import → Existing Maven Projects → `Ejercicio API` | Requiere PyDev. Import → `Ejercicio E2E` |
| **VS Code** | Open Folder → `Ejercicio API`. Extensión: *Extension Pack for Java* | Open Folder → `Ejercicio E2E`. Extensión: *Python* |
| **PyCharm** | — | Open → `Ejercicio E2E`. Configurar intérprete al venv |

> **📌 Nota:** Abra cada ejercicio como proyecto independiente, no la carpeta raíz. Si abre la raíz, el IDE no detectará la configuración de Maven ni de Python automáticamente.

---

## Integración Continua

El repositorio incluye pipelines de GitHub Actions que ejecutan ambos ejercicios automáticamente:

| Workflow | Descripción |
|----------|-------------|
| [`api-tests.yml`](.github/workflows/api-tests.yml) | Karate con Java 17 en Ubuntu |
| [`e2e-tests.yml`](.github/workflows/e2e-tests.yml) | Selenium con Chrome headless en Ubuntu |

Los reportes se archivan como **artifacts** en cada ejecución.

---

**Autor:** Alexander Morales · **Versión:** 1.1 · **Última actualización:** Mayo 2026
