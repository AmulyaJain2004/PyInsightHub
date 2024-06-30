from rest_framework import serializers
from .models import Student


class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id', ]
        fields = '__all__'