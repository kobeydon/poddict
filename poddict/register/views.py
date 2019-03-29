from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm
)


User = get_user_model()



class UserCreate(generic.CreateView):
    """temporary registration"""
    template_name = 'register/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        # """temporarily register and send activation mail"""
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        """ send activation url """
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol':self.request.scheme,
            'domain':domain,
            'token':dumps(user.pk),
            'user':user,
            }

        subject_template = get_template('register/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('register/mail_template/create/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('register:user_create_done')


class UserCreateDone(generic.TemplateView):
    """ User temporary registration is done """
    template_name = 'register/user_create_done.html'

class UserCreateComplete(generic.TemplateView):
    """Officially register new user when activate by clicking the link in the Email"""
    template_name = 'register/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)

    def get(self,request,**kwargs):
        """register if token is correct"""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

            return HttpResponseBadRequest()


class Top(generic.TemplateView):
    template_name = 'register/top.html'


class Login(LoginView):
    """login page"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """logout page"""
    template_name = 'register/top.html'# Create your views here.
