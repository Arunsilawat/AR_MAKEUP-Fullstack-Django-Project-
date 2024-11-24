from django.shortcuts import render,redirect
from .models import ItemInfo
from .forms import ItemInfoForm
# Create your views here.

# import razorpay
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    data = ItemInfo.objects.all()
    return render(request,'home.html',{'data':data})

def datapost(request):
    if request.method=="POST":
        form = ItemInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        data = ItemInfo.objects.all()
        return render(request,'datapost.html',{'form':form,'data':data})
    form = ItemInfoForm()
    data = ItemInfo.objects.all()
    if data:
        return render(request,'datapost.html',{'form':form,'data':data})
    else:
        return render(request,'datapost.html',{'form':form})
def addtocard(request,pk):
    if request.method == 'POST':
        quantity = request.session.get('quantity', [])
        quantity1 =int(request.POST.get('quantity'))
        quantity.append(quantity1)
        # print("quantity :",quantity)
        request.session['quantity'] = quantity
        cart = request.session.get('cart', [])
        cart.append(pk)
        request.session['cart'] = cart
        # form = ItemInfoForm()
        data = ItemInfo.objects.all()
        return render(request,'home.html',{ 'data':data})
def cart(request):
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    # print("Cart :",cart)
    # print("Quantity :",quantity)
    # print(len(cart))
    alldata = []
    i=0
    j=0
    total=0
    while i < len(cart):
        data = ItemInfo.objects.get(id=cart[i])
        total = total + (data.item_price)*quantity[j]
        # print(data.id)
        # print(data.iten_name)
        # print(data.item_desc)
        # print(data.item_price)
        # print(data.item_image)
        alldata.append({
            'id':data.id,
            'iten_name':data.iten_name,
            'item_details':data.item_details,
            'item_price':data.item_price,
            'item_image':data.item_image,
            'item_quantity':quantity[j]
        })
        i+=1
        j+=1
    # print("Total Amount = ",total)
    # print(alldata)
    return render(request,'cart.html',{'key':alldata,'amount':total})
def deletecart(request,pk):
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
 
    x = cart.index(pk)
    # print("Cart index no:",x)
    # y = quantity[x]
    # print("Quantity of that card index:",y)
    cart1=[]
    y = len(cart)   
    i=0
    while i<y:
        if i==x:
            pass
        else:
            cart1.append(cart[i])
        i+=1
    request.session['cart']=cart1
    quantity1=[]
    z = len(quantity)
    j=0
    while j<z:
        if j==x:
            pass
        else:
            quantity1.append(quantity[j])
        j+=1
    request.session['quantity']=quantity1
    # ----------------------------------------------------
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    # print(len(cart))
    alldata = []
    i=0
    j=0
    total=0
    while i < len(cart):
        data = ItemInfo.objects.get(id=cart[i])
        total = total + (data.item_price)*quantity[j]
        # print(data.id)
        # print(data.item_name)
        # print(data.item_desc)
        # print(data.item_price)
        # print(data.item_image)
        alldata.append({
            'id':data.id,
            'iten_name':data.iten_name,
            'item_details':data.item_details,
            'item_price':data.item_price,
            'item_image':data.item_image,
            'item_quantity':quantity[j]
        })
        i+=1
        j+=1
    # print("Total Amount = ",total)
    return render(request,'cart.html',{'key':alldata,'amount':total})
def details(request,pk):
    data=ItemInfo.objects.get(id=pk)
    return render(request,'details.html',{'data':data})