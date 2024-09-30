# Atividade 1
Roteiro da atividade:
• Parte 1:
1. Criar um novo app chamado blog;
2. Fazer todos os passos para criar a url /blog, apontando para a index no
arquivo views.py;
3. Criar duas tabelas:
a. post: com os campos titulo (CharField), texto (TextField), e
pub_date (DateTimeField);
b. comentario: com os campos post_id (ForeignKey para a tabela
post), texto (CharField) e com_date (DateTimeField);
4. Popular essas duas tabelas com pelo menos 2 posts e 3 comentários e
cada post;
• Parte 2:
1. Acessa o Classroom da disciplina e buscar pela seguinte postagem:
2. 2. Baixar o arquivo e extrair em uma pasta separada;
3. O arquivo descompactado tem um arquivo blog-template.html e 4 outras
pastas;
4. Na sua aplicação (blog), você deve adicionar um template base com o
código blog-template.html;
5. Você deve adequar o código para que os arquivos estáticos que são
usados sejam utilizado dentro do seu app;
• Parte 3:
1. Na sua tabela ”post”, adicionar um campo imagem;
2. Na página index do seu app blog, você deve listar todas as postagens da
seguinte forma:
a. Imagem, nome da postagem e um botão para acessar o detalhe da
postagem;
3. Ao clicar no botão, o usuário deve ser direcionado para uma página que
será mostrado apenas o conteúdo da postagem selecionada;
4. Mostrar os comentários da postagem;
5. Você deve adicionar nessa página um formulário para inserção de
comentários;
6. Ao inserir um comentário, o usuário deve ser direcionado para a página
inicial e deve receber uma mensagem de sucesso;
