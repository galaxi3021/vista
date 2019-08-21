from django.contrib import admin

from .models import Producto,Factura,Detalle

admin.site.register(Producto)
# admin.site.register(Factura)
# admin.site.register(Detalle)

class DetalleInline(admin.TabularInline):
    '''Tabular Inline View for Detalle'''

    model = Detalle
    extra = 1

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    '''Admin View for Factura'''

    list_display = ('nombre','nit','direccion','fecha','total',)
    # list_filter = ('',)
    inlines = [
        DetalleInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


# @admin.register(Invoice)
# class InvoiceAdmin(admin.ModelAdmin):
#     '''Admin View for Invoice'''

#     list_display = ('invoice_number','customer', 'order','date','total', 'payment')
#     ordering = ('invoice_number','date',)
