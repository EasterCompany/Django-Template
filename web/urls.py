# Essential
from django.urls import path

# Application Views
from core.views import *

# URL Endpoints
urlpatterns = [

    # Core App
    path('', index),
    path('robots.txt', robots),
    path('manifest.json', manifestJSON),
    path('asset-manifest.json', asset_manifest)

]
