from django.urls import path

from .views import HomePageView, AboutPageView, HulkView, WidowView, HeroView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),#new
    path('', HomePageView.as_view(), name='home'),
    path('hulk/', HulkView.as_view()),
    path('black_widow', WidowView.as_view()),
    path('hero/<str:identity>', HeroView.as_view()),
]