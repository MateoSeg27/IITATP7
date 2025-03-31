#Punto Nro 1º-
class Rectangulo():
    def __init__(self,altura_elegida,base_elegida):
        self.altura=altura_elegida
        self.base=base_elegida
    
    def sacar_area(self):
        self.area=self.base*self.altura
        print(self.area)

Rectangulo1=Rectangulo(4,2)
Rectangulo2=Rectangulo(10,5)
Rectangulo1.sacar_area()
Rectangulo2.sacar_area()

print("---------------------------------------------")

#Punto Nro 2º-
class Mate():
    def __init__(self,estado_elegido,cebadas_elegidas):
        self.cebadas_restantes=cebadas_elegidas
        self.estado=estado_elegido
        self.n=5
        
    def cebar(self):
        if self.cebadas_restantes>0:
            if self.estado=="lleno":
                print("¡Cuidado!¡Te quemaste!")
            else:
                print("El mate ahora esta lleno")
                self.estado="lleno"
                self.cebadas_restantes=self.cebadas_restantes-1
        else:
            if self.estado=="lleno":
                print("¡Cuidado!¡Te quemaste!")
            else:
                print("El mate ahora esta lleno")
                self.estado="lleno"
                self.n=0
            
    def beber(self):
        if self.cebadas_restantes>0:
            if self.estado=="vacio" or self.estado=="Vacio":
                print("El mate esta vacio")
            else:
                print("Ruidito de mate")
                self.estado="vacio"
        else:
            if self.estado=="vacio" or self.estado=="Vacio":
                print("El mate esta vacio")
            else:
                print("Advertencia: El mate esta lavado")
                self.estado="vacio"        

mate1=Mate("lleno",2)
mate1.cebar()
mate1.beber()
mate1.cebar()
mate1.beber()

print("---------------------------------------------")

#Punto Nro 3º-
class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega  # Guarda el nombre de la bodega del corcho

class Botella:
    def __init__(self, corcho: Corcho = None):
        self.corcho = corcho  # Puede tener un corcho o estar destapada

class Sacacorchos:
    def __init__(self):
        self.corcho = None  # Al inicio, el sacacorchos no tiene un corcho

    def destapar(self, botella: Botella):
        if botella.corcho is None:
            print("La botella ya está destapada.")  # Mensaje en lugar de excepción
            return
        if self.corcho is not None:
            print("El sacacorchos ya contiene un corcho.")  # Mensaje en lugar de excepción
            return

        # Extraer el corcho de la botella y guardarlo en el sacacorchos
        self.corcho = botella.corcho
        botella.corcho = None  # La botella ahora queda destapada
        print("Se ha destapado la botella correctamente.")

    def limpiar(self):
        if self.corcho is None:
            print("El sacacorchos no tiene un corcho para limpiar.")  # Mensaje en lugar de excepción
            return

        # Sacar el corcho del sacacorchos
        self.corcho = None
        print("El sacacorchos ha sido limpiado.")

corcho1 = Corcho("Bodega A")
botella1 = Botella(corcho1)
sacacorchos1 = Sacacorchos()

# Intentamos destapar la botella
sacacorchos1.destapar(botella1)
print(f"¿La botella tiene corcho? {botella1.corcho is not None}")  # False
print(f"¿El sacacorchos tiene corcho? {sacacorchos1.corcho is not None}")  # True

# Intentamos limpiar el sacacorchos
sacacorchos1.limpiar()
print(f"¿El sacacorchos tiene corcho? {sacacorchos1.corcho is not None}")  # False

# Intentamos destapar una botella ya destapada
sacacorchos1.destapar(botella1)

# Intentamos limpiar un sacacorchos que ya está vacío
sacacorchos1.limpiar()

print("---------------------------------------------")

#Punto Nro 4º-
class Restaurante():
    def __init__(self,restaurante_elegido, tipo_comida_elegida):
        self.nom_restaurante=restaurante_elegido
        self.tipo_comida=tipo_comida_elegida
    
    def describir_restaurante(self):
        print(self.nom_restaurante)
        print(self.tipo_comida)
    
    def abrir_restaurante(self):
        print("El restaurante esta Abierto")

class Heladeria(Restaurante):
    def __init__(self, restaurante_elegido, tipo_comida_elegida,sabores_elegidos):
        super().__init__(restaurante_elegido, tipo_comida_elegida)
        self.sabores=sabores_elegidos
        
    def mostrar_sabores(self):
        print(f"Los sabores disponibles en {self.nom_restaurante}")
        for sabor in self.sabores:
            print(f"-{sabor}")
mi_heladeria=Heladeria("Fili","Helados",["Chocolate","Cielo","Frutilla","Pistachio"])
mi_heladeria.describir_restaurante()
mi_heladeria.abrir_restaurante()
mi_heladeria.mostrar_sabores()