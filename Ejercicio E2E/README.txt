EJERCICIOS E2E Y API - DEMOBLAZE AUTOMATION
==========================================

DESCRIPCION DEL PROYECTO
------------------------
Este proyecto contiene pruebas automatizadas End-to-End (E2E) para el sitio web
Demoblaze.com utilizando Selenium WebDriver y Python. El framework de pruebas
es pytest y Selenium es un requisito obligatorio.

OBJETIVO
--------
Automatizar el flujo completo de compra en Demoblaze.com, validando:
- Agregar dos productos especificos al carrito
- Visualizar y verificar el contenido del carrito
- Completar el formulario de compra con datos validos
- Finalizar la compra exitosamente

TECNOLOGIAS Y FRAMEWORK
-----------------------
- Python 3.12 (compatible con 3.8+)
- Selenium WebDriver 4.15.2 (requerido)
- Pytest 7.4.3 (framework de testing)
- WebDriver Manager 3.9.1
- pytest-html 4.1.1

ARQUITECTURA
------------
- Page Object Model (POM) para encapsular la logica de paginas
- Fixtures de pytest para inicializacion de drivers y paginas
- Configuracion por entorno en config.py
- Evidencia automatica en reports/

ESTRUCTURA DEL PROYECTO
-----------------------
Ejercicios-E2E-y-API/
+-- Ejercicio E2E/                 # Proyecto principal
   +-- pages/                     # Page Object Model
   |   +-- __init__.py
   |   +-- base_page.py           # Base de POM con waits y helpers
   |   +-- home_page.py           # Pagina principal de Demoblaze
   |   +-- product_page.py        # Pagina individual de producto
   |   +-- cart_page.py           # Pagina del carrito de compras
   |   +-- checkout_page.py       # Pagina de checkout y compra
   +-- tests/                     # Casos de prueba E2E
   |   +-- __init__.py
   |   +-- conftest.py            # Fixtures y hooks de Pytest
   |   +-- data.py                # Datos de prueba
   |   +-- test_purchase_flow.py  # Suite completa de pruebas
   +-- utils/                     # Utilidades del sistema
   |   +-- __init__.py
   |   +-- driver_manager.py      # Gestor automatico de WebDriver
   |   +-- logging_config.py      # Configuracion de logging
   +-- reports/                   # Reportes de ejecucion
   +-- config.py                  # Configuracion por entorno
   +-- pytest.ini                 # Configuracion de Pytest
   +-- requirements.txt           # Dependencias del proyecto
   +-- run_tests.py               # Script principal de ejecucion
   +-- conclusiones.txt           # Hallazgos y analisis tecnico
   +-- README.txt                 # Documentacion (este archivo)

GUIA DE INSTALACION
-------------------
1. Clonar el repositorio
   - git clone <url-del-repositorio>

2. Navegar a la carpeta del proyecto
   - cd "Ejercicio E2E"

3. Crear entorno virtual
   - python -m venv .venv

4. Activar entorno virtual
   - Windows (CMD):       .venv\Scripts\activate
   - Windows (PowerShell): .venv\Scripts\Activate.ps1
   - Linux/Mac:           source .venv/bin/activate

5. Instalar dependencias
   - pip install -r requirements.txt

6. Verificar instalacion
   - python -c "import selenium; print(selenium.__version__)"
   - pytest --version

REQUISITOS PREVIOS
------------------
- Python 3.8+ (recomendado 3.12)
  Descargar desde: https://www.python.org/downloads/
  IMPORTANTE: Marcar "Add Python to PATH" durante la instalación en Windows.
- Google Chrome o Microsoft Edge instalado en el sistema.
- Conexion a internet para la primera ejecucion (WebDriver Manager descarga
  el driver compatible automáticamente).

EJECUCION DE PRUEBAS
--------------------
Opcion 1: Ejecucion rapida (script incluido)
  python run_tests.py

Opcion 2: Ejecucion con pytest directamente
  pytest tests/ -v --html=reports/test_report.html --self-contained-html

Opcion 3: Ejecucion de un test especifico
  pytest tests/test_purchase_flow.py::test_complete_purchase_flow -v

Opcion 4: Modo headless (sin ventana del navegador)
  Windows (CMD):        set HEADLESS=true && python run_tests.py
  Windows (PowerShell): $env:HEADLESS="true"; python run_tests.py
  Linux/Mac:            HEADLESS=true python run_tests.py

EJECUCION DESDE IDE
--------------------
PyCharm:
  1. File > Open > seleccionar la carpeta "Ejercicio E2E".
  2. Configurar el intérprete de Python:
     File > Settings > Project > Python Interpreter > seleccionar el venv.
  3. Click derecho sobre tests/ > Run 'pytest in tests'.

VS Code:
  1. Abrir la carpeta "Ejercicio E2E".
  2. Instalar extensiones: "Python" y "Python Test Explorer".
  3. Seleccionar el intérprete del venv (Ctrl+Shift+P > Python: Select Interpreter).
  4. Usar el panel de Testing para ejecutar los tests.

IntelliJ IDEA (con plugin Python):
  1. File > Open > seleccionar la carpeta "Ejercicio E2E".
  2. Configurar el SDK de Python al venv creado.
  3. Click derecho sobre tests/ > Run 'pytest in tests'.

VARIABLES DE ENTORNO UTILES
---------------------------
- BROWSER=auto|chrome|edge       Navegador a utilizar (default: auto)
- BASE_URL=https://www.demoblaze.com/
- HEADLESS=true|false            Modo sin ventana (default: false)
- EXPLICIT_WAIT=20               Tiempo de espera en segundos (default: 15)
- PYTEST_MARKER=smoke            Ejecutar solo tests con marker específico

CASOS DE PRUEBA
--------------
- test_complete_purchase_flow: flujo completo de compra (smoke test)
- test_add_and_remove_from_cart: alta y baja de productos
- test_empty_cart_checkout: validacion de checkout con carrito vacio

DATOS DE PRUEBA
--------------
CUSTOMER_DATA = {
    "name": "Juan Perez",
    "country": "Mexico",
    "city": "Ciudad de Mexico",
    "card": "4111111111111111",
    "month": "12",
    "year": "2025",
}

PRODUCTS = ["Samsung galaxy s6", "Nokia lumia 1520"]
EXPECTED_TOTAL = 1180

REPORTES Y EVIDENCIAS
---------------------
- Reporte HTML: reports/test_report.html
- Screenshots en fallos: reports/screenshots/

SOLUCION DE PROBLEMAS
---------------------
1. Error "No compatible browsers could be set up!":
   - Verificar que Google Chrome o Microsoft Edge está instalado.
   - Si usa un navegador no estándar, establecer BROWSER=chrome o BROWSER=edge.

2. Error "ChromeDriver not found" o "SessionNotCreated":
   - Verificar conexión a internet (WebDriver Manager necesita descargar el driver).
   - Actualizar Chrome/Edge a la última versión estable.
   - Ejecutar de nuevo: pip install --upgrade webdriver-manager

3. Error "Connection timeout" o "TimeoutException":
   - Aumentar el tiempo de espera: set EXPLICIT_WAIT=30
   - Verificar conexión a internet y acceso a www.demoblaze.com.
   - Intentar en modo headless: set HEADLESS=true

4. Error "Element not found" o "StaleElementReferenceException":
   - El sitio Demoblaze puede tener latencia variable.
   - Los tests incluyen reintentos automáticos para estos casos.

5. Error "ModuleNotFoundError: No module named 'selenium'":
   - Activar el entorno virtual antes de ejecutar.
   - Reinstalar dependencias: pip install -r requirements.txt

6. PowerShell no reconoce "set HEADLESS=true && ...":
   - Usar la sintaxis de PowerShell: $env:HEADLESS="true"; python run_tests.py

INTEGRACION CONTINUA
--------------------
El proyecto incluye un pipeline de GitHub Actions (.github/workflows/e2e-tests.yml)
que ejecuta automáticamente las pruebas en modo headless con Chrome.
Los reportes HTML y screenshots se archivan como artifacts del workflow.

INFORMACION DEL PROYECTO
------------------------
- Ultima actualizacion: 31 de Mayo, 2026
- Version: 1.1
- Autor: Alexander Morales
