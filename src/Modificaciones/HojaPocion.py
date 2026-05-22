class HojaPocion(Decorator):
    def usar(self, personaje):
        print("La poción brilla intensamente...")
        self.em.usar(personaje)