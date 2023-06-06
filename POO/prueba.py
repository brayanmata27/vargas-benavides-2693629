class Empleado:
    # Variable de clase para contar la cantidad de objetos creados
    cantidad_empleados = 0

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.cantidad_empleados += 1

    # Getters y Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def calcular_salario_por_hora(self):
        horas_trabajo_diarias = 8  # Considerando una jornada laboral de 8 horas diarias
        dias_trabajo_semana = 5  # De lunes a viernes
        salario_por_hora = self.salario / (horas_trabajo_diarias * dias_trabajo_semana)
        return salario_por_hora

    def calcular_incremento_salario(self, ipc):
        salario_minimo = 1000  # Ejemplo de salario mínimo
        incremento = ipc

        if self.salario <= salario_minimo:
            incremento += 0.03

        incremento_total = self.salario * incremento
        return incremento_total

    def calcular_salario_con_horas_extras(self, horas_extras):
        horas_diarias_extras_max = 2
        dias_trabajo_semana = 5  # De lunes a viernes
        salario_hora_extra = self.calcular_salario_por_hora() * 1.5

        if horas_extras > (horas_diarias_extras_max * dias_trabajo_semana):
            return "Error: Las horas extras exceden el límite permitido."

        salario_total = self.salario + (horas_extras * salario_hora_extra)
        return salario_total


# Ejemplo de uso
empleado1 = Empleado("Juan Perez", "Analista", 2500)
print("Empleado 1 - Salario por hora:", empleado1.calcular_salario_por_hora())

empleado1.set_salario(3000)
print("Empleado 1 - Incremento de salario:", empleado1.calcular_incremento_salario(0.02))

print("Empleado 1 - Salario con horas extras:", empleado1.calcular_salario_con_horas_extras(5))

print("Cantidad de empleados:", Empleado.cantidad_empleados)
