# Python Web Scraping and Email Automation Projects

Este repositorio contiene dos scripts en Python que realizan tareas de scraping y automatización de correos electrónicos. A continuación se describen los dos scripts incluidos y sus funcionalidades.

## Scripts

### 1. Job Postings Scraper & Email Sender

Este script obtiene ofertas de trabajo desde la API de Remote OK, guarda los datos en un archivo Excel y envía el archivo por correo electrónico.

#### Funcionalidades

- **Obtener Ofertas de Trabajo:** Realiza una solicitud HTTP a la API de Remote OK para obtener ofertas de trabajo en formato JSON.
- **Guardar en Excel:** Escribe los datos de las ofertas en un archivo Excel (`remote_jobs.xls`) utilizando `xlwt`.
- **Enviar Correo Electrónico:** Envía un correo electrónico con el archivo Excel adjunto, utilizando `smtplib` para conectarse a un servidor SMTP.

#### Uso

1. Asegúrate de tener las siguientes dependencias instaladas:
pip install requests xlwt
Ejecuta el script:
python job_postings_email.py
El script enviará un correo con el archivo remote_jobs.xls adjunto.

2. Amazon Product Scraper
Este script realiza scraping en Amazon para obtener información de productos como el precio, el título, la calificación y los detalles técnicos. Los datos se guardan en un archivo CSV.

**Funcionalidades**

Scraping de Productos: Extrae el precio, título, calificación y detalles técnicos de productos de Amazon.
Soporte Multihilo: Utiliza un ThreadPoolExecutor para realizar scraping de múltiples URLs simultáneamente, acelerando el proceso.
Guardar en CSV: Los datos obtenidos se guardan en un archivo CSV con un nombre basado en la fecha actual.
Uso
Instala las dependencias necesarias:


pip install requests beautifulsoup4 lxml tqdm

Asegúrate de tener un archivo amazon_products_url.csv con las URLs de los productos de Amazon que quieres analizar.

Ejecuta el script:
python amazon_scraper.py
El script generará un archivo CSV con la información de los productos.

**Requisitos**
Python 3.7+
Conexión a Internet
Acceso a un servidor SMTP para enviar correos (por ejemplo, Gmail)

**Notas**
El script de Amazon scraping puede requerir ajustes dependiendo de la estructura del HTML en las páginas de productos de Amazon.
Para enviar correos electrónicos, asegúrate de habilitar el acceso a aplicaciones poco seguras en tu cuenta de Gmail o utiliza un servidor SMTP alternativo.
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una sugerencia, no dudes en abrir un issue o un pull request.

Este archivo README proporciona una descripción completa de ambos scripts, cómo configurarlos y ejecutarlos