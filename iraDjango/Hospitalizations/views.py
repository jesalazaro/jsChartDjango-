from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Hospitalizations


class HospitalizationsChartView(TemplateView):
    template_name = 'Hospitalizations/chartHospi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Hospitalizations.objects.all()
        return context

# Create your views here.
