from django.views import View


class AnalysisView(View):
    def post(self, request, *args, **kwargs):
        pass

analysis = AnalysisView.as_view()
