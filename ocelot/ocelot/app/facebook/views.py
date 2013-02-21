# -*- coding: utf-8 -*-
from django.shortcuts import render

from fandjango.decorators import facebook_authorization_required


@facebook_authorization_required
def home(request):
    return render(request, 'home.html', {})