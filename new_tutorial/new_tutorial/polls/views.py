from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Question, Choice
from .forms import VoteForm, MyForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
#
#
# def results(request, question_id):
#     obj = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question': obj,
#     })

# def detail(request, question_id):
#     obj = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = VoteForm(question=obj, data=request.POST)
#         if form.is_valid():
#             form.vote()
#             return redirect('polls:results', question_id)
#     else:
#         form = VoteForm(question=obj)
#     return render(request, 'polls/detail.html', {
#         'form': form,
#         'question': obj,
#     })

class Detail(SingleObjectMixin, FormView):
    model = Question
    form_class = VoteForm
    context_object_name = 'question'
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['question'] = self.object
        return kwargs

    def form_valid(self, form):
        form.vote()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('polls:results', self.kwargs['pk'])

detail = Detail.as_view()

class FormTest(FormView):
    form_class = MyForm
    template_name = 'polls/forms.html'
    success_url = reverse_lazy('polls:index')

form_test = FormTest.as_view()
