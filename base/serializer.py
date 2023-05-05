from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Computers,Phones




class ComputersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = '__all__'

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones 
        fields = '__all__'

class AllProductSerializer(serializers.ModelSerializer):
    model_one = SerializerMethodField()
    model_two = SerializerMethodField()

    class Meta:
        model = None
        fields = ('model_one', 'model_two')


    def get_model_one(self, obj):
        serializer = ComputersSerializer(obj)
        return serializer.data
    
    def get_model_two(self, obj):
        serializer = PhonesSerializer(obj)
        return serializer.data