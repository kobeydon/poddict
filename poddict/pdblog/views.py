from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from pdblog.models import Article, Writer

class BlogForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pdblog_title', 'pdblog_text', 'pub_date']

def blog_list(request, template_name='pdblog/blog_list.html'):
    title = Article.objects.all()
    data = {}
    data['objects_list'] = title
    return render(request, template_name, data)

def blog_view(request, pk, template_name='pdblog/blog_detail.html'):
    blog = get_object_or_404(Article, pk=pk)
    return render(request, template_name, {'object':blog})

def blog_create(request, template_name='pdblog/blog_form.html'):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_update(request, pk, template_name='pdblog/blog_form.html'):
    blog= get_object_or_404(Article, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})


def blog_delete(request, pk, template_name='pdblog/blog_confirm_delete.html'):
    blog = get_object_or_404(Article, pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name, {'object':blog})
# Create your views here.
