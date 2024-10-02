from django.db import models

# Modelo para a tabela de Postagens
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='img/', blank=True, null=True)
    pub_date = models.DateTimeField()

# Modelo para a tabela de Comentários
class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=300)
    com_date = models.DateTimeField()
