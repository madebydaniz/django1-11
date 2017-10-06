import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

@login_required()
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        # obj = RestaurantLocation.objects.create(
        #     name = form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),
        #     category = form.cleaned_data.get('category ')
        # )
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/restaurants/')
        else:
            return HttpResponseRedirect('/login/')
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
    'object_list' : queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    # login_url = '/login/'
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    # success_url = '/restaurants/'

    def get_context_data(self, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add restaurant'
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)
