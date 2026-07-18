from django.urls import path

from apps.views import BabyListApiView

urlpatterns = [
path('list/data/',BabyListApiView.as_view())
]