#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove all  from all Python files recursively"""
from pathlib import Path

# Scan all directories for Python files
for py_file in Path('.').rglob('*.py'):
    try:
        with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Remove all occurrences of 
        if '' in content:
            new_content = content.replace('', '')
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {py_file.name}")
    except Exception as e:
        pass

print("Done!")
