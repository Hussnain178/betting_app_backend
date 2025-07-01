from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import User  # Ensure this matches your app name
from mongoengine import NotUniqueError, DoesNotExist


@api_view(['GET'])
def test_view(request):
    return JsonResponse({'status': 'API is running'}, status=200)


# Create User
@api_view(['POST'])
def create_user_view(request):
    name = request.data.get('name')
    age = request.data.get('age')

    if not name or not age:
        return JsonResponse({'error': 'Name and age are required'}, status=400)

    try: 

        user = User(_id=name, name=name, age=age)  # _id is now the MongoDB _id
        user.save(force_insert=True)

        return JsonResponse({'message': f'User: {name} created!'}, status=201)
    except NotUniqueError:
        return JsonResponse({'error': 'User with this name already exists'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Get User by Name
@api_view(['GET'])
def get_age_view(request):
    name = request.GET.get('name')
    if not name:
        return JsonResponse({'error': 'Name is required'}, status=400)

    try:
        user = User.objects.get(_id=name)  # Safe query using .get()
        return JsonResponse({'age': user.age}, status=200)
    except DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Update User Age
@api_view(['POST'])
def update_age_view(request):
    name = request.data.get('name')
    age = request.data.get('age')

    if not name or not age:
        return JsonResponse({'error': 'Name and age are required'}, status=400)

    try:
        user = User.objects.get(_id=name)
        user.age = age
        user.save()
        return JsonResponse({'message': f'User: {name} updated!'}, status=200)
    except DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Delete User
@api_view(['POST'])
def delete_user_view(request):
    name = request.data.get('name')
    if not name:
        return JsonResponse({'error': 'Name is required'}, status=400)

    try:
        user = User.objects.get(_id=name)  # Uses MongoDB _id
        user.delete()
        return JsonResponse({'message': f'User: {name} deleted!'}, status=200)
    except DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
#
# from .models import User
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
#
#
# # from rest_framework.response import Response
#
# # Create your views here.
# @api_view(['GET'])
# def test_view(request):
#     json_data = {'age': 178}
#     response = JsonResponse(json_data, status=200)
#     return response
#
#
# # Create
# @api_view(['POST'])
# def create_user_view(request):
#     name = request.data.get('name')
#     age = request.data.get('age')
#     # name = 'name'
#     # age = 19
#     user = User(_id=name, name=name, age=age)
#     user.save()
#     json_data = {'message': f'User: {name} Created!'}
#     response = JsonResponse(json_data, status=200)
#     return response
#     # return Response({"msg": "Check your email to verify"}, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET'])
# def get_age_view(request):
#     name = request.GET.get('name')
#     found = User.objects(_id=name)
#     json_data = {'age': found.age}
#     response = JsonResponse(json_data, status=200)
#     return response
#
#
# @api_view(['POST'])
# def update_age_view(request):
#     name = request.data.get('name')
#     age = request.data.get('age')
#     found = User.objects(_id=name).first()
#     found.age = age
#     found.save()
#     json_data = {'message': f'User: {name} Updated!'}
#     response = JsonResponse(json_data, status=200)
#     return response
#
#
# @api_view(['POST'])
# def delete_user_view(request):
#     name = request.data.get('name')
#     found = User.objects(_id=name).first()
#     found.delete()
#     json_data = {'message': f'User: {name} Deleted!'}
#     response = JsonResponse(json_data, status=200)
#     return response
