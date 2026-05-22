#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove trailing backticks from Python files"""
from pathlib import Path
import re

solucion_path = Path('Solucion')

for py_file in solucion_path.glob('*.py'):
    try:
        with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Remove trailing backticks
        if content.rstrip().endswith(''):
            new_content = re.sub(r'\s*$', '', content.rstrip()) + '\n'
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {py_file.name}")
    except Exception as e:
        print(f"Error with {py_file.name}: {e}")

print("Done!")
