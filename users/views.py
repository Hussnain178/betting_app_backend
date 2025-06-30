from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view


# from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def test_view(request):
    json_data = {'age': 178}
    response = JsonResponse(json_data, status=200)
    return response


# Create
@api_view(['POST'])
def create_user_view(request):
    # name = request.GET.get('name')
    # age = request.GET.get('age')
    name = 'name'
    age = 19
    user = User(name=name, age=age)
    user.save()
    json_data = {'message': f'User: {name} Deleted!'}
    response = JsonResponse(json_data, status=200)
    return response
    # return Response({"msg": "Check your email to verify"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_age_view(request):
    name = request.GET.get('name')
    found = User.objects(name=name).first()
    json_data = {'age': found.age}
    response = JsonResponse(json_data, status=200)
    return response


@api_view(['POST'])
def update_age_view(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    found = User.objects(name=name).first()
    found.age = age
    found.save()
    json_data = {'message': f'User: {name} Deleted!'}
    response = JsonResponse(json_data, status=200)
    return response


@api_view(['POST'])
def delete_user_view(request):
    name = request.GET.get('name')
    found = User.objects(name=name).first()
    found.delete()
    json_data = {'message': f'User: {name} Deleted!'}
    response = JsonResponse(json_data, status=200)
    return response
