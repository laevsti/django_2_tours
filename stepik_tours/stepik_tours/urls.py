from django.urls import path, re_path
from tours.views import MainView, TourView, DepartureView


urlpatterns = [
    path('', MainView.as_view()),
    path('/departure/<str:departure>/', DepartureView.as_view()),
    path('/tour/<int:id>/', TourView.as_view()),
]