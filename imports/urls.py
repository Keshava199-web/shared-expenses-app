from django.urls import path

from .views import ImportCSVView

urlpatterns = [
    path("upload/", ImportCSVView.as_view()),
]