# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

# Handling forms with class-based views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .forms import MyForm


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = "Morning to Ya"


def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # xxxxxx
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})


class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


def success(request):
    return HttpResponse("Success !")
