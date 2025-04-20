from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):

  class Meta:
    model = Person
    fields = '__all__'

  def validate_age(self, data):
    pass 

  def validate(self, data):
    if data['age'] < 18:
      raise serializers.ValidationError('Age must be 18 or older')
    return data     
