from django.urls import path
from tours.views import MainView, TourView, DepartureView


urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:tour_id>', TourView.as_view())
]
