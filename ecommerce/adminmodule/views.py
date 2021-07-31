from django.db.models.query import get_prefetcher
from django.shortcuts import render,redirect
from .models import reviews,wishlist,searchitems,recentlyviewed,advertisement,chatmessages,category, orderdetails, paymentdetails, product,subcategory,userdetails,productdetails,cart,orderdetails,paymentdetails,negotiationdetails
from django.http import HttpResponse, request,JsonResponse
from datetime import date
import random
import pytz
from datetime import datetime
import time
from django.template.loader import render_to_string
from django.db.models import Count,Avg
from django.core.mail import BadHeaderError, send_mail

# Create your views here.
def showcategory(request):
    cat=category.objects.all()
    #subcat=subcategory.objects.all().order_by('id')
    subcat = subcategory.objects.all()
    sessemail=""
    sessem=""
    email=""
    
    #print(subcat.catname)
    #print(subcategory.catname)
   # subcat=subcategory.objects.values('catid_id').get(catid=cat.catid)['id']
    fullname=""
    
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    productssdet=productdetails.objects.all()
    productss=product.objects.all()
    reproducts=product.objects.filter(recentlyviewed__email=sessem).order_by('-recentlyviewed__id')[:4]
    ts1=""
    res2=[]
    i=0
    for orii in reproducts:
        pq1=orii.product_number
        ts1=pq1
        if i==0:
            res2.append(ts1)
        else:
            res2.append(ts1)
        i=i+1    
    print(res2)
    print("demo")
    reproductdet=productdetails.objects.filter(product_number__in=res2).order_by('-product_number').distinct().all()[:4]
    #print(prcat4)
    
    #reproductdet=productdetails.objects.filter(recentlyviewed__email=sessem).order_by('-product_number')[:4]
    reproducts1=product.objects.filter(recentlyviewed__email=sessem).order_by('-recentlyviewed__id')[4:8]
    reproducts2=product.objects.filter(recentlyviewed__email=sessem).count()
    ts2=""
    res3=[]
    j=0
    for oriii in reproducts1:
        pq1=oriii.product_number
        ts2=pq1
        if j==0:
            res3.append(ts2)
        else:
            res3.append(ts2)
        j=j+1    
    print(res3)
    print("ccc")
    
    reproductdet1=productdetails.objects.filter(product_number__in=res3).order_by('-product_number').distinct().all()
    print(reproducts)
    print(reproductdet)
    print(reproducts1)
    print(reproductdet1)
    print("take care")
    ad=advertisement.objects.filter().order_by('-id')[:4]
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    records = productdetails.objects.filter(related_to__in=[item['related_to'] for item in distinct])
    getitem=searchitems.objects.filter(email=email).order_by('-id').distinct()
    ts4=""
    res5=[]
    l=0
    print(getitem)
    print("mapper")
    for git in getitem:
       pq1=git.product_number
       print(pq1)
       print("my test")
       ts4=pq1
       if l==0:
            res5.append(ts4)
       else:
            res5.append(ts4)
       l=l+1   

    print(res5)
    odd=orderdetails.objects.filter(product_number__in=res5).values_list('product_number',flat=True).exclude(email=email).distinct()
    print(odd)
    ts5=""
    res6=[]
    l=0
    for odt in odd:
       pq2=odt
       print(pq2)
       print("my test2")
       ts5=pq2
       if l==0:
            res6.append(ts5)
       else:
            res6.append(ts5)
       l=l+1   

    print(res6)
    
    print(email)
    produ=product.objects.filter(orderdetails__product_number__in=res6).annotate(name_count=Count('product_number')).filter(name_count__gte=2).distinct()
    print(produ)
    ts6=""
    res7=[]
    l=0
    for prd in produ:
       pq3=prd
       print(pq3)
       print("my test3")
       ts6=pq3
       if l==0:
            res7.append(ts6)
       else:
            res7.append(ts6)
       l=l+1   

    print(res7)
    
    produdet=productdetails.objects.filter(product_number__in=res7).values_list('brand',flat=True).distinct()
    produdet2=productdetails.objects.filter(brand__in=produdet).values_list('product_number',flat=True).order_by('-product_number').distinct()
    produdet1=productdetails.objects.filter(brand__in=produdet).order_by('-product_number').distinct()[:6]
    prods1=product.objects.filter(product_number__in=produdet2).order_by('-product_number').distinct()[:6]
    produdet4=productdetails.objects.filter(product_number__in=res7).count()
    print("Products")
    print(prods1)
    print("Products Det")
    print(produdet1)
    #.annotate(name_count=Count('product_number')).filter(name_count__gte=1).distinct()
    cartt=cart.objects.filter(email=email).count()
    print("pagal Keta")
    print(produ)
    """  produ=orderdetails.objects.filter(product_number=pq1).annotate(name_count=Count('product_number')).filter(name_count__gte=1).values_list('product_number').exclude(email=email).distinct()
        if produ:
            ts4=produ
            if l==0:
                res5.append(ts4)
            else:
                res5.append(ts4)
            l=l+1  """   

    
    print("raag aleli madhuri")
    




    """ ts3=""
    res4=[]
    k=0
    print(getitem)
    for gi in getitem:
        pq1=gi.product_number
        print(pq1)
        print("my test")
        produ=product.objects.filter(product_number=pq1).values_list('subcatname',flat=True)
        ts3=produ
        if k==0:
            res4.append(ts3)
        else:
            res4.append(ts3)
        k=k+1    
    print(res4)
    print("bhukad ketaki") """
     

    #getor=orderdetails.objects.filter(order_id__in).exclude(email=email).all()
    
    return render(request,'homepage.html',{'fullname':fullname,'produdet4':produdet4,'cartt':cartt,'recprods1':prods1,'recprodudet1':produdet1,'reproducts':reproducts,'reproducts1':reproducts1,'reproducts2':reproducts2,'reproductdet':reproductdet,'reproductdet1':reproductdet1,'productssdet':productssdet,'productss':productss,'ad':ad,'records2':distinct2,'records1':distinct1,'records':distinct,'cat':cat,'subcat':subcat,'sessemail':sessemail})

def myprofile(request):
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    userdet=userdetails.objects.get(email=email)
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    if request.method == 'POST' and 'saveprof' in request.POST:
        personal=userdetails.objects.get(email=email)
        if request.POST.get('fullnamee'):
            personal.fullname=request.POST.get('fullnamee')
        if request.POST.get('emailid'):    
            personal.email=request.POST.get('emailid')
        if request.POST.get('gender'):    
            personal.gender=request.POST.get('gender')
        if request.POST.get('address'):     
            personal.address=request.POST.get('address')
        if request.POST.get('cont'): 
            personal.phonenumber=request.POST.get('cont')
        if request.POST.get('country'):     
            personal.country=request.POST.get('country')
        if request.POST.get('state'):    
            personal.state=request.POST.get('state')
        if request.POST.get('pincode'): 
            personal.pincode=request.POST.get('pincode')
        if request.POST.get('city'):  
            personal.city=request.POST.get('city')   
        personal.save()
    cartt=cart.objects.filter(email=email).count()
    return render(request,'myprofile.html',{'fullname':fullname,'cartt':cartt,'userdet':userdet,'records2':distinct2,'records1':distinct1,'records':distinct,'cat':cat,'subcat':subcat,'sessemail':sessemail})

def myorders(request):
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname


    userdet=userdetails.objects.get(email=email)
    orderdet=orderdetails.objects.filter(email=email).all().order_by('-ordered_date')
    orderdet1=orderdetails.objects.filter(email=email).count()
    #for ors in orderdet:
         #productss=product.objects.filter(product_number=ors.product_number)
    #productssdet=productdetails.objects.all()
    productss=product.objects.all()
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'myorders.html',{'fullname':fullname,'cartt':cartt,'productss':productss,'orderdet1':orderdet1,'orderdet':orderdet,'userdet':userdet,'records2':distinct2,'records1':distinct1,'records':distinct,'cat':cat,'subcat':subcat,'sessemail':sessemail})

def mywishlist(request):
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    if request.method == 'POST' and 'remove' in request.POST:
        if request.POST.get('pnum'):
            pnum=request.POST.get('pnum')
            instance = wishlist.objects.get(email=email,product_number=pnum)
            instance.delete()

    userdet=userdetails.objects.get(email=email)
    wishdet=wishlist.objects.filter(email=email).all().order_by('-created_date')
    wishdet1=wishlist.objects.filter(email=email).count()
    #for ors in orderdet:
         #productss=product.objects.filter(product_number=ors.product_number)
    #productssdet=productdetails.objects.all()
    productss=product.objects.filter(wishlist__email=email).all()
    productss1=product.objects.filter(wishlist__email=email).values_list('product_number',flat=True)
    prodett=productdetails.objects.filter(product_number__in=productss1)

    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'mywishlist.html',{'fullname':fullname,'cartt':cartt,'prodett':prodett,'productss':productss,'wishdet1':wishdet1,'wishdet':wishdet,'userdet':userdet,'records2':distinct2,'records1':distinct1,'records':distinct,'cat':cat,'subcat':subcat,'sessemail':sessemail})




def sliderfunc(request,pno):
    mycat=product.objects.get(product_number=pno)
    myrelate=productdetails.objects.get(product_number=pno)
    return redirect('/showproduct/'+str(mycat.catna)+'/'+str(mycat.subcatname)+'/'+str(myrelate.related_to))


def search(request):
    res=""
    res1=""
    sessemail=""
    text=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    if request.method=="POST" and 'searchbtn' in request.POST:
        if request.POST.get('searchtext'):
            text=request.POST.get('searchtext')
            data=productdetails.objects.filter(related_to__icontains=text).order_by('product_number').first()
            data1=product.objects.filter(product_name__icontains=text).order_by('product_number').first()
            data2=productdetails.objects.filter(brand__icontains=text).order_by('product_number').first()
            if data:
                res=data.product_number
                res1=data.related_to
                prod=product.objects.get(product_number=res)
                catname=prod.catna
                subcatname=prod.subcatname
                rev=searchitems.objects.filter(product_number=res,email=email)
                if 'name' in request.session:
                    if rev.count()<=0:
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()
                    elif rev.count()>0:
                        instance = searchitems.objects.get(email=email,product_number=res)
                        instance.delete()
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()
                return redirect('/showproduct/'+str(catname)+'/'+str(subcatname)+'/'+str(res1))
            elif data2:
                res=data2.product_number
                res1=data2.brand
                prod=product.objects.get(product_number=res)
                catname=prod.catna
                subcatname=prod.subcatname
                rev=searchitems.objects.filter(product_number=res,email=email)
                if 'name' in request.session:
                    if rev.count()<=0:
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()
                    elif rev.count()>0:
                        instance = searchitems.objects.get(email=email,product_number=res)
                        instance.delete()
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()



                return redirect('/showproduct/'+str(catname)+'/'+str(subcatname)+'/'+str(res1))    
            elif data1:
                res1=data1.product_number
                prod=product.objects.get(product_number=res1)
                catname=data1.catna
                subcatname=data1.subcatname
                rev=searchitems.objects.filter(product_number=res1,email=email)
                if 'name' in request.session:
                    if rev.count()<=0:
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()
                    elif rev.count()>0:
                        instance = searchitems.objects.get(email=email,product_number=res1)
                        instance.delete()
                        reviewed=searchitems()
                        reviewed.product_number=prod
                        reviewed.email=sessem
                        reviewed.save()
                return redirect('/showproduct/'+str(catname)+'/'+str(subcatname)+'/'+str(res1))
            
            else:
                mymsg="No results found for"
                distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
                distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
                distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
                cartt=cart.objects.filter(email=email).count()
                return render(request,'product.html',{'fullname':fullname,'cartt':cartt,'mymsg':mymsg,'records':distinct,'records1':distinct1,'records2':distinct2,'sessemail':sessemail,'text':text})
    


def showproduct(request,catname,subcatname,val):
    cat=category.objects.all()
    subcat = subcategory.objects.all()
   
    print(catname)
    print(subcatname)
    #catname=category.objects.get(catname=catname)
    #subcatname=category.objects.get(subcatname=subcatname)
    fullname=""
    sessemail=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    getprod=product.objects.filter(catna=catname,subcatname=subcatname).order_by('product_number')
    if val=="all":
        getproddet=productdetails.objects.all()
        print(getproddet)
        print("all")
    else:
        getproddet=productdetails.objects.filter(related_to=val).order_by('product_number')
        print("DIlli")
        if not getproddet:
            getproddet=productdetails.objects.filter(brand=val).order_by('product_number').all()
            print("silly")
            if not getproddet:
                getproddet=productdetails.objects.filter(product_number=val).order_by('product_number') 
                print("billy")
           
        print(getproddet)
        print("not all")
    getminprice=product.objects.filter(catna=catname,subcatname=subcatname).order_by('product_price').first()
    getmaxprice=product.objects.filter(catna=catname,subcatname=subcatname).order_by('product_price').last()
    
    request.session['sesscat']=catname
    request.session['sesssub']=subcatname

    
    colors={}
    type1={}
    brands={}
    sizes={}
    temp=[]
    temp1=[]
    temp2=[]
    temp3=[]

    res={}
    res2={}
    res3={}
    res4={}
    for pn in getprod:
         c=productdetails.objects.filter(product_number=pn.product_number).distinct()
         for cl in c:
           colors[pn.product_number]=cl.color
         for tp in c:
             type1[pn.product_number]=tp.type
         for bran in c:
             brands[pn.product_number]=bran.brand
         for siz in c:
             sizes[pn.product_number]=siz.size


    for key, val in colors.items():
        if val not in temp:
            temp.append(val)
            res[key] = val
    #colors=productdetails.objects.filter(product_number=getprod).values('color').distinct()
    for key, val in type1.items():
        if val not in temp1:
            temp1.append(val)
            res2[key] = val

    for key, val in brands.items():
        if val not in temp2:
            temp2.append(val)
            res3[key] = val

    for key, val in sizes.items():
        if val not in temp3:
            temp3.append(val)
            res4[key] = val
    
    print(colors)

    print(res)

    print("color")
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    records = productdetails.objects.filter(related_to__in=[item['related_to'] for item in distinct])
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'product.html',{'catname':catname,'fullname':fullname,'cartt':cartt,'records':distinct,'records1':distinct1,'records2':distinct2,'sizes':res4,'brands':res3,'type1':res2,'colors':res,'sesscat':request.session['sesscat'],'sesssub':request.session['sesssub'],'getminprice':getminprice,'getmaxprice':getmaxprice,'cat':cat,'subcat':subcat,'product':getprod,'sessemail':sessemail,'getdetail':getproddet})

def filter_data(request):
    sessemail=""
    sesscat=""
    sesssub=""
    colors=request.GET.getlist('color[]')
    type1=request.GET.getlist('types1[]')
    brands=request.GET.getlist('brands[]')
    sizes=request.GET.getlist('sizes[]')
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    if 'sesscat' in request.session:
        sesscat=request.session['sesscat']
    if 'sesssub' in request.session:
        sesssub=request.session['sesssub']
    print(sesscat)
	
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    #catname=category.objects.get(catname=catname)
    #subcatname=category.objects.get(subcatname=subcatname)
    getprod=product.objects.filter(catna=sesscat,subcatname=sesssub)
    getproddet=productdetails.objects.all()
    getminprice=product.objects.filter(catna=sesscat,subcatname=sesssub).order_by('product_price').first()
    getmaxprice=product.objects.filter(catna=sesscat,subcatname=sesssub).order_by('product_price').last()
    #sortprice=product.objects.filter(catna=sesscat,subcatname=sesssub)
    #print(sortprice)
    print("c u")
    
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']
    sortprice=request.GET['sortprice']
    print("now")
    print(sortprice)
    print(minPrice)
    print(maxPrice)
    print(getminprice)
    print(getmaxprice)
        
    allProducts=product.objects.all().order_by('-product_number').distinct()
    print(allProducts)
    allProducts=allProducts.filter(catna=sesscat,subcatname=sesssub,product_price__gte=minPrice)
    print(allProducts)
    allProducts=allProducts.filter(catna=sesscat,subcatname=sesssub,product_price__lte=maxPrice)
    print(allProducts)
    prdict={}
        
    for all in allProducts:

        getprodp=productdetails.objects.filter(product_number=all.product_number)
        for pdp in getprodp:
            disprice=int(all.product_price-(all.product_price*pdp.discount/100))
            prdict[pdp.product_number]=disprice
    print(prdict)
    if len(colors)>0:
        allProducts=allProducts.filter(productdetails__color__in=colors)
    if len(type1)>0:
        allProducts=allProducts.filter(productdetails__type__in=type1)
    if len(brands)>0:
        allProducts=allProducts.filter(productdetails__brand__in=brands)
    if len(sizes)>0:
        allProducts=allProducts.filter(productdetails__size__in=sizes)
    print(colors)
    print("Hey")
    print(allProducts)
    
    if sortprice == "High to Low":
       allProducts=allProducts.order_by('-minimum_price')  
    elif sortprice == "Low to High":
        allProducts=allProducts.order_by('minimum_price')   

    if allProducts:

        t=render_to_string('product-list.html',{'data':allProducts,'getdetail':prdict,'getproddet':getproddet})

        return JsonResponse({'data':t})
    else:
        mymsg1="No matches found"
       
        t=render_to_string('product-list.html',{'mymsg1':mymsg1})

        return JsonResponse({'data':t})

        #return render(request,'product.html',{'mymsg1':mymsg1,'records':distinct,'sessemail':sessemail})

def singleproduct(request,prodname):
    
    request.session['cnt']=0
    botchat="No"
    sessemail=""
    sessem=""
    email=""
    getp = product.objects.get(product_number=prodname)
    fullname=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
        rev=recentlyviewed.objects.filter(product_number=prodname,email=email)
        if rev.count()<=0:
            reviewed=recentlyviewed()
            reviewed.product_number=getp
            reviewed.email=sessem
            reviewed.save()
        elif rev.count()>0:
             instance = recentlyviewed.objects.get(email=email,product_number=prodname)
             instance.delete()
             reviewed=recentlyviewed()
             reviewed.product_number=getp
             reviewed.email=sessem
             reviewed.save()


    cat=category.objects.all()
    subcat = subcategory.objects.all()
    #getprod = product.objects.filter(product_number=prodname)
    
   # getproddetail=productdetails.objects.filter(product_number=prodname)
    getproddet=productdetails.objects.get(product_number=prodname)
    
    #context={'getproddetail':getproddetail}
    disprice=int(getp.product_price-(getp.product_price*getproddet.discount/100))
    
    instance=chatmessages.objects.all()
    try:

        instance = chatmessages.objects.get(sender=email,receiver=email)
    except chatmessages.DoesNotExist:
        instance.delete()
    exist="no"
    cartd=cart.objects.filter(email=email,product_number=getp,negotiation_status="Not negotiated") 
    if cartd:
        exist="exist"
        print(exist)
        print("hhhh")
    proddu=productdetails.objects.all()
    prcat=product.objects.filter(subcatname=getp.subcatname,productdetails__related_to=getproddet.related_to).exclude(product_number=prodname).order_by('-product_number').distinct()[:4]
    prcat1=product.objects.filter(subcatname=getp.subcatname,productdetails__related_to=getproddet.related_to).exclude(product_number=prodname).order_by('-product_number').distinct()[4:8]
    prcat2=product.objects.filter(productdetails__brand=getproddet.brand).exclude(subcatname=getp.subcatname,product_number=prodname).order_by('-product_number').distinct()[:4]
    prcat3=product.objects.filter(productdetails__brand=getproddet.brand).exclude(subcatname=getp.subcatname,product_number=prodname).order_by('-product_number').distinct()[4:8]
    #to disable arrows
    prcatd1=product.objects.filter(subcatname=getp.subcatname,productdetails__related_to=getproddet.related_to).exclude(product_number=prodname).count()
    prcatd2=product.objects.filter(productdetails__brand=getproddet.brand).exclude(subcatname=getp.subcatname,product_number=prodname).count()
    interestin3=""
    
    i=0
    orid=orderdetails.objects.filter(product_number=prodname).all()
    ts1=""
    res2=[]
    
    for orii in orid:
        pq1=orii.order_id
        ts1=pq1
        if i==0:
            res2.append(ts1)
        else:
            res2.append(ts1)
        i=i+1    
    print(res2)
    print("demo")
    prcat4=orderdetails.objects.filter(order_id__in=res2).values_list('product_number',flat=True).exclude(product_number=prodname).distinct().all()
    print(prcat4)
    ts2=""
    res3=[]
    j=0
    for pc4 in prcat4:
        pq2=pc4
        ts2=pq2
        if j==0:
            res3.append(ts2)
        else:
            res3.append(ts2)
        j=j+1   

    interestin3=product.objects.filter(product_number__in=res3,catna=getp.catna)[:4]
    interestind1=product.objects.filter(product_number__in=res3,catna=getp.catna).count()
    interestin4=product.objects.filter(product_number__in=res3,catna=getp.catna)[5:9]
    print(interestin3)
    interestin = productdetails.objects.filter(related_to=getproddet.related_to).exclude(product_number=prodname).order_by('product_number')[:4]
  
    interestin1 = productdetails.objects.filter(related_to=getproddet.related_to).exclude(product_number=prodname).order_by('product_number')[4:8]
    

    #interestin1 = productdetails.objects.filter(related_to= getproddet.related_to).exclude(product_number=prodname).order_by('product_number')[5:9]
    print(interestin)
    print(prcat)
    print("prcat")
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    if request.method == 'POST' and 'wishlist' in request.POST:
        #personal=userdetails()
        wl=wishlist()
        wldata=wishlist.objects.filter(email=email,product_number=prodname)
        if wldata.count()<=0:
            wl.email=sessem
            wl.product_number=getp
            wl.save()
    cartt=cart.objects.filter(email=email).count()
    myreviewss=reviews.objects.filter(product_number=getp)
    myreviewss1=reviews.objects.filter(product_number=getp).values_list('email',flat=True).distinct()
    myreviewsscount=reviews.objects.filter(product_number=getp).count()
    res4=[]
    k=0
    ts3=""
    for pc5 in myreviewss1:
        pq3=pc5
        ts3=pq3
        print("hiss")
        print(ts3)
        if k==0:
            res4.append(ts3)
        else:
            res4.append(ts3)
        k=k+1   
    print(res4)
    usdet=userdetails.objects.filter(email__in=res4).all()
    avgreview=reviews.objects.filter(product_number=getp).aggregate(Avg('stars'))
    ar=avgreview['stars__avg']
   
    print(ar)
    return render(request,'productdetails.html',{'avgreview':ar,'usdet':usdet,'myreviewsscount':myreviewsscount,'myreviewss':myreviewss,'fullname':fullname,'interestind1':interestind1,'prcatd1':prcatd1,'prcatd2':prcatd2,'cartt':cartt,'interestin4':interestin4,'interestin3':interestin3,'prcat':prcat,'prcat1':prcat1,'prcat2':prcat2,'prcat3':prcat3,'interestin1':interestin1,'proddu':proddu,'interestin':interestin,'records':distinct,'records1':distinct1,'records2':distinct2,'exist':exist,'botchat':botchat,'count':request.session['cnt'],'cat':cat,'subcat':subcat,'product':getp,'getdetail':getproddet,'disprice':disprice,'sessemail':sessemail})    

def mycart(request,prodnum,neg):
    exist="no"
    getprods=product.objects.get(product_number=prodnum)
    getproddet=productdetails.objects.get(product_number=prodnum)
    disprice=int(getprods.product_price-(getprods.product_price*getproddet.discount/100))
    print(disprice)
    current_time = datetime.now() 
    cid=str('C')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
    sessemail=""
    sessem=""
    email=""
    fullname=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    today = date.today()
    try:
        cartdet=cart()
        #userd=userdetails.objects.get(fullname=sessemail)
        email=userdetails.objects.get(email=sessemail)
        #cartd=
        sessem=email.email
        cartdet.email=email
        cartdet.product_number=getprods           
        cartd=cart.objects.get(email=email,product_number=getprods,negotiation_status=neg) 
        if cartd:
            exist="exist"
            print(exist)
            print("hhhh")
        else:
            cartdet.discount_price=disprice
            print(disprice)
            print("doesnt")
            cartdet.negotiation_status="Not negotiated"
            cartdet.cart_id=cid
            cartdet.quantity=1
            cartdet.save()
    except cart.DoesNotExist:
        cartdet.discount_price=disprice
        print(disprice)
        print("doesnt")
        cartdet.negotiation_status="Not negotiated"
        cartdet.cart_id=cid
        cartdet.quantity=1
        cartdet.save()
    cartdata=cart.objects.all()
    proddet=product.objects.all()
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    getproddet=productdetails.objects.all()
    #disprice=int(getprods.product_price-(getprods.product_price*getproddet.discount/100))
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'cart.html',{'fullname':fullname,'cartt':cartt,'records':distinct,'records1':distinct1,'records2':distinct2,'exist':exist,'getproddet':getproddet,'sessemail':sessemail,'cartdata':cartdata,'proddet':proddet,'cat':cat,'subcat':subcat,'sessem':sessem})  

def mycarts(request,prodnumb,carid,quant):
    getprods=product.objects.get(product_number=prodnumb)
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    
        cartdet=cart()
        #userd=userdetails.objects.get(fullname=sessemail)
        email=userdetails.objects.get(email=sessemail)
        #cartd=
        sessem=email.email
        cartdet.email=email         
        cartd=cart.objects.get(email=email,product_number=getprods,cart_id=carid)
        cartd.quantity=quant
       
    cartd.save()
    cartdata=cart.objects.all()
    proddet=product.objects.all()
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    getproddet=productdetails.objects.all()
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'cart.html',{'fullname':fullname,'cartt':cartt,'records':distinct,'records1':distinct1,'records2':distinct2,'getproddet':getproddet,'sessemail':sessemail,'cartdata':cartdata,'proddet':proddet,'cat':cat,'subcat':subcat,'sessem':sessem})  


def deleteitemcart(request,prodnumber,carid):
    getprods=product.objects.get(product_number=prodnumber)
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    sessem=""
    email=""
    sessemail=""
    fullname=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname

    cartdet=cart()
        #userd=userdetails.objects.get(fullname=sessemail)
    email=userdetails.objects.get(email=sessemail)
        #cartd=
    sessem=email.email
    cartdet.email=email         
    instance = cart.objects.get(email=email,product_number=getprods,cart_id=carid)
    instance.delete()

    cartdata=cart.objects.all()
    proddet=product.objects.all()
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    getproddet=productdetails.objects.all()
    cartda=cart.objects.filter(email=sessem)
    if cartda.count()<=0:
         return redirect('/gotocart')
    cartt=cart.objects.filter(email=email).count()
    return render(request,'cart.html',{'fullname':fullname,'cartt':cartt,'records':distinct,'records1':distinct1,'records2':distinct2,'getproddet':getproddet,'sessemail':sessemail,'cartdata':cartdata,'proddet':proddet,'cat':cat,'subcat':subcat,'sessem':sessem})  

def checkout(request):
    sesspre=""
    sessosum=""
    today = date.today()
    if request.method == 'POST' and 'personal' in request.POST:
        #personal=userdetails()
        personal=userdetails.objects.get(email=request.POST.get('emailid'))
        personal.fullname=request.POST.get('fullname')
        personal.email=request.POST.get('emailid')
        personal.address=request.POST.get('address')
        personal.phonenumber=request.POST.get('contact')
        personal.country=request.POST.get('country')
        personal.state=request.POST.get('state')
        personal.pincode=request.POST.get('pincode') 
        personal.city=request.POST.get('city')   
        personal.save()
        request.session["predetails"]="filled"
        request.session["osum"]="pfilled"
    if 'predetails' in request.session:
        sesspre=request.session['predetails']
        sessosum=request.session['osum']
    fullname=""
    sessemail=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    if request.method == 'POST' and 'confirmorder' in request.POST:
        request.session["osum"]="filled"
        if 'osum' in request.session:
            sessosum=request.session['osum']
       # try:
    if request.method == 'POST' and 'creditcard' in request.POST:
        cts=cart.objects.filter(email=sessem)
        current_time = datetime.now() 
        oid=str('O')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
        request.session['orderid']=oid
        for ct in cts:
            od=orderdetails()
            od.email=sessem
            od.product_number=ct.product_number
            od.size=1
            od.quantity=ct.quantity
            od.order_id=oid
            od.order_status="Y"
            od.discount_price=ct.discount_price
            od.negotiation_status=ct.negotiation_status
            od.save()
        current_time = datetime.now() 
        pid=str('P')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
        pay=paymentdetails()
        pay.payment_id=pid
        pay.email=sessem
        pay.order_id=oid
        pay.payment_mode="Credit Card"
        pay.amount_paid=request.POST.get('amount')
        pay.save()
        for delc in cts :
            delc.delete()
        
        # proddet1=product.objects.all()
        # getproddet1=productdetails.objects.all()
        # userdetails1=userdetails.objects.all()
        # if "predetails" in request.session.keys() or "osum" in request.session.keys():
        if 'predetails' in request.session:
            del request.session["predetails"]
        if 'osum' in request.session:
            del request.session["osum"]
        try:
            send_mail("Order Confirmation for Order no: "+str(oid), "Hi "+str(fullname)+",\nYour Order has been successfully placed.Your order will be delivered within 2 days.\nThanks for Shopping with Minics", "siescoms2019@gmail.com", [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/receipt')
        
        

    if request.method == 'POST' and 'cod' in request.POST:
        cts=cart.objects.filter(email=sessem)
        current_time = datetime.now() 
        oid=str('O')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
        request.session['orderid']=oid
        
        for ct in cts:
            od=orderdetails()
            od.email=sessem
            od.product_number=ct.product_number
            od.size=1
            od.quantity=ct.quantity
            od.order_id=oid
            od.order_status="Y"
            od.discount_price=ct.discount_price
            od.negotiation_status=ct.negotiation_status
            od.save()
        current_time = datetime.now() 
        pid=str('P')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
        
        pay=paymentdetails()
        pay.payment_id=pid
        pay.email=sessem
        pay.order_id=oid
        pay.payment_mode="COD"
        pay.amount_paid=request.POST.get('amount')
        pay.save()
        for delc in cts :
            delc.delete()
        # proddet1=product.objects.all()
        # getproddet1=productdetails.objects.all()
        # userdetails1=userdetails.objects.all()
        # if "predetails" in request.session.keys() or "osum" in request.session.keys():
        if 'predetails' in request.session:
            del request.session["predetails"]
        if 'osum' in request.session:
            del request.session["osum"]
        #return render(request,"receipt.html",{'proddet1':proddet1,'getproddet1':getproddet1,'userdetails1':userdetails1})
        try:
            send_mail("Order Confirmation for Order no: "+str(oid), "Hi "+str(fullname)+",\nYour Order has been successfully placed.Your order will be delivered within 2 days.\nThanks for Shopping with Minics", "siescoms2019@gmail.com", [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('/receipt')
        #instance = cart.objects.get(email=sessem)
        #instance.delete()
        
    details=userdetails.objects.get(email=email)   
    carts=cart.objects.all()
    proddet=product.objects.all()
    getproddet=productdetails.objects.all()
    
    return render(request,'checkout.html',{'fullname':fullname,'perdetails':sesspre,'osum':sessosum,'detail':details,'sessemail':sessemail,'carts':carts,'proddet':proddet,'getproddet':getproddet,'sessem':sessem})

def receipt(request):
    proddet1=product.objects.all()
    getproddet1=productdetails.objects.all()
    sessemail=""
    orderid=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    
    if 'orderid' in request.session:
        orderid=request.session['orderid']

    orderdetails1=orderdetails.objects.filter(order_id=orderid)
    payment1=paymentdetails.objects.filter(order_id=orderid)   
    
    userdetails1=userdetails.objects.get(email=sessemail)
     
    return render(request,'receipt.html',{'fullname':fullname,'sessorderid':orderid,'proddet1':proddet1,'getproddet1':getproddet1,'userdetails1':userdetails1,'orderdetails1':orderdetails1,'payment1':payment1,'sessname':sessemail,'sessem':sessem})

def register(request):
    if request.method == 'POST' and 'register' in request.POST:
        if request.POST.get('full_name') and request.POST.get('your_email') and request.POST.get('password') and request.POST.get('comfirm_password'):
            if request.POST.get('password') == request.POST.get('comfirm_password'):
                post=userdetails()
                post.fullname= request.POST.get('full_name')
                post.email= request.POST.get('your_email')
                post.password= request.POST.get('password')
                post.save()
                cat=category.objects.all()
                subcat = subcategory.objects.all()
                return render(request, 'user_register.html')  
            

    elif request.method == 'POST' and 'login' in request.POST:
        if request.POST.get('your_email_1') and request.POST.get('password_1'):
            getuser=userdetails.objects.filter(email=request.POST.get('your_email_1'),password=request.POST.get('password_1')).exists()
            if getuser:
                getuser=userdetails.objects.get(email=request.POST.get('your_email_1'),password=request.POST.get('password_1'))
                request.session['name'] = getuser.email

                message="successfully logged in"
                cat=category.objects.all()
                subcat = subcategory.objects.all()
                distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
                distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
                distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
                productssdet=productdetails.objects.all()
                productss=product.objects.all()
                ad=advertisement.objects.filter().order_by('-id')[:4]
                return redirect('/')
                #return render(request,'homepage.html',{'productssdet':productssdet,'productss':productss,'ad':ad,'records':distinct,'records1':distinct1,'records2':distinct2,'cat':cat,'subcat':subcat,'messages':message,'sessemail':request.session['name']}) 
            else:
                message="failed"
                return render(request,'user_register.html',{'messages':message})
    else:

        return render(request,'user_register.html')

def greeting():
    IST = pytz.timezone('Asia/Kolkata')
    greet=datetime.now(IST).hour
    #print(greet)
    if greet >=6 and greet<12:
        greetmorng="Good Morning ! Have a great day ahead"
        return greetmorng
    elif greet >=12 and greet<18:
        greetaftern="Good Afternoon!"
        return greetaftern
    elif greet >=18 and greet<20:
        greetevening="Good Evening"
        return greetevening
    else:
        greetnight="Have a pleasent Night!"
        return greetnight        

def negotiate(request,prodnumber):
   
    textstatus=""
    userprice=0
    cnt=0
    approval=""
    myprice=""
    temp=""
    botchat="Yes"
    finalprice=""
    gotocart="no"
    if 'myprice' in request.session:
        myprice=request.session['myprice']
    if 'temp' in request.session:
        temp=request.session['temp']
    if 'finalprice' in request.session:
        finalprice=request.session['finalprice']
    if 'userprice' in request.session:
        userprice=request.session['userprice']
    today = date.today()
    
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    #getprod = product.objects.filter(product_number=prodname)
    getp = product.objects.get(product_number=prodnumber)
   # getproddetail=productdetails.objects.filter(product_number=prodname)
    getproddet=productdetails.objects.get(product_number=prodnumber)
    #context={'getproddetail':getproddetail}
    disprice=int(getp.product_price-(getp.product_price*getproddet.discount/100))
    chatmsg=chatmessages.objects.all().order_by('id')
    cartdata=cart.objects.all()
    fullname=""
    sessem=""
    sessemail=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    if 'cnt' in request.session:
        cnt=request.session['cnt']
    
    cartd1=cart.objects.filter(email=email,product_number=getp,created_date=today.isoformat(),negotiation_status="negotiated")
    if cartd1:
        gotocart="yes"
        if cnt==0:
            grt=greeting()
            msgdata=chatmessages()
            msgdata.sender="chatbot"
            msgdata.receiver=email
            msgdata.message=grt
            msgdata.save()
            msgdata1=chatmessages()
            msgdata1.sender="chatbot"
            msgdata1.receiver=email                      
            msgdata1.message="You have already negotiated for this product today and your item is already existing in the cart"
            msgdata1.save()
            textstatus="no"
            approval="no"
            gotocart="yes"
            request.session['cnt']=cnt+1
        if request.method=="POST" and 'gotcart' in request.POST:
          return redirect('/gotocart')
    else:
        if cnt==0:
            grt=greeting()
            msgdata=chatmessages()
            msgdata.sender="chatbot"
            msgdata.receiver=email
            msgdata.message=grt
            msgdata.save()
            msgdata1=chatmessages()
            msgdata1.sender="chatbot"
            msgdata1.receiver=email                      
            msgdata1.message="Please quote your price"
            msgdata1.save()
            textstatus="yes"
            approval="no"
            request.session['cnt']=cnt+1
            print("greet")

        if cnt>=5:
            
            textstatus="no"
            approval="yes"
            print("cnt>5")
        
        #quoteoffer
        if request.method=="POST" and 'makeanoffer' in request.POST:
            if cnt>5:
                if request.POST.get('price'):
                    userprice=int(request.POST.get('price'))
                    request.session['userprice']=userprice
                    msgdata=chatmessages()
                    msgdata.sender=email
                    msgdata.receiver="chatbot"                     
                    msgdata.message="Offer submitted ₹"+str(userprice)
                    msgdata.save()
                    if userprice < getp.minimum_price:
                        msgdata=chatmessages()
                        msgdata.sender="chatbot"
                        msgdata.receiver=email                    
                        msgdata.message="Sorry your offered price is below than our cost, how does ₹"+str(finalprice)+" sounds to you? This is the last price to accept, afterwards you would not be elibible to negotiate"
                        msgdata.save()
                        textstatus="no"
                        approval="yes"
                        print("userprice<getp")
                    elif userprice >= disprice:
                        msgdata=chatmessages()
                        msgdata.sender="chatbot"
                        msgdata.receiver=email                    
                        msgdata.message="Your price seems to be greater than or equal to our discount price, please offer your price again.."
                        msgdata.save()
                        textstatus="yes"
                        approval="no"
                        print("userprice>disprice")
                        if cnt<=1:
                            request.session['cnt']=1
                            print("cnt<=1")
                        else:   
                            request.session['cnt']=cnt-1
                            print("cnt<=1 else")
                
            else:    
                if request.POST.get('price'):
                    userprice=int(request.POST.get('price'))
                    request.session['userprice']=userprice
                    msgdata=chatmessages()
                    msgdata.sender=email
                    msgdata.receiver="chatbot"                     
                    msgdata.message="Offer submitted ₹"+str(userprice)
                    msgdata.save()  
                    msgdata1=chatmessages()
                    msgdata1.sender="chatbot"
                    msgdata1.receiver=email                      
                    msgdata1.message="Thank you for your offer, now i need to get a quick approval from my boss. It will take a few seconds.BRB"
                    msgdata1.save()
                    myprice=int(disprice-getp.minimum_price)
                    temp=int(random.randint(1,myprice))
                    finalprice=int(disprice-temp)
                    request.session['myprice']=myprice
                    request.session['temp']=temp
                    request.session['finalprice']=finalprice
                    if userprice < disprice and userprice > getp.minimum_price:
                        textstatus="no"
                        approval="yes"
                        msgdata2=chatmessages()
                        msgdata2.sender="chatbot"
                        msgdata2.receiver=email                      
                        msgdata2.message="Hey there your offer is approved by our boss, would you like to confirm this price"
                        msgdata2.save()
                    elif userprice>=disprice:    
                        textstatus="yes"
                        approval="no"
                        msgdata2=chatmessages()
                        msgdata2.sender="chatbot"
                        msgdata2.receiver=email                      
                        msgdata2.message="Your price seems to be greater than or equal to our discount price, please offer your price again.."
                        msgdata2.save()
                        if cnt<=1:
                            request.session['cnt']=1
                            print("lala")
                        else:   
                            request.session['cnt']=cnt-1
                            print("haha")
                    else:
                        textstatus="yes"  
                        approval="no"
                        msgdata2=chatmessages()
                        msgdata2.sender="chatbot"
                        msgdata2.receiver=email                      
                        msgdata2.message="I can't get approval from my boss with an offer that low.Could you try a higher amount?"
                        msgdata2.save()
                        request.session['cnt']=cnt+1  
                        print("lol")  
            
        if request.method=="POST" and 'no' in request.POST:
            if cnt>5:
                textstatus="no"  
                approval="no"
                msgdata4=chatmessages()
                msgdata4.sender=email
                msgdata4.receiver="chatbot"                     
                msgdata4.message="Disagree this price"
                msgdata4.save()
                msgdata3=chatmessages()
                msgdata3.sender="chatbot"
                msgdata3.receiver=email                   
                msgdata3.message="Sorry the offered price by you is below than our cost price, we cannot sell our product to that rate, thank you"
                msgdata3.save()

            else:
                textstatus="yes"  
                approval="no"
                msgdata3=chatmessages()
                msgdata3.sender=email
                msgdata3.receiver="chatbot"                     
                msgdata3.message="Disagree this price"
                msgdata3.save()
                msgdata4=chatmessages()
                msgdata4.sender="chatbot"
                msgdata4.receiver=email                    
                msgdata4.message="Please quote a new price"
                msgdata4.save()
                request.session['cnt']=cnt+1
    

        if request.method=="POST" and 'approve' in request.POST:
            current_time = datetime.now() 
            cid=str('C')+str(current_time.year)+str(current_time.month)+str(current_time.day)+str(random.randint(1,100))
            if cnt>5:
                textstatus="no"  
                approval="no"
                gotocart="yes"
                msgdata3=chatmessages()
                msgdata3.sender="chatbot"
                msgdata3.receiver=email                     
                msgdata3.message="Your offer has been approved of ₹"+str(finalprice)
                msgdata3.save()
                neg1=negotiationdetails()
                neg1.email=sessem
                neg1.product_number=getp
                neg1.negotiated_price=finalprice
                neg1.save()
                crt=cart()
                crt.email=sessem
                crt.product_number=getp
                crt.quantity=1
                crt.discount_price=finalprice
                crt.negotiation_status="negotiated"
                crt.cart_id=cid
                crt.save()
                return redirect('/gotocart')
            else:
                textstatus="no"  
                approval="no"
                gotocart="no"
                msgdata3=chatmessages()
                msgdata3.sender="chatbot"
                msgdata3.receiver=email                     
                msgdata3.message="Your offer has been approved of ₹"+str(userprice)
                msgdata3.save()
                neg1=negotiationdetails()
                neg1.email=sessem
                neg1.product_number=getp
                neg1.negotiated_price=userprice
                neg1.save()
                crt=cart()
                crt.email=sessem
                crt.product_number=getp
                crt.quantity=1
                crt.discount_price=userprice
                crt.negotiation_status="negotiated"
                crt.cart_id=cid
                crt.save()
                return redirect('/gotocart')

        if cnt>=1 and cnt<=5 and request.method != "POST":
            textstatus="yes"  
            approval="no"
           
        
         
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    cartt=cart.objects.filter(email=email).count()
    return render(request,'productdetails.html',{'fullname':fullname,'cartt':cartt,'records':distinct,'records2':distinct2,'records1':distinct1,'gotocart':gotocart,'botchat':botchat,'approval':approval,'userprice':userprice,'textstatus':textstatus,'email':email,'chatmsg':chatmsg,'count':cnt,'cat':cat,'subcat':subcat,'product':getp,'getdetail':getproddet,'disprice':disprice,'sessemail':sessemail})    

def gotocart(request):
    distinct = productdetails.objects.values('related_to').annotate(name_count=Count('related_to')).filter(name_count__gte=1)
    distinct1 = product.objects.values('product_name').annotate(name_count=Count('product_name')).filter(name_count__gte=1)
    distinct2 = productdetails.objects.values('brand').annotate(name_count=Count('brand')).filter(name_count__gte=1)
    if 'name' not in request.session:
        return render(request,'emptycart.html',{'records':distinct,'records2':distinct2,'records1':distinct1})

    cartdata=cart.objects.all()
    proddet=product.objects.all()
    cat=category.objects.all()
    subcat = subcategory.objects.all()
    getproddet=productdetails.objects.all()
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    cartda=cart.objects.filter(email=sessem)
    if cartda.count()<=0:
         return render(request,'emptycart.html',{'fullname':fullname,'records':distinct,'sessemail':sessemail,'sessem':sessem,'records2':distinct2,'records1':distinct1})
    
    cartt=cart.objects.filter(email=email).count()
    return render(request,'cart.html',{'fullname':fullname,'cartt':cartt,'records2':distinct2,'records1':distinct1,'records':distinct,'getproddet':getproddet,'sessemail':sessemail,'cartdata':cartdata,'proddet':proddet,'cat':cat,'subcat':subcat,'sessem':sessem})  
def review(request):
    sessemail=""
    fullname=""
    sessem=""
    email=""
    if 'name' in request.session:
        sessemail=request.session['name']
        sessem=userdetails.objects.get(email=sessemail)
        email=sessem.email
        fullname=sessem.fullname
    pnum=""
    if request.method=="POST" and 'reviewbtn' in request.POST:
            if request.POST.get('myrating') and request.POST.get('suggestions'):
                stars=int(request.POST.get('myrating'))
                prnum=request.POST.get('prnum')
                pnum=product.objects.get(product_number=prnum)
                print("REVIEW")
                print(pnum)
                print(stars)

                suggestions=request.POST.get('suggestions')
                print(suggestions)
                review=reviews()
                review.product_number=pnum
                review.email=sessem
                review.stars=stars
                review.suggestion=suggestions
                review.save()
    return redirect('/singleproduct/'+str(pnum))         
                

        
def logout(request):
    if "name" in request.session.keys():
        del request.session["name"]
        if "predetails" in request.session.keys() or "osum" in request.session.keys():
            del request.session["predetails"]
            del request.session["osum"]
        
    return redirect("/")
    
   
    
       
