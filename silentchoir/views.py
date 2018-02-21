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

class WithWhomPageView(TemplateView):
    template_name = "q1-withWhom.html"

class ComfortLevelPageView(TemplateView):
    template_name = "q2-comfortLevel.html"

class EmailPageView(TemplateView):
    template_name = "q3-email.html"

class WhenPageView(TemplateView):
    template_name = "q4-when.html"

class SettingPageView(TemplateView):
    template_name = "q5-setting.html"