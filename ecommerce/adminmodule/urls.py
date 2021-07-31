from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[

    path('',views.showcategory,name='showcategory'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('myorders',views.myorders,name='myorders'),
    path('mywishlist',views.mywishlist,name='mywishlist'),
    path('search',views.search,name='search'),
    path('sliderfunc/<str:pno>',views.sliderfunc,name='sliderfunc'),
    path('showproduct/<str:catname>/<str:subcatname>/<str:val>',views.showproduct,name='showproduct'),
    path('filter-data',views.filter_data,name='filter_data'),
    path('singleproduct/<str:prodname>',views.singleproduct,name='singleproduct'),
    path('mycart/<str:prodnum>/<str:neg>',views.mycart,name='mycart'),
    path('mycarts/<str:prodnumb>/<str:carid>/<str:quant>',views.mycarts,name='mycarts'),
    path('deleteitemcart/<str:prodnumber>/<str:carid>',views.deleteitemcart,name='deleteitemcart'),
    path('register',views.register,name='register'),
    path('checkout',views.checkout,name='checkout'),
    path('receipt',views.receipt,name='receipt'),
    path('negotiate/<str:prodnumber>',views.negotiate,name='negotiate'),
    path('gotocart',views.gotocart,name='gotocart'),
    path('review',views.review,name='review'),
    path('logout',views.logout,name='logout')
   
]