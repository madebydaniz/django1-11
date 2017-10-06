from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

# from restaurants.views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, restaurant_createview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^items/', include('menus.urls', namespace='menus')),
    # url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    # url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurants-create'),
    # url(r'^restaurants/create/$', restaurant_createview),
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
    # url(r'^restaurants/(?P<rest_id>\d+)/$', RestaurantDetailView.as_view()),
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
]
