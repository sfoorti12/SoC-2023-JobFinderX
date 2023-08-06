from django.shortcuts import render
from .models import PostJobModel, UserModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PostJobSerializer, UserSerializer
from django.contrib.auth.models import User
import datetime, jwt
from django.contrib.auth.hashers import make_password

# Create your views here.
@api_view(['POST'])
def create_user(request):
        email = request.data.get('email')
        password = request.data.get('password')
        fname = request.data.get('fname')
        lname = request.data.get('lname')
        contact = request.data.get('contact')
        address = request.data.get('address')

        if User.objects.filter(username=email).exists():
            return Response({'error': 'Email already exists'})

        user = User.objects.create(
            username=email, password=make_password(password))
        UserModel.objects.create(
            user=user, fname=fname, lname=lname, contact=contact, address=address)

        return Response({'success': 'User registered successfully'})

@api_view(['POST'])
def user_login(request):
    email = request.data['email']
    password = request.data['password']
    
    user = User.objects.filter(username=email).first()

    if user is None:
        return Response({
            "jwt": '',
            "error": "Invalid Credentials"
        })
    if not user.check_password(password):
        return Response({
            "jwt": '',
            "error": "Invalid Password"
        })
    is_admin = user.is_staff
    payload = {
        'id': user.id,
        'is_admin' : is_admin,
        # Set the expiration to a far future date
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=36500),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {
        'jwt': token,
        'error': ''
    }

    return response

@api_view(['POST', 'PUT'])
def create_job(request):
    # if not request.user.is_staff:
    #     return Response({'error': 'You do not have permission to create a job'})
    if request.method == 'POST':
        
        company = request.data['company']
        position = request.data['position']
        job_type = request.data['job_type']
        education = request.data['education']
        experience = request.data['experience']
        salary = request.data['salary']
        location = request.data['location']
        
        PostJobModel.objects.create(
            company=company, position=position, job_type=job_type, education=education, experience=experience, salary=salary, location=location)
        
        return Response({'success': 'Job posted successfully'})
    
    if request.method == 'PUT':
        
        company = request.data['company']
        position = request.data['position']
        job_type = request.data['job_type']
        job = PostJobModel.objects.filter(company=company, position=position).first()
        serializer = PostJobSerializer(serializer)
        
        education = request.data['education']
        experience = request.data['experience']
        salary = request.data['salary']
        location = request.data['location']
        
        PostJobModel.objects.create(
            company=company, position=position, job_type=job_type, education=education, experience=experience, salary=salary, location=location)
        
        return Response({'success': 'Job Updated successfully'})
    
    
@api_view(['GET'])
def get_job(request):
    job = PostJobModel.objects.all()
    serializer = PostJobSerializer(job, many=True)
    return Response(serializer.data)