from django.urls import path
from ExcelImport import views
from ExcelImport.views import *

urlpatterns = [
    path('get_VoucherPrice/', get_VoucherPrice.as_view(), name='get_VoucherPrice'),
    path('createUser/', createUsersViewSet.as_view(), name='createUsersViewSet'),
    path('loginUser/', loginUsersViewSet.as_view(), name='loginUsersViewSet'),
    path('editUser/<int:pk>/', EditUserAPIView.as_view(), name='EditUserAPIView'),
]
 