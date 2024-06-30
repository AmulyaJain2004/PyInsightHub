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
    return Response({'status': 200, 'payload': serializer.data, 'message':'you sent'})

@api_view(['PUT'])
def update_student(request, id):
    try:    
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data)
        
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors, 'message': 'Something went wrong'})
        
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message':'your data is saved'})
    
    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})
    
@api_view(['PATCH'])
def update_student_patch(request, id):
    try:    
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors, 'message': 'Something went wrong'})
        
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message':'your data is saved'})
    
    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})

# method 1    
# @api_view(['DELETE'])
# def update_student_patch(request, id):
#     try:    
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200, 'message': 'deleted'})

#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})
    
    
@api_view(['DELETE'])
def update_student_patch(request):
    try:    
        id = request.GET.get('id')
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200, 'message': 'deleted'})

    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})
