#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove all backticks from Python files"""
from pathlib import Path

solucion_path = Path('Solucion')

for py_file in solucion_path.glob('*.py'):
    try:
        with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Remove all occurrences of 
        new_content = content.replace('', '')
        
        if new_content != content:
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {py_file.name}")
    except Exception as e:
        print(f"Error with {py_file.name}: {e}")

print("Done!")
