from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class HulkView(TemplateView):
    template_name = 'hulk.html'

    def get_context_data(self, **kwargs):
        return { 'hero': 'hulk' }

class WidowView(TemplateView):
    template_name = "black_widow.html"

    def get_context_data(self, **kwargs):
        return { 'hero': 'black_widow' }

class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return { 'hero': kwargs['identity'] }
# Create your views here.
