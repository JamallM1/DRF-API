from django.urls import path
from .views import CoreList, CoreDetail

urlpatterns = [
    path("", CoreList.as_view(), name="core_list"),
    path("<int:pk>/", CoreDetail.as_view(), name="core_detail"),
]
