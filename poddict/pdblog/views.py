from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from pdblog.models import Article, Writer

# class BlogForm(ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title', 'text']

def article_list(request, template_name='pdblog/list.html'):
    article = Article.objects.all()
    data = { 'objects_list' : article }
    return render(request, template_name, data)

def article_view(request, article_id, template_name='pdblog/detail.html'):
    blog = get_object_or_404(Article, pk=article_id)
    return render(request, template_name, {'objects':blog})

# def blog_create(request, template_name='pdblog/forms.html'):
#     form = BlogForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('blog_list')
#     return render(request, template_name, {'form':form})
#
# def blog_update(request, pk, template_name='pdblog/forms.html'):
#     blog= get_object_or_404(Article, pk=pk)
#     form = BlogForm(request.POST or None, instance=blog)
#     if form.is_valid():
#         form.save()
#         return redirect('blog_list')
#     return render(request, template_name, {'form':form})
#
#
# def blog_delete(request, pk, template_name='pdblog/forms.html'):
#     blog = get_object_or_404(Article, pk=pk)
#     if request.method=='POST':
#         blog.delete()
#         return redirect('blog_list')
#     return render(request, template_name, {'object':blog})
# # Create your views here.
