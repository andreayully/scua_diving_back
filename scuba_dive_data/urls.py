from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from scuba_diving_back.views import ScubaDiveDataListCreateView

urlpatterns = {
    path('scuba-dive-data/', ScubaDiveDataListCreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
