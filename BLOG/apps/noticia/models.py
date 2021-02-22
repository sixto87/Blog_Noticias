from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, null=False, blank=False )
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add= True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural= 'Categoría'

        def __str__(self):
            return self.Nombre
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Autor', max_length = 255, null= False, blank= False)
    apellido = models.CharField('Apellido de Autor', max_length = 255, null= False, blank= False)
    correo = models.EmailField('Correo Electronico', blank= False, null=False)
    estado = models.BooleanField('Auto Activo/No Activo', default = True)
    fecha_creacion = models. DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name ='Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellido, self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo',max_length= 90, blank=False, null= False)
    slug = models.CharField('Slug',max_length= 90, blank=False, null= False)
    descripcion= models.CharField('Descripcion', max_length = 110, blank= False, null = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length= 255, blank= False, null=False)
    autor= models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __srt__(self):
        return self.titulo

# Create your models here.
