from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
# Model Object - Single Student Data
# def student_detail(request):
#     stu = Student.objects.get(id=3)
#     print(stu)
    
#     serializer = StudentSerializer(stu)
#     print(serializer)
#     print(serializer.data)
    
#     json_data = JSONRenderer().render(serializer.data)
#     print(json_data)
    
#     return HttpResponse(json_data)

# using primary key as id
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    print(stu)
    
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    
    return HttpResponse(json_data)

# Query set - All Student Data
# def student_list(request):
#     stu = Student.objects.all()
#     print(stu)
    
#     serializer = StudentSerializer(stu, many=True)
#     print(serializer)
#     print(serializer.data)
    
#     json_data = JSONRenderer().render(serializer.data)
#     print(json_data)
    
#     return HttpResponse(json_data)



#----------------------------# the below lines of the functions can be replaced by
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    
    # return HttpResponse(json_data)
    
#----------------------------# By applying these lines
# from django.http import HttpResponse, JsonResponse

#     return JsonResponse(serializer.data, safe=True)  #by default safe = True if error comes due to non dict items so make safe=False


#-----------------------# the output data doesn't show but it is generated from models.Model by default 
# so to display wehave to specify id = serializers.IntegerField() in serializers.py to do this.  