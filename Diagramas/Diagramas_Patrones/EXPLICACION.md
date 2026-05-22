EXPLICACION DE LOS DIAGRAMAS DE PATRONES

En esta carpeta se incluyen los diagramas UML que representan
los diferentes patrones de diseño utilizados en el proyecto.

A continuación se explica brevemente en qué consiste cada uno.

----------------------------------------
DIAGRAMA DE CLASES
----------------------------------------
Representa la estructura general del sistema:
- Clases principales
- Atributos y métodos
- Relaciones entre clases (herencia, asociación, composición)

Sirve para entender cómo está organizado el proyecto.

----------------------------------------
FACTORY METHOD
----------------------------------------
Este patrón permite crear objetos sin especificar exactamente
qué clase concreta se va a instanciar.

Se define un método de creación en una clase, pero son las subclases
las que deciden qué objeto se crea realmente.

----------------------------------------
DECORATOR
----------------------------------------
Permite añadir funcionalidades a un objeto de forma dinámica
sin modificar su estructura original.

Se utiliza envolviendo el objeto con otros objetos (decoradores)
que amplían su comportamiento.

----------------------------------------
STRATEGY
----------------------------------------
Permite definir diferentes comportamientos e intercambiarlos
en tiempo de ejecución.

En el juego se usa para los distintos modos de los bichos
(asustado, frenético, etc.).

----------------------------------------
COMPOSITE
----------------------------------------
Permite tratar objetos individuales y grupos de objetos
de la misma forma.

Se utiliza cuando una estructura está formada por partes
que pueden ser tratadas igual que el conjunto completo.

----------------------------------------
ITERATOR
----------------------------------------
Permite recorrer elementos de una colección sin mostrar
su representación interna.

Facilita el acceso a los elementos de forma ordenada.

----------------------------------------
TEMPLATE METHOD
----------------------------------------
Define la estructura de un algoritmo en una clase base,
dejando algunos pasos a las subclases.

Permite reutilizar el comportamiento común.

----------------------------------------
ABSTRACT FACTORY
----------------------------------------
Permite crear familias de objetos relacionados sin especificar
sus clases concretas.

Es útil cuando se necesitan distintos tipos de objetos
que deben funcionar juntos.

----------------------------------------
SINGLETON
----------------------------------------
Garantiza que una clase tenga una única instancia
y proporciona un punto de acceso global a ella.

----------------------------------------
BUILDER
----------------------------------------
Permite construir objetos complejos paso a paso.

Separa la construcción de un objeto de su representación final.

----------------------------------------
PROXY
----------------------------------------
Actúa como un intermediario que controla el acceso a otro objeto.

Puede añadir control, seguridad o retrasar la creación del objeto real.

----------------------------------------
DIAGRAMA FINAL
----------------------------------------
Representa la integración de todos los patrones en el sistema completo.

Permite ver cómo interactúan entre sí todos los elementos del proyecto
y cómo se conectan las distintas partes del laberinto.

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
