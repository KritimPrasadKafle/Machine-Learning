from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PeopleSerializer
from .models import Person


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
      'course_name': 'Python',
      'learn': ['Flask', 'Django', 'Tornado', 'FastApi'],
      'course_provider': 'Scaler'
    }
    if request.method == 'GET':
      print(request.GET.get('search'))
      print('You HIT A GET METHOD')
      return Response(courses)
    elif request.method == 'POST':
       data = request.data
       print(data)
       print('You HIT A POST METHOD')
       return Response(courses)
    elif request.method == 'PUT':
       print('You HIT A PUT METHOD')
       return Response(courses)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
   if request.method == 'GET':
      objs = Person.objects.all()
      serializer = PeopleSerializer(objs, many = True)
      return Response(serializer.data)
   elif request.method == 'POST':
      data = request.data 
      serializer = PeopleSerializer(data = data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      
      return Response(serializer.errors)
   
   elif request.method == 'PUT':
      data = request.data
      obj = Person.objects.get(id=data['id'])
      serializer = PeopleSerializer(obj, data = data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)

   elif request.method == 'PATCH':
      data = request.data
      obj = Person.objects.get(id = data['id'])
      serializer = PeopleSerializer(obj, data = data, partial = True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   
   else:
      data = request.data
      obj = Person.objects.get(id = data['id'])
      obj.delete()
      return Response({'message': 'Person deleted'})
