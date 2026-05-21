# Laberinto26-Pharo-clase

## 📌 Descripción

Este proyecto se desarrolla en el marco de la asignatura *Diseño de Software* y tiene como objetivo la implementación de un sistema de laberinto en Python, en el que diferentes elementos interactúan entre sí siguiendo una arquitectura flexible y extensible.

El laberinto está formado por un conjunto de habitaciones conectadas mediante puertas y delimitadas por paredes, creando una estructura navegable que puede evolucionar con nuevas funcionalidades.

A lo largo del desarrollo, se aplican diversos patrones de diseño con el fin de mejorar la organización, reutilización y mantenibilidad del código. Estos son los siguientes:

- **Factory Method**, Permite crear objetos sin saber exactamente qué tipo se va a crear hasta que el programa se ejecuta.
- **Decorator**, Añade funcionalidades a un objeto sin cambiar su clase.
- **Strategy**, Permite cambiar el comportamiento de un objeto en tiempo de ejecución.
- **Composite**, Permite tratar objetos individuales y grupos de objetos de la misma forma.
- **Iterator**, Permite recorrer elementos de una colección sin mostrar cómo están guardados.
- **Template**, Define los pasos de un algoritmo dejando que algunos se puedan modificar.
- **Abstract Factory**, Permite crear familias de objetos relacionados sin especificar sus clases concretas.
- **Singleton**, Garantiza que solo exista una única instancia de una clase.
- **Builder**, Permite construir objetos complejos paso a paso.
- **Proxy**, Controla el acceso a otro objeto.
- **Adapter**, Permite que clases con interfaces diferentes puedan trabajar juntas.
- **Bridge**, Separa una abstracción de su implementación para que puedan cambiar independientemente.
- **Mediator**, Centraliza la comunicación entre varios objetos para reducir dependencias.
- **State**, Permite que un objeto cambie su comportamiento según su estado.
- **Prototype**, Permite crear objetos copiando otros existentes.
- **Observer**, Notifica automáticamente a varios objetos cuando uno cambia.
- **Command**, Encapsula una acción como un objeto para poder ejecutarla o deshacerla.

Además, el sistema incorpora elementos especiales que enriquecen la interacción dentro del laberinto, como:
- Paredes con comportamientos especiales (por ejemplo, bomba broma).
- Enemigos u obstáculos que afectan al avance del usuario.

Este enfoque permite construir un modelo modular en el que es sencillo añadir nuevas características sin modificar el núcleo del sistema.

En la nueva versión del juego se han implementado modificaciones las cuales han añadido nuevas funcionalidades al sistema del laberinto para enriquecer el comportamiento y la interacción. A continuación se describen brevemente:

ModoAsustado.py
Define un estado en el que el bicho tiene miedo y no ataca, solo realiza acciones pasivas.
<img width="292" height="371" alt="ModoAsustado" src="https://github.com/user-attachments/assets/a6cfd611-e644-4739-8c0d-ec82169eee52" />

ModoFrenetico.py
Define un estado en el que el bicho está agresivo y ataca constantemente.
<img width="278" height="384" alt="ModoFrenetico" src="https://github.com/user-attachments/assets/8ac9f06e-0e18-4b62-837e-a60dae3238d4" />

BichoMutable.py
Bicho especial que puede cambiar de comportamiento (modo) durante la ejecución del juego.
<img width="289" height="264" alt="BichoMutable" src="https://github.com/user-attachments/assets/4802b2c6-d221-42cc-a9a1-99a19582ffc2" />

Cofre.py
Contenedor que almacena objetos como pociones que el jugador puede recoger.
<img width="248" height="221" alt="Cofre" src="https://github.com/user-attachments/assets/f0d7fafc-5de3-40de-83d5-fe1f7fa1cb00" />

Altar.py
Contenedor especial que permite interactuar con elementos más importantes o mágicos.
<img width="278" height="223" alt="Altar" src="https://github.com/user-attachments/assets/a32f40bc-76ae-4c48-8a62-bb9f47d50c24" />

PocionesConcretas.py
Define distintos tipos de pociones (curación, fuerza, etc.) con efectos diferentes.
EfectoPocion.py
Gestiona la aplicación de los efectos de las pociones sobre el jugador.
<img width="278" height="223" alt="Altar" src="https://github.com/user-attachments/assets/a32f40bc-76ae-4c48-8a62-bb9f47d50c24" />

HojaEspejo.py
Decorador que añade propiedades especiales a un espejo dentro del laberinto.
HojaFoso.py
Decorador que convierte un foso en un elemento con efectos adicionales (daño, obstáculo, etc.).
HojaPocion.py
Decorador que añade propiedades extra a las pociones (raras, especiales, etc.).
<img width="376" height="308" alt="Hojas" src="https://github.com/user-attachments/assets/2990ede7-3b95-482c-8d34-b200fbb365c9" />

GestorAmbiental.py
Gestiona el entorno del laberinto, incluyendo condiciones y efectos ambientales dinámicos.
<img width="265" height="249" alt="GestorAmbiental" src="https://github.com/user-attachments/assets/31912665-3868-4beb-b56e-729d11c2cadb" />

ConsolaInteractiva.py
Proporciona una interfaz por consola para interactuar con el sistema y probar funcionalidades
<img width="707" height="471" alt="Comandos" src="https://github.com/user-attachments/assets/814f3467-ab69-4708-8365-2b3fa6e7d856" />

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

