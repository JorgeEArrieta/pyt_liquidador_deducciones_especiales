class ExisteLegajo (Exception):
    
    def __init__(self):
        super().__init__(self)
        self.mensaje = 'Existe legajo'
        print(self.mensaje)


class ExisteRegistro (Exception):
    
    def __init__(self):
        super().__init__(self)
        self.mensaje = """Existe un registro en la tabla de deducción o remuneracion para el legajo seleccionado."""
        print(self.mensaje)


class ExisteFamiliar (Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'Ya existe un familiar, con el número de documento especificado, para el legajo.'
        print(self.mensaje)


class NoExisteLegajo (Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'No existe legajo'
        print(self.mensaje)


class LegajoInactivo (Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'La fecha de ingreso es posterior al periodo a liquidar'
        print(self.mensaje)


class LegajoInicial(Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'El legajo de inicio no puede ser menor al de finalización'
        print(self.mensaje)


class MesInicial(Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'El mes de inicio no puede ser menor al de finalización'
        print(self.mensaje)

class ErrorBruto(Exception):

    def __init__(self):
        super().__init__(self)
        self.mensaje = 'El bruto supera el importe permitido para el primer párrafo'