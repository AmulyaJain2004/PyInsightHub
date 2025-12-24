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
    
    # we can write the logic for custom validation here but it is not a good practice to follow. 
    # if request.data['age'] < 18:
    #     return Response({'stataus':403, 'message': 'age must be > 18'})
    # All these logic should be written inside serializer class in serializers.py to ensure MVC architecture.
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'errors':serializer.errors, 'message': 'Something went wrong'})
    
    serializer.save()
        
    print(data)
    return Response({'status': 200, 'payload': data, 'message':'you sent'})