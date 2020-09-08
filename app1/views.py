from django.views.generic import TemplateView
from .models import Category


class IndexPageView(TemplateView):
    template_name = 'index.html'

