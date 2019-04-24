from django.shortcuts import render, redirect, resolve_url, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .models import Article
from register.models import User
from .forms import ArticleForm, ContactForm
try:
    from django.utils import simplejson as json
except ImportError:
    import json


class ArticleList(ListView):
    model = Article
    template_name = 'pdblog/list.html'

# funstion view as reference
# def article_list(request, template_name='pdblog/list.html'):
#     article = Article.objects.all()
#     data = { 'objects_list' : article }
#     return render(request, template_name, data)

def article_view(request, article_id, template_name='pdblog/detail.html'):

    target_article = get_object_or_404(Article, pk=article_id)
    data = { 'article_detail' : target_article }
    return render(request, template_name, data)

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'pdblog/forms.html'


    def get_success_url(self):
        return reverse_lazy('pdblog:article_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# @login_required
# def article_create(request, template_name='pdblog/forms.html'):
#     form = ArticleForm(request.POST or None)
#     if form.is_valid():
#         try:
#             form.instance.user = request.user
#             form.save()
#             return redirect('pdblog:article_list')
#         except:
#             pass
#     else:
#         form = ArticleForm()
#
#     return render(request, template_name, {'form':form})

class OnlyYourBlogMixin():

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Article, pk=self.kwargs['pk'])
        if obj.user != self.request.user:
            raise Http404("You are not allowed to edit this blog")
        return super().dispatch(request, *args, **kwargs)

class ArticleUpdate(LoginRequiredMixin, OnlyYourBlogMixin, UpdateView):
    model = Article
    template_name = 'pdblog/forms.html'
    form_class = ArticleForm

    def get_success_url(self):
        return resolve_url('pdblog:article_view', self.kwargs['pk'])

# '''function base view for reference'''
# def article_update(request, article_id, template_name='pdblog/forms.html'):
#     article= get_object_or_404(Article, pk=article_id)
#     form = ArticleForm(request.POST or None, instance=article)
#     if form.is_valid():
#         form.instance.user = request.user
#         form.save()
#         return redirect('pdblog:article_list')
#     return render(request, template_name, {'form':form})

class ArticleDelete(LoginRequiredMixin, OnlyYourBlogMixin, DeleteView):

    model = Article
    success_url = reverse_lazy('pdblog:article_list')

# function base view for reference
# @login_required
# def article_delete(request, article_id, template_name='pdblog/delete.html'):
#     article = get_object_or_404(Article, pk=article_id)
#     if request.method=='POST':
#         article.delete()
#         return redirect('pdblog:article_list')
#     return render(request, template_name, {'form':article})

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

@login_required
@require_POST
def favorites(request):
    if request.method == 'POST':
        user = requset.user
        slug = request.POST.get('slug', None)
        article = get_object_or_404(Artilce, slug=slug)

        if article.favorites.filter(id=user.id).exsists():
            article.favorites.remove(user)
            message='Not favorite'

        else:
            article.favorites.add(user)
            message = 'Favorite'

    data={'favorites': article.total_fav, 'message': message }

    return HttpResponse(json.dumps(data), content_type='application/json')


