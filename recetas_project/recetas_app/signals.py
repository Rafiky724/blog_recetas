from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Receta

@receiver(pre_save, sender=Receta)
def borrar_imagen_anterior(sender, instance, **kwargs):
    try:
        receta_antigua = Receta.objects.get(pk=instance.pk)
        if receta_antigua.imagen and receta_antigua.imagen != instance.imagen:
            receta_antigua.imagen.delete(save=False)
    except Receta.DoesNotExist:
        pass
