from django.views import View


class ChainAnalysisView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST["image"])

chain_analysis = ChainAnalysisView.as_view()
