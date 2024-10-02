from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comentario

# Função para exibir a lista de posts
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

# Função para exibir os detalhes de um post específico
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentario = Comentario.objects.all()
    return render(request, 'post_detail.html', {'post': post, 'comentario': comentario})

# Função para adicionar um comentário a um post
def comentarios(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        texto = request.POST.get('texto')
        comentario = Comentario(post_id=post, texto=texto, com_date=timezone.now())
        comentario.save()
        return redirect('index')  
    return redirect('post_detail', post_id=post_id)
