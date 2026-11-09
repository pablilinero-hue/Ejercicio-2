#Ejercicio 2 - Trabajo Práctico Final

import json


# PUNTO A: DOMINIO DEL CATÁLOGO

# Excepción personalizada
class StockInvalidoError(Exception):
    """Error producido cuando se intenta asignar un stock negativo."""
    pass


# Clase base
class DispositivoEcológico:

    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self._stock = 0

        # Validación del stock inicial
        self.stock = stock

    # Encapsulamiento explícito mediante propiedad
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise StockInvalidoError(
                "El stock debe ser un número entero."
            )

        if cantidad < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self._stock = cantidad

    # Ficha técnica comercial
    def ficha_tecnica(self):
        return {
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": "Dispositivo ecológico"
        }


# Clase especializada que hereda de DispositivoEcológico
class PanelSolar(DispositivoEcológico):

    def __init__(
        self, nombre, marca, precio, stock,
        potencia_watts, eficiencia
    ):
        super().__init__(nombre, marca, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    # Polimorfismo: redefine la ficha técnica
    def ficha_tecnica(self):
        ficha = super().ficha_tecnica()

        ficha.update({
            "tipo": "Panel solar",
            "potencia_watts": self.potencia_watts,
            "eficiencia": self.eficiencia
        })

        return ficha



# PUNTO B: PERSISTENCIA DEL INVENTARIO

class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):

        # Convertir los objetos en diccionarios
        catalogo = [
            dispositivo.ficha_tecnica()
            for dispositivo in lista_dispositivos
        ]

        # Guardar los datos en formato JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado exitosamente en: {ruta_archivo}")


# BLOQUE DE PRUEBA

if __name__ == "__main__":

    print("===== ECOTECH SOLUTIONS =====")

    # Crear productos válidos
    panel1 = PanelSolar(
        "Panel Solar Eco 400",
        "EcoPower",
        250000,
        15,
        400,
        "21%"
    )

    panel2 = PanelSolar(
        "Panel Solar Eco 550",
        "GreenTech",
        320000,
        10,
        550,
        "23%"
    )

    # Verificar captura de excepción personalizada
    print("\n--- Prueba de validación de stock ---")

    try:
        panel1.stock = -5

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")

    # Mostrar fichas técnicas
    print("\n--- Catálogo de productos ---")

    for dispositivo in [panel1, panel2]:
        print(dispositivo.ficha_tecnica())

    # Exportar productos válidos
    print("\n--- Exportación del catálogo ---")

    productos_validos = [panel1, panel2]

    GestorInventario.guardar_catalogo_json(
        productos_validos,
        "catalogo_ecotech.json"
    )

