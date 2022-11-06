from rest_framework import serializers
from .model import Hero 

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    model = Hero
    fields = ('id','name','alias')