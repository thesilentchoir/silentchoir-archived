from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class LegalPageView(TemplateView):
    template_name = "legal.html"

class SecurityPageView(TemplateView):
    template_name = "security.html"

class TriggerPageView(TemplateView):
    template_name = "trigger.html"

class WithWhomPageView(TemplateView):
    template_name = "q1-withWhom.html"

class EmailPageView(TemplateView):
    template_name = "q2-email.html"

class WhenPageView(TemplateView):
    template_name = "q3-when.html"

class SettingPageView(TemplateView):
    template_name = "q4-setting.html"

class WherePageView(TemplateView):
    template_name = "q5-where.html"

class IdentifyPageView(TemplateView):
    template_name = "q6-identify.html"

class SocialPageView(TemplateView):
    template_name = "q7-social.html"

class DescribePageView(TemplateView):
    template_name = "q8-describe.html"

class ResourcesPageView(TemplateView):
    template_name = "q9-resources.html"

class ConnectPageView(TemplateView):
    template_name = "q10-connect.html"

class ClosingPageView(TemplateView):
    template_name = "closing.html"

class InquirePageView(TemplateView):
    template_name = "inquire.html"