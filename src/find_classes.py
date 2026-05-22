#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

# Diccionario de clases y sus módulos
CLASS_TO_MODULE = {
    'Forma': 'Solucion.Forma',
    'ElementoMapa': 'Solucion.ElementoMapa',
    'Contenedor': 'Solucion.Contenedor',
    'Ente': 'Solucion.Ente',
    'Modo': 'Solucion.Modo',
    'Bicho': 'Solucion.Bicho',
    'Personaje': 'Solucion.Personaje',
    'Hoja': 'Solucion.Hoja',
    'Decorator': 'Solucion.Decorator',
    'Puerta': 'Solucion.Puerta',
    'Pared': 'Solucion.Pared',
    'Comando': 'Solucion.Comando',
    'Abrir': 'Solucion.Comando',
}

def get_class_definitions(file_path):
    """Extract class names defined in a file"""
    classes = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            pattern = r'^class\s+(\w+)\s*[\(:]'
            matches = re.findall(pattern, content, re.MULTILINE)
            classes.update(matches)
    except:
        pass
    return classes

# Scan Solucion directory for class definitions
solucion_path = Path('Solucion')
for py_file in solucion_path.glob('*.py'):
    classes = get_class_definitions(str(py_file))
    module_name = f'Solucion.{py_file.stem}'
    for cls in classes:
        if cls not in CLASS_TO_MODULE:
            CLASS_TO_MODULE[cls] = module_name

print("Classes found:")
for cls, mod in sorted(CLASS_TO_MODULE.items()):
    print(f"  {cls}: {mod}")
