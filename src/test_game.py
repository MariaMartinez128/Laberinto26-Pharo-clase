#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script for the game"""
import sys
from Builder.Director import Director
from Modificaciones.ConsolaInteractiva import ConsolaInteractiva

try:
    # Procesar el JSON del laberinto
    director = Director()
    director.procesar("laberinto.json")
    
    # Obtener el juego
    juego = director.obtener_juego()
    
    # Crear consola
    consola = ConsolaInteractiva(juego)
    
    print("✅ Game initialized successfully!")
    print(f"   Laberinto: {juego.laberinto}")
    print(f"   Bichos: {len(juego.bichos)}")
    print(f"   Habitaciones: {len(juego.laberinto.habitaciones)}")
    
    # Show all habitaciones
    for hab_num in sorted(juego.laberinto.habitaciones.keys()):
        hab = juego.laberinto.habitaciones[hab_num]
        print(f"   - {hab} ({len(hab.hijos)} items)")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
