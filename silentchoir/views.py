from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class IntroPageView(TemplateView):
    template_name = "intro.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class LegalPageView(TemplateView):
    template_name = "legal.html"

class ConsentPageView(TemplateView):
    template_name = "consent.html"

class TriggerPageView(TemplateView):
    template_name = "trigger.html"