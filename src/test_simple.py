#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script simple para probar el LaberintoBuilder sin usar unittest directamente
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Builder.Director import Director

def test_laberinto():
    print("\n" + "="*60)
    print("PRUEBA 1: Cargar Laberinto")
    print("="*60)
    
    director = Director()
    archivo = os.path.join(os.path.dirname(__file__), '..', 'laberinto.json')
    
    try:
        director.procesar(archivo)
        print("✅ JSON cargado correctamente")
    except Exception as e:
        print(f"❌ Error cargando JSON: {e}")
        return False
    
    # Test 2: Obtener juego
    print("\n" + "="*60)
    print("PRUEBA 2: Obtener Juego")
    print("="*60)
    
    try:
        juego = director.obtener_juego()
        assert juego is not None, "Juego es None"
        assert juego.laberinto is not None, "Laberinto es None"
        print("✅ Juego obtenido correctamente")
    except Exception as e:
        print(f"❌ Error obteniendo juego: {e}")
        return False
    
    # Test 3: Agregar personaje
    print("\n" + "="*60)
    print("PRUEBA 3: Agregar Personaje")
    print("="*60)
    
    try:
        juego.agregar_personaje("Maria")
        assert juego.person is not None, "Personaje es None"
        print(f"✅ Personaje creado: {juego.person}")
    except Exception as e:
        print(f"❌ Error creando personaje: {e}")
        return False
    
    # Test 4: Verificar habitaciones
    print("\n" + "="*60)
    print("PRUEBA 4: Verificar Habitaciones")
    print("="*60)
    
    try:
        for i in range(1, 7):
            hab = juego.obtener_habitacion(i)
            assert hab is not None, f"Habitación {i} es None"
            print(f"✅ Hab-{i} existe: {hab}")
    except Exception as e:
        print(f"❌ Error verificando habitaciones: {e}")
        return False
    
    # Test 5: Verificar bichos
    print("\n" + "="*60)
    print("PRUEBA 5: Verificar Bichos")
    print("="*60)
    
    try:
        assert len(juego.bichos) == 3, f"Esperaba 3 bichos, obtuve {len(juego.bichos)}"
        print(f"✅ Total de bichos: {len(juego.bichos)}")
        for bicho in juego.bichos:
            print(f"   • {bicho} en {bicho.posicion} - Vidas: {bicho.vidas}")
    except Exception as e:
        print(f"❌ Error verificando bichos: {e}")
        return False
    
    # Test 6: Pruebas de movimiento
    print("\n" + "="*60)
    print("PRUEBA 6: Movimiento entre habitaciones")
    print("="*60)
    
    try:
        from Solucion.Norte import Norte
        print(f"   Posición inicial: {juego.person.posicion}")
        
        # Intentar moverse al norte
        Norte.default().caminar(juego.person)
        print(f"   Posición después de norte: {juego.person.posicion}")
        print("✅ Movimiento funcionando")
    except Exception as e:
        print(f"❌ Error en movimiento: {e}")
        return False
    
    print("\n" + "="*60)
    print("✅ TODAS LAS PRUEBAS PASARON")
    print("="*60 + "\n")
    return True

if __name__ == "__main__":
    success = test_laberinto()
    sys.exit(0 if success else 1)
