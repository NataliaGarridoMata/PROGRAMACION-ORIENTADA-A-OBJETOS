# 📂 Manejo de Archivos en Python
Natalia Yamile Garrido Mata 

Este proyecto muestra un ejemplo básico del manejo de archivos en Python utilizando las funciones `open()`, `write()` y `close()`.

El programa crea un archivo de texto, escribe contenido dentro de él y posteriormente lo cierra correctamente.

---

# 📚 Objetivo

El objetivo principal es aprender cómo trabajar con archivos en Python, permitiendo:

- Crear archivos
- Escribir información
- Guardar cambios
- Cerrar archivos correctamente



Este ejemplo representa una introducción básica al trabajo con archivos de texto en Python.
---

# 📄 Código del Programa

```python
archivo = open("test.txt", "w", encoding="utf-8")

archivo.write("hola mundo")

archivo.close()

