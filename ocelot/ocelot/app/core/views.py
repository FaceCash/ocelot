# encoding: utf-8
from django import http
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import LoginForm

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

def context_processor(request):
    login_form = LoginForm()
    return {'login_form': login_form}


def site_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            redirect = request.GET.get('next')
            if redirect == reverse('login'):
                redirect = '/'
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return http.HttpResponseRedirect(redirect)
                else:
                    alert = ('alert', 'User inactive.',)
            else:
                alert = ('alert-error', 'invalid user/password.')
        else:
            alert = ('alert', 'Please, complete the form.')

        return render(request, 'quiz/index.html', {'alert':alert})
    else:
        return render(request, 'quiz/index.html')


def site_logout(request):
    logout(request)
    return http.HttpResponseRedirect(reverse('index'))