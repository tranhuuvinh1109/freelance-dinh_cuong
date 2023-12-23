from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id','location', 'name_ttcq', 'phone_staff', 'km', 'name', 'phone', 'date','note', 'createAt', 'updateAt']
