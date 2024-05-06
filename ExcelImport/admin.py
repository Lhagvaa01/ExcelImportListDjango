from django.contrib import admin
from .models import *

class VoicherPriceAdmin(admin.ModelAdmin):
    model = VoicherPrice
    list_display = ['name', 'price']
    search_fields = [ 'name']

admin.site.register(VoicherPrice, VoicherPriceAdmin)


class UsersAdmin(admin.ModelAdmin):
    model = Users
    list_display = ['TCUSERNAME', 'TCUSERICON', 'TCEMAIL']
    search_fields =  ['TCUSERNAME', 'TCUSERICON', 'TCEMAIL']

admin.site.register(Users, UsersAdmin)


class ProductListAdmin(admin.ModelAdmin):
    model = ProductList
    list_display = ['TCITEMCODE',  'TCNAME', 'TCSALEPRICE','get_voucher', 'TCBARCODE']
    search_fields =  ['TCITEMCODE',  'TCNAME', 'TCSALEPRICE', 'TCBARCODE']

    def get_voucher(self, obj):
        return obj.TCVOUCHERPRICEPk.price

    get_voucher.short_description = 'get_voucher'

admin.site.register(ProductList, ProductListAdmin)