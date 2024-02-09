from django.contrib import admin
from django.urls import path
from resumes.views import upload_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_pdf, name='upload_pdf'),
    # ... other URL patterns for your project ...
]