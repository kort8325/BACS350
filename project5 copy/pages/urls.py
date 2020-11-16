from django.urls import path
from .views import BlogListView, BlogDetailView, HomePage, BasePage

urlpatterns = [
    path('hero',BlogListView.as_view(), name='hero'),  
    path('<int:pk>', BlogDetailView.as_view(), name='hero_detail'),
    path('', HomePage.as_view(), name='home'),
    path('home', HomePage.as_view(), name='home'),
    
]