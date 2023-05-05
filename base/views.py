from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import Computers,Phones,User,CustomerUser

from .serializer import ComputersSerializer,PhonesSerializer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
# ,CustomerUserForm,CustomerUserChangeForm
from django.contrib.auth.decorators import login_required
# from .forms import CustomerUserCreationForm, CustomerUserChangeForm
from django.contrib.auth import authenticate, login



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod

    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # replace 'home' with the name of your home page URL pattern
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





# @login_required
# def profile(request):
#     return render(request, 'profile.html')

# @login_required
# def profile_update(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserChangeForm(instance=request.user)
#     return render(request, 'profile_update.html', {'form': form})

    



def index(req):
    return JsonResponse('HELLO ELY FROM VIEWS', safe=False)

def myComputers(req):
    all_products = ComputersSerializer(Computers.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def myPhones(req):
    all_products = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def allMyProducts(req):
    all_computers = ComputersSerializer(Computers.objects.all(), many=True).data
    all_phones = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_computers+all_phones, safe=False)



# @api_view(['GET','POST'])
# def user(request):
#     print(request)
#     array=[]
#     for user in User.objects.all():
#         array.append({"complete_name":user.complete_name,"email":user.email,"id":user.id})
#     return HttpResponse(array)

# use 

# @api_view(['GET','POST'])
# def user(request):
#      if request.method == 'GET':
#           array=[]
#           for user in User.objects.all():
#                array.append({""})
        
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
# 	return "i'm protected"     
