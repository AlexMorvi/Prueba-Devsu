# EJERCICIOS E2E Y API - DEMOBLAZE AUTOMATION
===============================================

## 📋 DESCRIPCION DEL PROYECTO
=============================

Este proyecto contiene pruebas automatizadas End-to-End (E2E) para el sitio web
**Demoblaze.com** utilizando **Selenium WebDriver** y **Python**. 

El proyecto está diseñado para que cualquier evaluador puede
ejecutar fácilmente sin configuración manual compleja.

### 🎯 OBJETIVO PRINCIPAL

Automatizar el **flujo completo de compra** en Demoblaze.com, validando:
- ✅ Agregar dos productos específicos al carrito
- ✅ Visualizar y verificar el contenido del carrito
- ✅ Completar el formulario de compra con datos válidos
- ✅ Finalizar la compra exitosamente

## 🛠️ TECNOLOGIAS Y HERRAMIENTAS
===============================

### Stack Tecnológico:
- **Python 3.12** - Lenguaje de programación principal
- **Selenium WebDriver 4.15.2** - Automatización de navegadores web
- **Pytest 7.4.3** - Framework de testing con reportes avanzados
- **WebDriver Manager 3.9.1** - Gestión automática de drivers de navegador
- **pytest-html 4.1.1** - Generación de reportes HTML detallados

### Navegadores Soportados:
- **Google Chrome** (Principal - recomendado)
- **Microsoft Edge** (Fallback automático)

### Arquitectura:
- **Page Object Model (POM)** - Separación de lógica de páginas
- **Sistema de logging detallado** - Transparencia total del proceso
- **Estrategias de fallback múltiples** - Máxima compatibilidad

## 📁 ESTRUCTURA DEL PROYECTO
============================

```
Ejercicios-E2E-y-API/
└── 📂 Ejercicio E2E/              # Proyecto principal
    ├── 📂 pages/                  # Page Object Model
    │   ├── __init__.py
    │   ├── home_page.py          # Página principal de Demoblaze
    │   ├── product_page.py       # Página individual de producto
    │   ├── cart_page.py          # Página del carrito de compras
    │   └── checkout_page.py      # Página de checkout y compra
    ├── 📂 tests/                  # Casos de prueba E2E
    │   ├── __init__.py
    │   └── test_purchase_flow.py # Suite completa de pruebas
    ├── 📂 utils/                  # Utilidades del sistema
    │   ├── __init__.py
    │   └── driver_manager.py     # Gestor automático de WebDriver
    ├── 📂 reports/                # Reportes de ejecución
    │   └── test_report.html      # Reporte HTML detallado
    ├── 📂 .venv/                  # Entorno virtual Python
    ├── 📄 pytest.ini             # Configuración de Pytest
    ├── 📄 requirements.txt        # Dependencias del proyecto
    ├── 📄 run_tests.py           # Script principal de ejecución
    ├── 📄 conclusiones.txt       # Hallazgos y análisis técnico
    └── 📄 README.txt             # Esta documentación
```


## GUIA DE INSTALACION
==========================================

### ⚡ Instalación Rápida (5 pasos):

```bash
# 1. Clonar el repositorio
git clone https://github.com/AlexMorvi/Ejercicios-E2E-y-API.git
cd Ejercicios-E2E-y-API

# 2. Navegar a la carpeta del proyecto
cd "Ejercicio E2E"

# 3. Crear entorno virtual
python -m venv .venv

# 4. Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 5. Instalar dependencias
pip install -r requirements.txt
```

### ✅ Requisitos Previos:
- **Python 3.8+** (recomendado 3.12)
- **Google Chrome** o **Microsoft Edge** (ya incluidos en Windows)
- **Conexión a internet** (solo para primera ejecución)

## 🎮 EJECUCION DE PRUEBAS
=========================

### 🚀 Opción 1: Ejecución Rápida (Recomendada)
```bash
# Desde la carpeta "Ejercicio E2E"
cd "Ejercicio E2E"
python run_tests.py
```

### 🔧 Opción 2: Ejecución con Pytest Directamente
```bash
# Desde la carpeta "Ejercicio E2E"
cd "Ejercicio E2E"

# Todas las pruebas con reporte HTML
pytest tests/ -v --html=reports/test_report.html --self-contained-html

# Solo el flujo completo de compra
pytest tests/test_purchase_flow.py::TestPurchaseFlow::test_complete_purchase_flow -v

# Ejecución con logs detallados
pytest tests/ -v -s
```

### 🕶️ Opción 3: Modo Headless (Sin ventana del navegador)
```bash
# Windows (desde "Ejercicio E2E")
cd "Ejercicio E2E"
set HEADLESS=true && python run_tests.py

# Linux/Mac (desde "Ejercicio E2E")
cd "Ejercicio E2E"
HEADLESS=true python run_tests.py
```

## 📊 FLUJO DETALLADO DE LAS PRUEBAS E2E
=======================================

### 🎯 TEST 1: FLUJO COMPLETO DE COMPRA (test_complete_purchase_flow)

Este es el **test principal** que valida todo el flujo de compra:

#### 📍 PASO 1: NAVEGACION A PAGINA PRINCIPAL
- Accede a https://www.demoblaze.com/
- Verifica que la página se carga correctamente
- Valida elementos principales (categorías, productos destacados)

#### 🛒 PASO 2: AGREGAR PRIMER PRODUCTO AL CARRITO
- Navega a la categoría **"Phones"**
- Busca y selecciona **"Samsung Galaxy S6"**
- Hace clic en **"Add to cart"**
- Confirma que se recibe el mensaje de éxito
- Regresa a la página principal

#### 🛒 PASO 3: AGREGAR SEGUNDO PRODUCTO AL CARRITO
- Navega nuevamente a la categoría **"Phones"**
- Busca y selecciona **"Nokia Lumia 1520"**
- Hace clic en **"Add to cart"**
- Confirma que se recibe el mensaje de éxito

#### 👁️ PASO 4: VISUALIZAR EL CARRITO DE COMPRAS
- Hace clic en el enlace **"Cart"**
- Verifica que hay **2 productos** en el carrito:
  - Samsung Galaxy S6 ($360)
  - Nokia Lumia 1520 ($820)
- Calcula y verifica el **total: $1,180**
- Valida nombres, precios y cantidades

#### 💳 PASO 5: PROCEDER AL CHECKOUT
- Hace clic en **"Place Order"**
- Verifica que se abre el modal de checkout
- Valida que todos los campos del formulario están presentes

#### 📝 PASO 6: COMPLETAR FORMULARIO DE COMPRA
Llena el formulario con datos de prueba válidos:
```
- Nombre: Juan Pérez
- País: México  
- Ciudad: Ciudad de México
- Tarjeta: 4111111111111111
- Mes: 12
- Año: 2025
```

#### 🎯 PASO 7: FINALIZAR LA COMPRA
- Hace clic en **"Purchase"**
- Verifica que aparece el mensaje de éxito
- Valida que la compra se procesó correctamente
- Cierra el modal de confirmación

### 🔄 TEST 2: GESTION DEL CARRITO (test_add_and_remove_from_cart)

Valida la funcionalidad de agregar/quitar productos:
- Agrega productos al carrito
- Verifica que se pueden eliminar productos
- Valida que el carrito se actualiza correctamente

### ⚠️ TEST 3: MANEJO DE CASOS LIMITE (test_empty_cart_checkout)

Prueba el comportamiento con carrito vacío:
- Intenta hacer checkout sin productos
- Verifica el manejo adecuado de errores
- Valida mensajes de validación del sistema

## 📈 INTERPRETACION DE RESULTADOS
=================================

### ✅ Ejecución Exitosa:
```
======================== 3 passed in 137.06s (0:02:17) ========================
✅ All tests passed!
📊 Test report generated: reports/test_report.html
```

### 📊 Métricas de Rendimiento:
- **Tiempo promedio**: 2-3 minutos para las 3 pruebas
- **Cobertura funcional**: 100% del flujo crítico de compra
- **Tasa de éxito esperada**: 3/3 pruebas (100%)
- **Compatibilidad**: Windows 10/11, Linux, macOS

### 📄 Reportes Generados:
1. **Reporte HTML**: `reports/test_report.html` (detallado con capturas)
2. **Logs de consola**: Salida en tiempo real con emojis y formato
3. **Screenshots automáticos**: En caso de fallos (para debugging)

## 🔧 SISTEMA AUTOMATICO DE DRIVERS
==================================

### 🎯 FILOSOFIA: SIMPLICIDAD PARA EVALUADORES

Este proyecto está diseñado para que **cualquier evaluador** pueda ejecutarlo
sin configuración manual de drivers. ¡NO requiere descargas manuales!

### ⚙️ COMO FUNCIONA (AUTOMATICO):

#### 🎯 ESTRATEGIA 1: WebDriver Manager (Principal)
- Detecta automáticamente la versión de Chrome/Edge instalada
- Descarga el driver compatible directamente de los repos oficiales
- Almacena en caché local para futuras ejecuciones
- Se auto-actualiza cuando el navegador se actualiza

#### 🔄 ESTRATEGIA 2: System PATH (Fallback)
- Si WebDriver Manager falla (sin internet, firewall corporativo, etc.)
- Intenta usar driver ya instalado en el PATH del sistema
- Útil para entornos corporativos con restricciones de red


## 🎨 SISTEMA DE LOGGING MEJORADO
================================

### 📊 TRANSPARENCIA TOTAL DEL PROCESO

El sistema incluye logging detallado que muestra en tiempo real:

```
================================================================================
🚀 INICIANDO FLUJO COMPLETO DE COMPRA E2E
================================================================================

📍 PASO 1: NAVEGANDO A LA PÁGINA PRINCIPAL
   • Accediendo a https://demoblaze.com...
      → Cargando URL: https://www.demoblaze.com/
      → Esperando a que la página se cargue completamente...
   ✅ Página principal cargada exitosamente

🛒 PASO 2: AGREGANDO PRIMER PRODUCTO AL CARRITO
   • Navegando a la categoría 'Phones'...
      → Buscando categoría 'Phones'...
      → Categoría 'Phones' seleccionada, cargando productos...
   • Seleccionando producto 'Samsung Galaxy S6'...
      → Buscando producto 'Samsung galaxy s6' en la página...
      → Producto 'Samsung galaxy s6' encontrado, haciendo clic...
      → Navegando a la página del producto...
   ✅ Primer producto agregado exitosamente
```

### 🎯 BENEFICIOS DEL LOGGING:
- **🔍 Transparencia**: Ves exactamente qué está pasando en cada momento
- **🐛 Debugging**: Fácil identificación de dónde fallan las pruebas
- **📊 Seguimiento**: Progreso visual del flujo de pruebas
- **✅ Validación**: Confirmación de cada paso completado

## 🛠️ SOLUCION DE PROBLEMAS COMUNES
===================================

### ❌ Error: "No compatible browsers could be set up!"
**Causa**: No se encuentra Chrome ni Edge instalado
**Solución**:
```bash
# Verificar Chrome instalado:
python -c "import os; print(os.path.exists(r'C:\Program Files\Google\Chrome\Application\chrome.exe'))"
# Si es False, instalar Chrome: https://www.google.com/chrome/
```

### ❌ Error: "ChromeDriver not found" 
**Causa**: WebDriver Manager no puede descargar el driver
**Solución**:
1. Verificar conexión a internet
2. Probar en red sin firewall corporativo
3. Los drivers se almacenan en caché para uso offline posterior

### ❌ Error: "Connection timeout"
**Causa**: Red lenta o sitio web no disponible
**Solución**:
```bash
# Ejecutar en modo headless (más rápido):
HEADLESS=true python run_tests.py
# Verificar acceso a https://demoblaze.com/
```

### ❌ Error: "Element not found"
**Causa**: El sitio web cambió su estructura
**Solución**:
1. Verificar que https://demoblaze.com/ esté accesible
2. Los localizadores están en `pages/*.py` si necesitas actualizarlos
3. Incrementar timeouts en `utils/driver_manager.py`

## 📋 DATOS DE PRUEBA UTILIZADOS
===============================

### 👤 Información del Cliente (Formulario):
```python
customer_data = {
    'name': 'Juan Pérez',           # Nombre completo válido
    'country': 'México',            # País de origen
    'city': 'Ciudad de México',     # Ciudad de envío
    'card': '4111111111111111',     # Tarjeta de prueba Visa válida
    'month': '12',                  # Mes de vencimiento
    'year': '2025'                  # Año de vencimiento
}
```

### 🛍️ Productos de Prueba:
- **Samsung Galaxy S6** - $360 (Categoría: Phones)
- **Nokia Lumia 1520** - $820 (Categoría: Phones)
- **Total esperado**: $1,180

### 🎯 Criterios de Validación:
- ✅ Productos se agregan correctamente al carrito
- ✅ Precios se calculan correctamente  
- ✅ Formulario acepta datos válidos
- ✅ Proceso de compra se completa exitosamente
- ✅ Mensajes de confirmación aparecen correctamente

## 🏆 MEJORES PRACTICAS IMPLEMENTADAS
====================================

### 🏗️ Arquitectura:
- **Page Object Model (POM)**: Separación clara de responsabilidades
- **Waits explícitos**: Esperas inteligentes para elementos dinámicos
- **Manejo de excepciones**: Try-catch en operaciones críticas
- **Configuración flexible**: Opciones headless y personalizables

### 🔄 Confiabilidad:
- **Múltiples estrategias de fallback**: Para máxima compatibilidad
- **Retry automático**: En operaciones que pueden fallar temporalmente
- **Validaciones robustas**: Verificación de estados antes de acciones
- **Limpieza automática**: Cierre correcto de recursos

### 📊 Reporting:
- **Reportes HTML detallados**: Con capturas y métricas
- **Logging granular**: Seguimiento paso a paso
- **Screenshots automáticos**: En caso de fallos para debugging
- **Métricas de rendimiento**: Tiempos de ejecución y estadísticas

## 📞 SOPORTE Y CONTACTO
=======================

### 🔍 Si encuentras problemas:

1. **Revisa esta documentación** - Sección "Solución de Problemas"
2. **Consulta el reporte HTML** - `reports/test_report.html`
3. **Verifica los logs de consola** - Salida detallada en terminal
4. **Prueba en modo headless** - Puede resolver problemas de GUI

### 📧 Para soporte adicional:
- Crear issue en el repositorio con:
  - Mensaje de error completo
  - Sistema operativo y versión
  - Versión de Python
  - Navegador y versión
  - Pasos para reproducir el problema

---

## 📅 INFORMACION DEL PROYECTO
=============================

- **Fecha de creación**: 25 de Septiembre, 2025
- **Última actualización**: 26 de Septiembre, 2025  
- **Versión**: 2.0 (Sistema simplificado)
- **Autor**: Alexander Morales
- **Propósito**: Prueba técnica E2E Automation
- **Sitio objetivo**: https://demoblaze.com/

### 🎯 Estado del Proyecto: ✅ COMPLETO Y LISTO PARA EVALUACION
