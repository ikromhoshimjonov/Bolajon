from rest_framework.serializers import ModelSerializer

from apps.models import Bolajon


class BabyModelSerializer(ModelSerializer):
    class Meta:
        model = Bolajon
        fields = 'id', "instagram",'telegram','phone_number','longitude','latitude'