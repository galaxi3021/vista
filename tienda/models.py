from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

class Producto(models.Model):
    """Model definition for Producto."""

    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True)
    precio= models.DecimalField(max_digits=5 ,decimal_places=2)


    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return u'/tienda/%d' % self.id 

class Factura(models.Model):
    """Model definition for factura."""

    nombre= models.CharField(max_length=40)
    nit= models.CharField('C/F',max_length=13)
    direccion= models.CharField('Ciudad', max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def update_total(self):
        total = 0
        producto = self.detalle_set.all()
        for prod in producto:
            total += prod.subtotal
        self.total = total
        self.save()


    class Meta:
        """Meta definition for factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return str(self.id)

class Detalle(models.Model):
    """Model definition for Detalle."""

    producto = models.ForeignKey(Producto,on_delete= models.PROTECT)
    factura = models.ForeignKey(Factura,on_delete= models.PROTECT)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


    class Meta:
        """Meta definition for Detalle."""

        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        return str(self.id)


def detalle_pre_save_receiver(sender, instance, *args, **kwargs):
    """Pre saves the price and subtotal of orders."""
    cant = instance.cantidad
    if cant >= 1:
        precio = instance.producto.precio
        subtotal = cant * precio
        instance.precio = precio
        instance.subtotal = subtotal


pre_save.connect(detalle_pre_save_receiver, sender=Detalle)

def detalle_post_save_receiver(sender, instance, *args, **kwargs):
    """Calls update_total def from Order Model"""
    instance.factura.update_total()

post_save.connect(detalle_post_save_receiver, sender=Detalle)

post_delete.connect(detalle_post_save_receiver, sender=Detalle)
