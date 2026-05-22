#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script para arreglar imports en archivos de Solucion"""
import os
from pathlib import Path

# Define imports needed for each file
IMPORTS_NEEDED = {
    'Personaje.py': 'from Solucion.Ente import Ente',
    'Bicho.py': 'from Solucion.Ente import Ente',
    'Hoja.py': 'from Solucion.ElementoMapa import ElementoMapa',
    'Pared.py': 'from Solucion.Hoja import Hoja',
    'Puerta.py': 'from Solucion.Hoja import Hoja',
    'Tunel.py': 'from Solucion.Hoja import Hoja',
    'Bomba.py': 'from Solucion.Hoja import Hoja',
    'Armario.py': 'from Solucion.Contenedor import Contenedor',
    'Comando.py': '',  # base class
    'Abrir.py': 'from Solucion.Comando import Comando',
    'Agresivo.py': 'from Solucion.Modo import Modo',
    'Perezoso.py': 'from Solucion.Modo import Modo',
    'Orientacion.py': '',
    'Norte.py': 'from Solucion.Orientacion import Orientacion',
    'Sur.py': 'from Solucion.Orientacion import Orientacion',
    'Este.py': 'from Solucion.Orientacion import Orientacion',
    'Oeste.py': 'from Solucion.Orientacion import Orientacion',
    'Noreste.py': 'from Solucion.Orientacion import Orientacion',
    'Noroeste.py': 'from Solucion.Orientacion import Orientacion',
    'Sureste.py': 'from Solucion.Orientacion import Orientacion',
    'Suroeste.py': 'from Solucion.Orientacion import Orientacion',
}

solucion_path = Path('Solucion')

for filename, import_line in IMPORTS_NEEDED.items():
    filepath = solucion_path / filename
    if not filepath.exists():
        print(f"Skipping {filename} - not found")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if import already exists or if file starts with class
        if import_line and import_line not in content and not content.strip().startswith('#'):
            # Add import at the beginning
            lines = content.split('\n')
            insert_after = 0
            
            # Skip encoding line if present
            if lines[0].startswith('#'):
                insert_after = 1
            
            new_lines = lines[:insert_after] + [import_line, ''] + lines[insert_after:]
            new_content = '\n'.join(new_lines)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")
        else:
            print(f"Skipped {filename} - already has imports or is base")
    except Exception as e:
        print(f"Error fixing {filename}: {e}")

print("Done!")
