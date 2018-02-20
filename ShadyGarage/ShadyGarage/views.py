from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class error_404(TemplateView):
    template_name = 'error404.html'

class error_500(TemplateView):
    template_name = 'error500.html'
