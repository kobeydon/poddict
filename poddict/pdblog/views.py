from django.shortcuts import render, redirect, get_object_or_404
from pdblog.models import Article, Writer
from pdblog.forms import ArticleForm, WriterForm

def article_list(request, template_name='pdblog/list.html'):
    article = Article.objects.all()
    data = { 'objects_list' : article }
    return render(request, template_name, data)

def article_view(request, article_id, template_name='pdblog/detail.html'):
    target_article = get_object_or_404(Article, pk=article_id)
    data = { 'article_detail' : target_article }
    return render(request, template_name, data)

def article_create(request, template_name='pdblog/forms.html'):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('pdblog:article_list')
        except:
            pass
    else:
        form = ArticleForm()

    return render(request, template_name, {'form':form})
#
def article_update(request, article_id, template_name='pdblog/forms.html'):
    article= get_object_or_404(Article, pk=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('pdblog:article_list')
    return render(request, template_name, {'form':form})
#
#
# def blog_delete(request, pk, template_name='pdblog/forms.html'):
#     blog = get_object_or_404(Article, pk=pk)
#     if request.method=='POST':
#         blog.delete()
#         return redirect('blog_list')
#     return render(request, template_name, {'object':blog})
# # Create your views here.
