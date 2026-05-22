#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Automated test of the game following the video script"""
import sys
from io import StringIO
from Builder.Director import Director
from Modificaciones.ConsolaInteractiva import ConsolaInteractiva

# Simulate user input
class FakeInput:
    def __init__(self, inputs):
        self.inputs = iter(inputs)
    
    def __call__(self, prompt=""):
        try:
            val = next(self.inputs)
            print(prompt + val)
            return val
        except StopIteration:
            return "salir"

# Setup game
director = Director()
director.procesar("laberinto.json")
juego = director.obtener_juego()
consola = ConsolaInteractiva(juego)

# Test sequence following the video script
test_inputs = [
    "Maria",        # Player name
    "norte",        # Move north to room 2
    "usar",         # Use cofre
    "este",         # Move east to room 5
    "este",         # Move east to room 6
    "salir"         # Exit game
]

# Replace input function
import builtins
original_input = builtins.input
builtins.input = FakeInput(test_inputs)

try:
    consola.loop()
    print("\n✅ Game test completed successfully!")
except Exception as e:
    print(f"\n❌ Error during test: {e}")
    import traceback
    traceback.print_exc()
finally:
    builtins.input = original_input
