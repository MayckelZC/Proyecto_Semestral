class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session 
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, figura):
        if str(figura.id) not in self.carro.keys():
            self.carro[figura.id] = {
                "figura_id": figura.id,
                "nombre": figura.nombreF,
                "precio": int(figura.precioF),
                "cantidad": 1,
                "imagen": figura.imagenF.url
        }
        else:
            for key, value in self.carro.items():
                if key == str(figura.id):
                    value["cantidad"] += 1
                    value["precio"] += figura.precioF
                    break  # Mover el break aquí, después de actualizar los valores
            self.guardar_carro()
    
   

    def eliminar(self, figura):
        figura.id = str(figura.id)
        if figura.id in self.carro:
            del self.carro[figura.id]
            self.guardar_carro()

    def restar(self, figura):
        for key, value in self.carro.items():
            if key==str(figura.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=value["precio"]-figura.precioF
                if value["cantidad"]<1:
                    self.eliminar(figura)
                break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True


    def importe_total_carro(self):
        total = 0
        for figura in self.carro.values():
            total += figura["precio"]
        return total
    
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
