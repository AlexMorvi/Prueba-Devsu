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
- Python 3.12
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
```
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
   |   +-- test_report.html       # Reporte HTML
   +-- config.py                  # Configuracion por entorno
   +-- pytest.ini                 # Configuracion de Pytest
   +-- requirements.txt           # Dependencias del proyecto
   +-- run_tests.py               # Script principal de ejecucion
   +-- conclusiones.txt           # Hallazgos y analisis tecnico
   +-- README.txt                 # Documentacion
```

GUIA DE INSTALACION
-------------------
1. Clonar el repositorio
   - git clone https://github.com/AlexMorvi/Ejercicios-E2E-y-API.git
   - cd Ejercicios-E2E-y-API
2. Navegar a la carpeta del proyecto
   - cd "Ejercicio E2E"
3. Crear entorno virtual
   - python -m venv .venv
4. Activar entorno virtual
   - Windows: .venv\Scripts\activate
   - Linux/Mac: source .venv/bin/activate
5. Instalar dependencias
   - pip install -r requirements.txt

REQUISITOS PREVIOS
------------------
- Python 3.8+ (recomendado 3.12)
- Google Chrome o Microsoft Edge
- Conexion a internet para la primera ejecucion de WebDriver Manager

EJECUCION DE PRUEBAS
--------------------
Opcion 1: ejecucion rapida
```
python run_tests.py
```

Opcion 2: ejecucion con pytest
```
pytest tests/ -v --html=reports/test_report.html --self-contained-html
pytest tests/test_purchase_flow.py::test_complete_purchase_flow -v
```

Opcion 3: modo headless
```
set HEADLESS=true && python run_tests.py
```

VARIABLES DE ENTORNO UTILES
---------------------------
- BROWSER=auto|chrome|edge
- BASE_URL=https://www.demoblaze.com/
- EXPLICIT_WAIT=20
- PYTEST_MARKER=smoke

CASOS DE PRUEBA
--------------
- test_complete_purchase_flow: flujo completo de compra
- test_add_and_remove_from_cart: alta y baja de productos
- test_empty_cart_checkout: validacion de checkout con carrito vacio

DATOS DE PRUEBA
--------------
```
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
```

REPORTES Y EVIDENCIAS
---------------------
- Reporte HTML: reports/test_report.html
- Screenshots en fallos: reports/screenshots/

SOLUCION DE PROBLEMAS COMUNES
-----------------------------
- Error "No compatible browsers could be set up!": verificar Chrome o Edge instalado.
- Error "ChromeDriver not found": verificar conexion a internet o ejecutar nuevamente.
- Error "Connection timeout": usar modo headless o incrementar EXPLICIT_WAIT en config.py.
- Error "Element not found": revisar localizadores en pages/.

INFORMACION DEL PROYECTO
------------------------
- Fecha de creacion: 25 de Septiembre, 2025
- Ultima actualizacion: 03 de Mayo, 2026
- Version: 2.1
- Autor: Alexander Morales
- Sitio objetivo: https://demoblaze.com/
- Estado del proyecto: completo y listo para evaluacion
