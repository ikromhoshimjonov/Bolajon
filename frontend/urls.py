from django.urls import path
from frontend.views import welcome_page_baby

urlpatterns = [
    path("", welcome_page_baby, name="frontend_index"),
]