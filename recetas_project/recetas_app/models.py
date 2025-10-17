from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    categoria = models.CharField(max_length=50, choices=[('Entrante', 'Entrante'),('Plato principal', 'Plato principal'),('Postre', 'Postre')])
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recetas")
    likes = models.ManyToManyField(User, related_name="recetas_liked", blank=True)
    imagen = models.ImageField(upload_to='recetas_imagenes/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
    def total_likes(self):
        return self.likes.count()
    
class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.usuario} en {self.receta}'
    
class Valoracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='valoraciones')
    valor = models.IntegerField(default=1)
    
    class Meta:
        unique_together = ('usuario', 'receta')
        
    def __str__(self):
        return f"{self.usuario.username} -> {self.receta.titulo}"
