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
Proporciona una interfaz por consola para interactuar con el sistema y probar funcionalidades.

<img width="707" height="471" alt="Comandos" src="https://github.com/user-attachments/assets/814f3467-ab69-4708-8365-2b3fa6e7d856" />
