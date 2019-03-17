from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Article, Writer
from .forms import ArticleForm, WriterForm, ContactForm

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

def article_update(request, article_id, template_name='pdblog/forms.html'):
    article= get_object_or_404(Article, pk=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('pdblog:article_list')
    return render(request, template_name, {'form':form})

def article_delete(request, article_id, template_name='pdblog/forms.html'):
    article = get_object_or_404(Article, pk=article_id)
    if request.method=='POST':
        article.delete()
        return redirect('pdblog:article_list')
    return render(request, template_name, {'form':article})

def writer_create(request):
    # When a POST request
    if request.method == 'POST':
        form = WriterForm(request.POST or None)
        if form.is_valid():
            return HttpResponseRedirect('/index/')
    else:
        form = WriterForm()
    return render(request, 'pdblog/forms.html', {'form':form})

def contactformsend(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['pacemaking313@gmail.com']

        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/index/')
    else:
        form = ContactForm()
    return render(request, 'pdblog/contactform.html', {'form': form})
