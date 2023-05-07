from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'accounts/home.html'


class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'


    