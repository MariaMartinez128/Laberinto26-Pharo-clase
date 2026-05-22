from Modificaciones.GestorAmbiental import GestorAmbiental
from Solucion.Norte import Norte
from Solucion.Sur import Sur
from Solucion.Este import Este
from Solucion.Oeste import Oeste


class ConsolaInteractiva:
    """Interfaz mejorada del juego con visualización de estado"""

    def __init__(self, juego):
        self.juego = juego
        self.turno = 0
        self.gestor = GestorAmbiental()

    def limpiar_pantalla(self):
        print("\n" * 2)

    def mostrar_titulo(self):
        print("════════════════════════════════════════════════════════════")
        print("█          🏰 LABERINTO 26 CON MODIFICACIONES 🏰          █")
        print("════════════════════════════════════════════════════════════\n")

    def mostrar_barra_estado(self):
        p = self.juego.person
        print(f"\n📋 ESTADO DEL JUEGO")
        print(f"   Heroe: {p.nombre:20} | Turno: {self.turno}")
        
        # Barra de vidas con emojis
        vidas_llenas = int(p.vidas / 5)
        print(f"   ❤️  Vidas: {'❤️ ' * vidas_llenas:<10} ({p.vidas}/50)")
        
        # Barra de poder
        poder_lleno = int(p.poder / 2)
        print(f"   ⚡ Poder: {'⚡' * poder_lleno:<10} ({p.poder}/10)")

    def mostrar_posicion(self):
        p = self.juego.person
        print(f"\n   📍 Posicion: {p.posicion}")

    def mostrar_mapa(self):
        print("\n┌─ MAPA DEL LABERINTO ─────────────────────────────────────┐")
        print("│                                                            │")
        print("│   ┌─────────┬─────────┬─────────┐                         │")
        print("│   │ Hab-1   │ Hab-2   │ Hab-3   │                         │")
        print("│   │   🕳️    │   📦    │   😨    │                         │")
        print("│   ├─────────┼─────────┼─────────┤                         │")
        print("│   │ Hab-4   │ Hab-5   │ Hab-6   │                         │")
        print("│   │   🔮    │   🌀    │   💣    │                         │")
        print("│   └─────────┴─────────┴─────────┘                         │")
        print("│                                                            │")
        print("│   Leyenda: 🕳️=Foso 📦=Cofre 😨=Bicho 🔮=Altar           │")
        print("│            🌀=Tunel 💣=Bomba  @=Tu posicion               │")
        print("└────────────────────────────────────────────────────────────┘")

    def mostrar_descripcion_habitacion(self):
        p = self.juego.person
        self.gestor.describir_habitacion(p.posicion.num)

    def mostrar_objetos_habitacion(self):
        p = self.juego.person
        if hasattr(p.posicion, 'hijos') and p.posicion.hijos:
            print("\n   📦 Objetos en esta habitacion:")
            for obj in p.posicion.hijos:
                print(f"      • {obj}")

    def mostrar_bichos_habitacion(self):
        p = self.juego.person
        bichos_aqui = [b for b in self.juego.bichos 
                       if b.posicion == p.posicion and b.esta_vivo()]
        
        if bichos_aqui:
            print("\n   👹 ENEMIGOS AQUI:")
            for bicho in bichos_aqui:
                print(f"      • {bicho} - Vidas: {bicho.vidas} - Poder: {bicho.poder}")

    def mostrar_estado(self):
        self.limpiar_pantalla()
        self.mostrar_titulo()
        self.mostrar_barra_estado()
        self.mostrar_posicion()
        self.mostrar_mapa()
        self.mostrar_descripcion_habitacion()
        self.mostrar_objetos_habitacion()
        self.mostrar_bichos_habitacion()

    def mostrar_ayuda(self):
        print("\n╔════════════════════════════════════════════════════════╗")
        print("║                   COMANDOS DISPONIBLES                 ║")
        print("╠════════════════════════════════════════════════════════╣")
        print("║ norte/sur/este/oeste → Moverte en esa direccion       ║")
        print("║ usar                 → Usar objeto en la habitacion   ║")
        print("║ abrir                → Abrir puertas                  ║")
        print("║ ayuda                → Mostrar este mensaje           ║")
        print("║ salir                → Terminar el juego             ║")
        print("╚════════════════════════════════════════════════════════╝")

    def mostrar_pantalla_final(self):
        p = self.juego.person
        print("\n\n")
        print("╔════════════════════════════════════════════════════════╗")
        print("║           🎬 FIN DE LA SIMULACION DEL JUEGO 🎬        ║")
        print("╠════════════════════════════════════════════════════════╣")
        print(f"║  Heroe: {p.nombre:45} ║")
        print(f"║  Turnos jugados: {self.turno:38} ║")
        print(f"║  Vidas restantes: {p.vidas}/50{' '*38} ║")
        print(f"║  Poder final: {p.poder}/10{' '*42} ║")
        print("╚════════════════════════════════════════════════════════╝\n")

    def manejar_comando(self, cmd):
        p = self.juego.person
        
        if cmd == "salir":
            self.mostrar_pantalla_final()
            return False

        elif cmd == "norte":
            print("\n➡️  Intentas moverte hacia el NORTE...")
            Norte.default().caminar(p)

        elif cmd == "sur":
            print("\n➡️  Intentas moverte hacia el SUR...")
            Sur.default().caminar(p)

        elif cmd == "este":
            print("\n➡️  Intentas moverte hacia el ESTE...")
            Este.default().caminar(p)

        elif cmd == "oeste":
            print("\n➡️  Intentas moverte hacia el OESTE...")
            Oeste.default().caminar(p)

        elif cmd == "usar":
            pos = p.posicion
            if hasattr(pos, "hijos") and pos.hijos:
                obj = pos.hijos[0]
                if hasattr(obj, "usar"):
                    print(f"\n🎯 Usas: {obj}")
                    obj.usar(p)
                else:
                    print("\n❌ No puedes usar esto")
            else:
                print("\n❌ No hay nada que usar aqui")

        elif cmd == "abrir":
            print("\n🚪 Abriendo puertas... (no implementado aun)")

        elif cmd == "ayuda":
            self.mostrar_ayuda()
            return True

        else:
            print(f"\n❌ Comando desconocido: '{cmd}'")
            print("   Escribe 'ayuda' para ver los comandos disponibles")
            return True

        return True

    def actuar_bichos(self):
        for b in self.juego.bichos:
            if b.esta_vivo():
                b.actua()

    def loop(self):
        # Pantalla inicial
        nombre = input("🎮 ¿Cual es el nombre de tu heroe? > ").strip()
        if not nombre:
            nombre = "Aventurero"
        
        self.juego.agregar_personaje(nombre)
        self.gestor.describir_entrada(nombre)
        
        while True:
            self.mostrar_estado()
            
            cmd = input("\n⚔️  Accion (norte/sur/este/oeste/usar/salir/ayuda): ").strip().lower()
            
            continuar = self.manejar_comando(cmd)
            if not continuar:
                break

            # Los bichos actuan
            self.actuar_bichos()
            
            self.turno += 1
            
            # Verificar si el personaje esta muerto
            if not self.juego.person.esta_vivo():
                print("\n💀 ¡HAS MUERTO!")
                self.mostrar_pantalla_final()
                break
