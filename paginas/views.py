from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    
class ModeloView(TemplateView):
    template_name = "modelo.html"


class SobreView(TemplateView):
    template_name = "sobre.html"
