from .models import *
from . serializers import *
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework import filters
from rest_framework.generics import ListAPIView

from .services import *



class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)  # username=admin, password=123
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response({'key': token.key})
        return Response(status=status.HTTP_403_FORBIDDEN)



class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        return Response(data={
            'id': user.id,
            'username': user.username
        })


class ProfileAPIViewSet(ModelViewSet):
    queryset = get_userprofile()
    serializer_class = ProfileSerializer



class UserAPIViewSet(ModelViewSet):
    queryset = get_userprofile()
    serializer_class = UserListSerializer


class PostAPIViewSet(ModelViewSet):
    queryset = get_post()
    serializer_class = PostSerializer



class Search1(ListAPIView):                       # version 1
    queryset = User.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']







# @api_view(['POST'])
# def authorization(request):
#     serializer = AuthValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)  # username=admin, password=123
#     if user:
#         try:
#             token = Token.objects.get(user=user)
#         except Token.DoesNotExist:
#             token = Token.objects.create(user=user)
#         return Response({'key': token.key})
#     return Response(status=status.HTTP_403_FORBIDDEN)


# @api_view(['POST'])
# def registration(request):
#     serializer = RegistrationValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data)
#     return Response(data={
#         'id': user.id,
#         'username': user.username
#     })





# @api_view(['GET', 'POST'])
# def user_list_view(request):
#     if request.method == 'GET':
#         users = UserProfile.objects.all()  # list
#         data = UserListSerializer(users, many=True).data  # serializer
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = UserListSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response()
        



# @api_view(['GET', 'PUT', 'DELETE'])
# def user_profile_item_view(request, id):
#     try:
#         profile = UserProfile.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = ProfileSerializer(profile).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ProfileSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})

#         gender = request.data.get('gender')
#         birthday = request.data.get('birthday')
#         phone = request.data.get('phone')
#         lives_in = request.data.get('lives_in')
#         profile_image = request.data.get('profile_image')
        
#         profile.gender = gender
#         profile.birthday = birthday
#         profile.phone = phone
#         profile.lives_in = lives_in
#         profile.profile_image = profile_image
#         profile.save()
#         return Response(data=ProfileSerializer(profile).data)





# @api_view(['GET', 'POST'])
# def posts_view(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()  # list
#         data = PostSerializer(posts, many=True).data  # serializer
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         user = serializer.validated_data.get('user')
#         datetime = serializer.validated_data.get('datetime')
#         image = serializer.validated_data.get('image')
#         text = serializer.validated_data.get('text')
#         posts = Post.objects.create(
#             user = user,
#             datetime = datetime,
#             image = image,
#             text = text
#         )
#         return Response(data=PostSerializer(posts).data)



# @api_view(['GET', 'PUT', 'DELETE'])
# def post_item_view(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = PostSerializer(post).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = PostSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})

#         user = request.data.get('user')
#         datetime = request.data.get('datetime')
#         image = request.data.get('image')
#         text = request.data.get('text')

#         post.user = user
#         post.datetime = datetime
#         post.image = image
#         post.text = text
#         post.save()
#         return Response(data=PostSerializer(post).data)