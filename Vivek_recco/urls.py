# In Vivek_recco/urls.py

from django.urls import path
from trends.views import trending_view  # Import the trending_view

urlpatterns = [
    path('', trending_view, name='trendinghome'),  # Add this line for the root URL
    path('trending/', trending_view, name='trending'),  # Keeps the trending URL as well
    # ... other url patterns ...
]

