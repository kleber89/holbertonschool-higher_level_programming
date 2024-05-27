#!/usr/bin/python3
def agregar_texto(nombre_archivo="", texto=""):
  """Agrega una cadena al final de un archivo de texto UTF-8 y devuelve el número de caracteres añadidos."""
  with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
      caracteres_añadidos = archivo.write(texto)
  return caracteres_añadidos
