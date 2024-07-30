# from resumeapp.api.views import 
from rest_framework.routers import DefaultRouter
from resumeapp.api.views import CodingLanguageList, CodingToolList, IndividualAssignmentList, IndividualProjectList, GroupProjectList
# 
from django.urls import path, include

from .views import CodingLanguageListView

# using sets & routes
router = DefaultRouter()
router.register('cl', CodingLanguageList, basename='codinglang')
router.register('ct', CodingToolList, basename='codingtool')
router.register('gp', GroupProjectList, basename='groupproject')
router.register('ia', IndividualAssignmentList, basename='individualassignment')
router.register('ip', IndividualProjectList, basename='individualproject')

urlpatterns = [
    # path('cl/', CodingLanguageListView.as_view(), name='coding_language_list'),
    path('', include(router.urls)),
]