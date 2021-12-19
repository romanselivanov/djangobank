from django.urls import path
import nezbank.views as views


urlpatterns = [
    path('', views.GetRoot.as_view()),
]
