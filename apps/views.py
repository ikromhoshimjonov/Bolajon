from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.models import Bolajon
from apps.serializer import BabyModelSerializer


class BabyListApiView(ListAPIView):
    queryset = Bolajon.objects.all()
    serializer_class = BabyModelSerializer

