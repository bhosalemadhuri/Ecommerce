from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.html import mark_safe

# Create your models here.
class category(models.Model):
    catname=models.CharField(max_length=100,primary_key=True)
    catimage=models.ImageField(upload_to='pics')
    def __str__(self):
        return str(self.catname)

    
class subcategory(models.Model):
    subcatname=models.CharField(max_length=200,primary_key=True)
    catnam=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.subcatname)

class product(models.Model):
    product_number=models.CharField(max_length=100,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_image=models.ImageField(upload_to='pics')
    product_price=models.IntegerField(default=0)
    minimum_price=models.IntegerField(null=True)
    soldby=models.CharField(max_length=200)
    catna=models.ForeignKey(category,on_delete=models.CASCADE)
    subcatname=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_number)

class userdetails(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=20)
    address=models.TextField(null=True)
    pincode=models.IntegerField(null=True)
    state=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=30,null=True)
    gender=models.CharField(max_length=10,null=True)
    def __str__(self):
        return str(self.email)

class productdetails(models.Model):
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    brand=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    related_to=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    size=models.CharField(max_length=100)
    description=models.TextField()
    item_weight=models.CharField(max_length=100)
    discount=models.IntegerField()
    def __str__(self):
        return str(self.product_number)

class cart(models.Model):
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    size=models.CharField(max_length=100)
    created_date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    discount_price=models.IntegerField()
    cart_id=models.CharField(max_length=100)
    negotiation_status=models.CharField(max_length=100)
    def __str__(self):
        return str(self.product_number)

class orderdetails(models.Model):
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    size=models.CharField(max_length=100)
    ordered_date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    order_id=models.CharField(max_length=100)
    order_status=models.CharField(max_length=100)
    discount_price=models.IntegerField()
    negotiation_status=models.CharField(max_length=100)
    def __str__(self):
        return str(self.order_id)
   

class paymentdetails(models.Model):
    payment_id=models.CharField(max_length=100)
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    order_id=models.CharField(max_length=100)
    payment_date=models.DateField(auto_now_add=True)
    payment_mode=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    def __str__(self):
        return str(self.email)

class negotiationdetails(models.Model):
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    discount_rate=models.IntegerField()
    negotiated_price=models.IntegerField()
    counter=models.IntegerField()
    negotiated_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.email)

class chatmessages(models.Model):
    message_date=models.DateField(auto_now_add=True)
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    message=models.TextField()
    
class advertisement(models.Model):
   product_number=models.ForeignKey(product,on_delete=models.CASCADE)
   product_image=models.ImageField(upload_to='pics')
   
class recentlyviewed(models.Model):
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    viewed_date=models.DateField(auto_now_add=True)
    
class searchitems(models.Model):
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    search_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.product_number)

class wishlist(models.Model):
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.product_number)

class reviews(models.Model):
    product_number=models.ForeignKey(product,on_delete=models.CASCADE)
    email=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    review_date=models.DateField(auto_now_add=True)
    stars=models.IntegerField()
    suggestion=models.TextField()
    def __str__(self):
        return str(self.product_number)

    