# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = "Morning to Ya"
