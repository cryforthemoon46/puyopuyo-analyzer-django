from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        pass


index = IndexView.as_view()