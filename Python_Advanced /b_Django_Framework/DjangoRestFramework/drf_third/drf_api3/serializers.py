from rest_framework import serializers
from .models import Student


class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id', ]
        fields = '__all__'
        
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': "age cannot be less than 18"})
        
        if data['name']:
            for n in data['name']:
                if n.is_digit():
                    raise serializers.ValidationError({'error': "name cannot be numeric"})
        
        return data 