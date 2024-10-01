from django.db import models

# Create your models here.
class Post(models.Model):
    
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='post_imagens/')
    pub_date = models.DateTimeField()
    
class Comentario(models.Model):
    
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=300)
    com_date = models.DateTimeField()
    