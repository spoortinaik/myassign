from rest_framework import viewsets
from .models import Branch,Organisarion
from .serializers import BranchFormSerializer,OrgFormSerializer
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class BranchFormViewList(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchFormSerializer

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = "branch/index.html"
        return template_name


class OrgFormViewList(viewsets.ModelViewSet):
    queryset = Organisarion.objects.all()
    serializer_class = OrgFormSerializer





  
