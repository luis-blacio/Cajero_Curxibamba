from django.db import models
from datetime import date

# Clase base Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        abstract = True

# Cliente hereda de Persona
class Cliente(Persona):
    email = models.EmailField(unique=True)

# Empleado hereda de Persona
class Empleado(Persona):
    salario = models.FloatField()
    turno = models.CharField(max_length=100)

# Cajero hereda de Empleado
class Cajero(Empleado):
    atiende = models.CharField(max_length=255)

# Farmacia
class Farmacia(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    horario_apertura = models.CharField(max_length=100)

# Sucursal
class Sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name="sucursales")

# Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    categoria = models.CharField(max_length=100)

# Inventario
class Inventario(models.Model):
    sucursal = models.OneToOneField(Sucursal, on_delete=models.CASCADE, related_name="inventario")
    producto = models.ManyToManyField(Producto, through="Stock")

# Modelo intermedio para relacionar Producto e Inventario
class Stock(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

# Transferencia
class Transferencia(models.Model):
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="transferencias_origen")
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="transferencias_destino")
    fecha = models.DateField(default=date.today)
    estado = models.CharField(max_length=50)

# Caja
class Caja(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="cajas")
    ventas_realizadas = models.IntegerField(default=0)

# Pago
class Pago(models.Model):
    monto = models.FloatField()
    fecha = models.DateField(default=date.today)
    tipo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

# Factura
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField(default=date.today)
    total = models.FloatField()
    detalles_productos = models.ManyToManyField(Producto, through="DetalleFactura")

# Modelo intermedio para relacionar Producto y Factura
class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.FloatField()


