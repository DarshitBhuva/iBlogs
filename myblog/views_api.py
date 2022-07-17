from queue import Empty
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import BlogUsers

class LoginView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'Key Username is not found'
                raise Exception("Key Username not found")
            
            if data.get("password") is None:
                response['message']  = 'Key Password not found'   
                raise Exception("Key Password not found")

            check_user = User.objects.filter(username = data.get("username"))
            # print(check_user)
            if len(check_user) == 0:
                  response['message']  = 'Invalid Username'   
                  raise Exception("Invalid Username, User not found")
              
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))  

            # print(user_obj)
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message']  = 'Invalid Password'   
                raise Exception("Invalid Password")
            
        except Exception as e:
            print(e)        
            
        return Response(response)    
    
LoginView = LoginView.as_view()    

class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'Key Username is not found'
                raise Exception("Key Username not found")
            
            if data.get("password") is None:
                response['message']  = 'Key Password not found'   
                raise Exception("Key Password not found")

            check_user = User.objects.filter(username = data.get("username"))
            print(check_user)
            if check_user:
                  response['message']  = 'Username already taken'   
                  raise Exception("Username already taken")
              
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User created'
            response['status'] = 200
           
        except Exception as e:
            print(e)        
            
        return Response(response)    
    
    
RegisterView = RegisterView.as_view()    