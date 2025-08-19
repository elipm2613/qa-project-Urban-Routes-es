# 🚕 Urban Routes - Automatización de Pruebas de la Aplicación Web
**Kevin Elí Pérez Martínez Cohort 34 – Sprint 8 TripleTen QA Engineer Bootcamp**

Este proyecto automatiza una serie de pruebas funcionales sobre el sitio web de **Urban Routes**, una aplicación de solicitud de transporte. La automatización fue realizada utilizando **Selenium WebDriver** y **Pytest**.

## ¿Qué pruebas automatiza?

El proyecto realiza las siguientes pruebas de forma automática:

1. Configura una dirección de origen y destino.
2. Selecciona la tarifa "Comfort".
3. Ingresa un número de teléfono.
4. Ingresa el código SMS recibido.
5. Agrega una tarjeta de crédito.
6. Escribe un mensaje personalizado para el conductor.
7. Solicita manta y pañuelos.
8. Pide dos helados.
9. Confirma el viaje y espera a que aparezca la información del conductor.

---

## 🧩 Estructura del proyecto

```

qa-project-urban-routes-es/
│
├── data.py                  # Datos como URL base, número de teléfono, direcciones, etc.
├── main.py                  # Archivo principal con pruebas estructuradas en Pytest
└── README.md                # Archivo sobre información del proyecto

````

---

## ⚙️ Requisitos

- Python 3.9+
- Google Chrome instalado
- ChromeDriver (compatible con tu versión de Chrome)

---

## 📦 Instalación

**Clonar el repositorio**:

git clone https://github.com/tu-usuario/qa-project-urban-routes-es.git
cd qa-project-urban-routes-es
  


##  Cómo ejecutar las pruebas

Desde la terminal (dentro del proyecto):

bash pytest main.py


Desde PyCharm puedes hacer clic derecho sobre `main.py` y seleccionar **"Run 'pytest in main'"**.

---

## 🧪 Tecnologías y herramientas

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **WebDriverWait**

---