import json

from django.views import View

from ..domain.usecase.chain_analysis_usecase import ChainAnalysisUseCase


class ChainAnalysisView(View):
    def post(self, request, *args, **kwargs):
        board_areas = request.POST["board_areas"]
        board_areas = json.loads(board_areas)
        captured_image_data = request.POST["captured_image_data"]
        chain_analysis_usecase = ChainAnalysisUseCase(board_areas,
                                                      captured_image_data)
        chain_analysis_usecase.make_boards()
        

chain_analysis = ChainAnalysisView.as_view()
