

# 🧩 Laberinto26 - Juego de Laberinto en Python

## 📌 Descripción

Este proyecto se desarrolla en el marco de la asignatura *Diseño de Software* y tiene como objetivo la implementación de un sistema de laberinto en Python, en el que diferentes elementos interactúan entre sí siguiendo una arquitectura flexible y extensible.

El laberinto está formado por un conjunto de habitaciones conectadas mediante puertas y delimitadas por paredes, creando una estructura navegable que puede evolucionar con nuevas funcionalidades.

---

## 🎮 ¿En qué consiste el juego?

El jugador controla a un personaje que debe:

- Recorrer el laberinto
- Interactuar con objetos (cofres, altares, pociones…)
- Evitar o enfrentarse a enemigos
- Tomar decisiones por turnos
- Llegar a la última habitación

El juego se ejecuta por consola y cuenta con una interfaz visual mejorada.

---

## ▶️ Ejecución

Para ejecutar el juego en la consola: python main.py

Para ejecutar los test en la consola: python test_simple.py

---

## 🧠 Patrones de diseño utilizados

El proyecto utiliza múltiples patrones para mejorar la organización del código:

- **Factory Method**  
  Permite crear objetos sin saber su tipo hasta ejecutar el programa  

- **Decorator**  
  Añade funcionalidades sin modificar la clase original  

- **Strategy**  
  Permite cambiar el comportamiento en tiempo de ejecución  

- **Composite**  
  Trata igual objetos individuales y conjuntos  

- **Iterator**  
  Recorre colecciones sin mostrar su estructura interna  

- **Template**  
  Define pasos de un algoritmo modificables  

- **Abstract Factory**  
  Crea familias de objetos relacionados  

- **Singleton**  
  Garantiza una única instancia  

- **Builder**  
  Construye objetos complejos paso a paso  

- **Proxy**  
  Controla el acceso a otro objeto  

- **Adapter**  
  Hace compatibles interfaces distintas  

- **Bridge**  
  Separa abstracción e implementación  

- **Mediator**  
  Centraliza la comunicación entre objetos  

- **State**  
  Cambia el comportamiento según el estado  

- **Prototype**  
  Crea objetos copiando otros  

- **Observer**  
  Notifica cambios automáticamente  

- **Command**  
  Encapsula acciones como objetos  

---



---

## ⚙️ Modificaciones implementadas

Se han añadido mejoras importantes al sistema:

- Nuevos comportamientos de enemigos  
- Nuevos objetos (cofre, altar, pociones)  
- Uso de decoradores en elementos del juego  
- Sistema ambiental dinámico  
- Interfaz de usuario mejorada  

📄 Más información:  
MODIFICACIONES.md
[Ver modificaciones](MODIFICACIONES.md)

---

## 🎯 Funcionamiento del juego

El juego sigue un sistema por turnos:

1. El jugador realiza una acción  
2. Los enemigos actúan  
3. Se actualiza el estado  

📄 Guía completa:  
COMO_JUGAR.md
[Cómo jugar](COMO_JUGAR.md)

---

## 🗺️ Estructura del laberinto

El laberinto contiene:

- 6 habitaciones conectadas  
- Obstáculos (fosos)  
- Objetos (cofres, altar, pociones)  
- Enemigos con comportamientos distintos  

---

## 📊 Diagramas

El proyecto incluye diagramas de:

- Clases  
- Factory Method  
- Decorator  
- Strategy  
- Composite  
- Iterator  
- Template  
- Abstract Factory  
- Singleton  
- Builder  
- Proxy  
- Diagrama final  

📄 Explicación:  
EXPLICACION.md
[Explicación de diagramas](Diagramas/Diagramas_Patrones/EXPLICACION.md)

Las modiificaciones añadidas se encuentran en:

EXPLICACION.md [Ver explicación](Diagramas/Diagramas_Modificaciones/EXPLICACION.md)

---

## 📚 Documentación adicional

- MODIFICACIONES.md
[Ver modificaciones](MODIFICACIONES.md)

- COMO_JUGAR.md
[Cómo jugar](COMO_JUGAR.md)

- EXPLICACION.md  
[Explicación de patrones](Diagramas/Diagramas_Patrones/EXPLICACION.md)

[Explicación de modificaciones](Diagramas/Diagramas_Modificaciones/EXPLICACION.md)

---

## 👩‍💻 Autor

**María Martínez González**  
Grado en Ingeniería Informática  
Asignatura: Diseño de Software  

---

## 🧭 Diagrama de Clases
<img width="1316" height="718" alt="Diagrama de Clases (2)" src="https://github.com/user-attachments/assets/e75f558d-4323-44ae-a788-9f8421d8d190" />

## 🧭 Diagrama Factory Method
<img width="880" height="532" alt="image" src="https://github.com/user-attachments/assets/1566459e-0b60-4aa0-bbce-3424b25e28b2" />

## 🧭 Diagrama Decorator
<img width="842" height="429" alt="Decorator" src="https://github.com/user-attachments/assets/c2c52c8e-50fe-4a74-ad04-2c952518792c" />

## 🧭 Diagrama Strategy
<img width="840" height="564" alt="Strategy" src="https://github.com/user-attachments/assets/3d38482b-ddea-4911-8083-3eb195e76662" />

## 🧭 Diagrama Composite
<img width="1379" height="674" alt="image" src="https://github.com/user-attachments/assets/a76a9412-c592-4f7f-af9d-365cc1085dd4" />

## 🧭 Diagrama Iterator
<img width="1038" height="663" alt="image" src="https://github.com/user-attachments/assets/3ab8ba42-0526-4061-b500-53cf6a8ba675" />

## 🧭 Diagrama Template
<img width="1144" height="625" alt="image" src="https://github.com/user-attachments/assets/d3af076b-ba4a-492c-bdf1-f3f937db07b6" />

## 🧭 Diagrama Abstract Factory
<img width="1060" height="686" alt="image" src="https://github.com/user-attachments/assets/db1f9f35-109d-47c8-9ee2-2e2b842f9d07" />

## 🧭 Diagrama Singleton
<img width="1174" height="732" alt="image" src="https://github.com/user-attachments/assets/b77bf321-d2d1-4d3d-93a7-4598f949d07b" />

## 🧭 Diagrama Builder
<img width="1154" height="735" alt="image" src="https://github.com/user-attachments/assets/3bd06d7f-7893-49e8-a0bb-e416cd0542c6" />

## 🧭 Diagrama Proxy
<img width="1361" height="825" alt="Proxy" src="https://github.com/user-attachments/assets/0d3d73f0-9235-4d59-b0e5-89aa64b47583" />

## 🧭 Diagrama Final
<img width="1088" height="796" alt="Captura de pantalla 2026-03-25 200743" src="https://github.com/user-attachments/assets/3cbb1b58-59c3-4996-9905-ac226aee10f4" />

