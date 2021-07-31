from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import category,subcategory,product,productdetails,orderdetails,paymentdetails,negotiationdetails,userdetails,advertisement
# Register your models here.
admin.site.site_header="Admin Dashboard"
class categoryAdmin(admin.ModelAdmin):
    list_display = ('catname', 'catimage')
    search_fields=['catname']

class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcatname', 'catnam')
    list_filter = ['catnam']
    search_fields=['subcatname']

class productAdmin(admin.ModelAdmin):
    list_display = ('product_number','product_name', 'product_price','minimum_price','catna','subcatname')
    list_filter = ['catna','subcatname']
    search_fields=['product_name','product_number']

class productdetailsAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'brand','type','related_to','color','discount','size')
    list_filter = ['brand','type','related_to','color','size']
    search_fields=['brand','type','related_to','color']


class orderdetailsAdmin(admin.ModelAdmin):
    list_display = ('order_id','email', 'product_number','size','ordered_date','quantity','discount_price','negotiation_status')
    list_filter = ['product_number','ordered_date','order_id']
    search_fields=['order_id']
    list_display_links=None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    
class paymentdetailsAdmin(admin.ModelAdmin):
    list_display = ('payment_id','order_id', 'payment_date','payment_mode','amount_paid')
    list_filter = ['payment_id','payment_mode','order_id']
    search_fields=['payment_id','order_id']
    list_display_links=None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    
class negotiationdetailsAdmin(admin.ModelAdmin):
    list_display = ('email','product_number', 'discount_rate','negotiated_price')
    list_filter = ['product_number','email']
    search_fields=['negotiated_price']
    list_display_links=None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    
class userdetailsAdmin(admin.ModelAdmin):
    list_display = ('fullname','email', 'address','pincode','state','country','city','phonenumber')
    list_filter = ['country','city','state']
    search_fields=['email','address','pincode','state','country','city','phonenumber']
    list_display_links=None
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False

class advertisementAdmin(admin.ModelAdmin):
    list_display=('product_number','product_image')


admin.site.register(category,categoryAdmin)
admin.site.register(subcategory,subcategoryAdmin)
admin.site.register(product,productAdmin)
admin.site.register(productdetails,productdetailsAdmin)
admin.site.register(orderdetails,orderdetailsAdmin)
admin.site.register(paymentdetails,paymentdetailsAdmin)
admin.site.register(negotiationdetails,negotiationdetailsAdmin)
admin.site.register(userdetails,userdetailsAdmin)
admin.site.register(advertisement,advertisementAdmin)
