from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


class get_VoucherPrice(APIView):
    def get(self, request):
        queryset = VoicherPrice.objects.all()
        serializer_class = VoicherPriceSerializer(queryset, many=True)

        

        return JsonResponse({"statusCode": "200", "dtl": serializer_class.data}, safe=False)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"statusCode": "200", "body": serializer.data})


class createUsersViewSet(APIView):

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"statusCode": "200", "body": serializer.data})
        error_string = str(serializer.errors)
        return Response({"statusCode": "400", "body": error_string}, status=status.HTTP_400_BAD_REQUEST)

class loginUsersViewSet(APIView):
    def post(self, request):
        mail = request.data.get('TCEMAIL')
        password = request.data.get('TCPASSWORD')
        data = Users.objects.filter(TCEMAIL=mail).first()
        if data:
            if data.TCPASSWORD == password:
                serializer = UsersSerializer(data)
                return Response({"statusCode": "200", "body": serializer.data})
            return Response({"statusCode": "400", "body": "Нууц үг буруу байна"})
        return Response({"statusCode": "400", "body": "Хэрэглэгч бүртгэгдээгүй байна"})
    

class EditUserAPIView(APIView):

    def put(self, request, pk, *args, **kwargs):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"statusCode": "200", "dtl": serializer.data})
        return JsonResponse({'error': 'Invalid JSON data', "body": serializer.errors}, status=400)


# class MyLists(APIView):
#     def get(self, request, userPk):
#         queryset = CreateLists.objects.filter(TCUSERPK=userPk)
#         serializer = CreateListsSerializer(queryset, many=True)
#         return JsonResponse({"statusCode": "200", "body": serializer.data}, safe=False)
    

#     def post(self, request):
#         serializer = CreateListsSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             # Extract data from request
#             tcuserpk_id = request.data.get('TCUSERPK')
#             tcuser = Users.objects.get(id=tcuserpk_id)  # Retrieve Users instance
#             tclocationspk_id = request.data.get('TCLOCATIONSPK')
#             tclocation = Location.objects.get(id=tclocationspk_id)  # Retrieve Location instance
#             tcbirdpk = request.data.get('TCBIRDPK')
#             tclistname = request.data.get('TCLISTNAME')
#             tcdate = request.data.get('TCDATE')

#             # Create CreateLists object
#             createlists = CreateLists.objects.create(
#                 TCUSERPK=tcuser,
#                 TCLOCATIONSPK=tclocation,
#                 TCLISTNAME=tclistname,
#                 TCDATE=tcdate
#             )
#             # Add TCBIRDPK
#             createlists.TCBIRDPK.add(*tcbirdpk)

#             # Return success response
#             return Response({"statusCode": "200", "body": "created"}, status=status.HTTP_200_OK)
#         else:
#             # Return error response with validation errors
#             return Response({"statusCode": "400", "body": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

#     def put(self, request):
#         try:
#             pk = request.data.get('pk')
#             createlists = CreateLists.objects.get(pk=pk)
#         except CreateLists.DoesNotExist:
#             return Response({"statusCode": "404", "body": "CreateLists object not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = CreateListsSerializer(createlists, data=request.data)
#         if serializer.is_valid():
#             tcbirdpk = request.data.get('TCBIRDPK')
#             createlists.TCBIRDPK.set(tcbirdpk)  # Update TCBIRDPK field with new value
#             createlists.save()  # Save the changes
            
#             serializer = CreateListsSerializer(createlists)
#             return Response({"statusCode": "200", "message": "updated successfully", "body": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"statusCode": "400", "body": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

#     def delete(self, request):
#         try:
#             pk = request.data.get('pk')
#             createlists = CreateLists.objects.get(pk=pk)
#         except CreateLists.DoesNotExist:
#             return Response({"statusCode": "404", "body": "CreateLists object not found"}, status=status.HTTP_404_NOT_FOUND)

#         createlists.delete()  # Delete the object
#         return Response({"statusCode": "200", "body": "deleted successfully"}, status=status.HTTP_200_OK)
    

# class ForgotPass(APIView):
#     def post(self, request):
#         mail = request.data.get('TCEMAIL')
#         user = Users.objects.filter(TCEMAIL=mail).first()
        
#         if user:
#             # Generate OTP
#             otp = get_random_string(length=4, allowed_chars='0123456789')

#             # Save OTP in user's model or database table
#             user.otp = otp
#             user.save()

#             # Compose email
#             subject = 'Forgot Password OTP'
#             message = f'Your OTP is: {otp}'
#             from_email = 'sales@kacc.mn'
#             recipient_list = [mail]

#             # Send email
#             send_mail(subject, message, from_email, recipient_list)
            
#             serializer = UsersSerializer(user)
#             serializer_data = serializer.data

#             return Response({"statusCode": "200", "message": "OTP sent successfully", "body":serializer_data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"statusCode": "400", "message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)