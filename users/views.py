from django.shortcuts import render
from models import User
# Create your views here.
# Create
user = User(name="John", age=30)
user.save()

# Query
found = User.objects(name="John").first()
print(found.age)

# Update
found.age = 31
found.save()

# Delete
found.delete()
