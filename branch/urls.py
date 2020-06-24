from django.urls import include,path
from rest_framework import routers
from .views import BranchFormViewList, IndexTemplateView,OrgFormViewList
# from .views import 



router = routers.DefaultRouter()
router.register('branch', BranchFormViewList)
router.register('org', OrgFormViewList)

urlpatterns = [
    # path("branchdetails/<int:pk>/",Branchview,name="branch_details"),
    path('', include(router.urls)),
  
]