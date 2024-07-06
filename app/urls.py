from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename='blog')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('login', LoginView.as_view(), name='login'),
    path('login', views.login),
    path('signup', views.signup),
    path('test_token', views.test_token),
    
    path('', include(router.urls)),
]