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

class WhenAndWherePageView(TemplateView):
    template_name = "q3-whenAndWhere.html"

class SettingPageView(TemplateView):
    template_name = "q4-setting.html"

class IdentifyPageView(TemplateView):
    template_name = "q5-identify.html"

class DescribePageView(TemplateView):
    template_name = "q6-describe.html"

class ConnectPageView(TemplateView):
    template_name = "q7-connect.html"

class ResourcesPageView(TemplateView):
    template_name = "q8-resources.html"

class ClosingPageView(TemplateView):
    template_name = "closing.html"

class InquirePageView(TemplateView):
    template_name = "inquire.html"

class InquirePageView(TemplateView):
    template_name = "humans.html"