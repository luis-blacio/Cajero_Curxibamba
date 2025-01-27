from django.contrib import admin
from .models import (
    Cliente, Empleado, Cajero, Farmacia, Sucursal, Producto, Inventario, Stock,
    Transferencia, Caja, Pago, Factura, DetalleFactura
)

# Configuraciones para visualizar relaciones intermedias en el admin
class StockInline(admin.TabularInline):
    model = Stock
    extra = 1

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    extra = 1

# Modelos registrados en el admin
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'salario', 'turno')
    search_fields = ('nombre', 'turno')

@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'turno', 'atiende')
    search_fields = ('nombre', 'atiende')

@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'horario_apertura')
    search_fields = ('nombre', 'direccion')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'farmacia')
    search_fields = ('nombre', 'direccion', 'telefono')
    list_filter = ('farmacia',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    search_fields = ('nombre', 'categoria')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal',)
    inlines = [StockInline]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('inventario', 'producto', 'cantidad')
    list_filter = ('inventario__sucursal', 'producto')

@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('sucursal_origen', 'sucursal_destino', 'fecha', 'estado')
    list_filter = ('estado', 'fecha')

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'ventas_realizadas')
    list_filter = ('sucursal',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('monto', 'fecha', 'tipo_pago', 'estado')
    list_filter = ('tipo_pago', 'estado', 'fecha')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'sucursal', 'fecha', 'total')
    list_filter = ('sucursal', 'fecha')
    search_fields = ('cliente__nombre', 'sucursal__nombre')
    inlines = [DetalleFacturaInline]

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio')

# Register your models here.
