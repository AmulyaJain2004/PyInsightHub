from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def home (request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many = True)
    
    return Response({'status': 200, 'payload': serializer.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'errors':serializer.errors, 'message': 'Something went wrong'})
    
    serializer.save()
        
    print(data)
    return Response({'status': 200, 'payload': data, 'message':'you sent'})
    
# hw make functions for all operations                  