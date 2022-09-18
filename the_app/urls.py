from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'the_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='the_app/index.html'), name='index'),
]