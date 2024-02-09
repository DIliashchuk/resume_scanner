from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_pdf, name='upload'),
    # Add other URL patterns if needed
]