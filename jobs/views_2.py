"""
Applicant (Resource)
GET HTTP request
- singular
- plural
"""
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Applicant


# Create your class based view like following -
#
"""
is a decorator used in Django views to exempt 
the view from Cross-Site Request Forgery (CSRF) protection.
"""


@method_decorator(csrf_exempt, name='dispatch')
class ApplicantList(ListView):
    """
    jobs/applicant_list.html
    """

    model = Applicant


class ApplicantDetailView(DetailView):
    """
     jobs/applicant_detail.html
     """

    model = Applicant
    context_object_name = 'applicant'
    queryset = Applicant.objects.all()


class ApplicantCreate(CreateView):

    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("v2-applicant-list")


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["id", "name", "cover_letter"]
    success_url = reverse_lazy("v2-applicant-list")


class ApplicantDelete(DeleteView):
    model = Applicant
    success_url = reverse_lazy("v2-applicant-list")
