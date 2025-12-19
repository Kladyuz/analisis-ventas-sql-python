# Análisis de Ventas y ETL con Python y SQL

## 📌 Descripción del Proyecto
Este proyecto consiste en un flujo de trabajo de **Data Science** y **ETL (Extract, Transform, Load)** para analizar el rendimiento de ventas de una empresa automotriz ficticia (`classicmodels`). 

El objetivo principal fue conectar Python a una base de datos PostgreSQL, extraer múltiples tablas relacionales, procesar la información garantizando la integridad de los datos y generar reportes financieros automatizados.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.12
* **Análisis de Datos:** Pandas (Merge, GroupBy, Pivot Tables)
* **Base de Datos:** PostgreSQL
* **Conexión DB:** SQLAlchemy, Psycopg2
* **Metodología:** Principio DRY (Don't Repeat Yourself) mediante modularización de funciones.

## 🚀 Características del Código
1.  **Conexión a Base de Datos:** Extracción automatizada de tablas (`orders`, `products`, `customers`, etc.) usando `SQLAlchemy`.
2.  **Integridad Referencial:** Cruce de datos (Merges) validando relaciones `1:m` y `m:1` para asegurar la calidad de la información.
3.  **Feature Engineering:** Cálculo de KPIs clave como **Venta Total**, **Costo** y **Ganancia** neta.
4.  **Modularización (DRY):** Uso de un archivo externo `funciones.py` para encapsular la lógica de:
    * Filtrado por fechas.
    * Generación de reportes pivote.
    * Escritura y exportación a SQL.
5.  **Persistencia de Datos:** Los reportes finales (Top 10 Clientes y Productos) se exportan automáticamente como nuevas tablas en la base de datos PostgreSQL.

## 📂 Estructura del Repositorio
* `Prueba.ipynb`: Jupyter Notebook con el flujo de análisis paso a paso y la narrativa del negocio.
* `funciones.py`: Módulo de Python con funciones reutilizables para filtrar y conectar con la BD.
* `README.md`: Documentación del proyecto.

## 📊 Resultados Clave
Se generaron tablas en PostgreSQL con:
* **Top 10 Clientes (2005):** Ranking basado en ventas brutas.
* **Top 10 Productos (2005):** Artículos más vendidos y rentables del año.

---
*Este proyecto fue desarrollado como parte de una evaluación técnica de Data Science.*