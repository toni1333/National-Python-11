import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Location, Pontaj
from django.urls import reverse

# Create your views here.

#ListView  listarea datelor dintr un model
#


class LocationsView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'

class CreateLocationsView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'


    def get_success_url(self):
        return reverse('locations:lista_locatii')


class UpdateLocationsView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/locations_form.html'

    def get_succes_url(self):
        return reverse('locations:lista_locatii')
@login_required
def delete_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect('locations:lista_locatii')
@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect('locations:lista_locatii')

@login_required
def new_timesheet(request):
    Pontaj.objects.create(user_id=request.user.id, start_date= datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
