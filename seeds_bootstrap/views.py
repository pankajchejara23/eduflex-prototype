from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.models import model_to_dict
from register import views as rv
from register.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import translation
from django.shortcuts import redirect
from django.core.paginator import Paginator
from register import forms as reg_forms
from django.contrib.sessions.models import Session
import pandas as pd
import pprint as pp
from django.conf import settings
from urllib.parse import unquote
from django.http import JsonResponse
from django.utils.translation import (
    check_for_language, get_language,
)
LANGUAGE_SESSION_KEY = '_language'

data = pd.read_csv('static/instructional-trajectory-session-24-results.csv')

def index(request):
    if request.method == "POST":
        pass
    else:
        students = data['Student'].to_list()
        return render(request, 'index.html', {'students': students})

def home(request):
    return render(request, 'home.html')