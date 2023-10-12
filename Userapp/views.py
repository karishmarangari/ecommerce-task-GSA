from django.shortcuts import render, redirect
from Adminapp.models import Product, MyCart
from django.contrib import messages
from datetime import datetime
import random

# Create your views here.
def Index(request):
    item = Product.objects.all()
    return render(request, "Indexpage.html", {"item":item})



def Productdetail(request, id):
    id = Product.objects.get(id=id)
    (discount) = int(((id.price)-(id.price)*0.4))
    return render(request, "Productdetail.html", {"id":id, "discount":discount})



def ViewCart(request):
    if(request.method == "POST"):
        productid = request.POST["productid"]
        qty = request.POST["qty"]
        prod = Product.objects.get(id = productid)
        #check for duplicate entry
        try:
            cart = MyCart.objects.get(product=prod)
        except:
            cart = MyCart()
            cart.product = prod
            cart.qty = qty
            cart.save()
            messages.success(request, "Product added successfully")
        else:
            pass
        return redirect(showCart)
        
            


def showCart(request):
    if(request.method == "GET"):
        cartitem = MyCart.objects.all()
        count = 0
        total = 0
        discounts = 0
        for item in cartitem:
            count += 1
            total += (item.product.price)*(item.qty)
            discounts += int(((item.product.price)-(item.product.price*40)//100)*(item.qty))
        request.session["count"] = count
        request.session["discount"] = discounts
        return render(request, "ViewCart.html", {"items":cartitem,"count":count,"total":total})
    else:
        id = request.POST["productid"]
        product = Product.objects.get(id=id)
        item = MyCart.objects.get(product=product)
        qty = request.POST["qty"]
        item.qty = qty
        item.save()
        return redirect(showCart)


def removeItem(request):
    id = request.POST["productid"]
    prod = Product.objects.get(id=id)
    item = MyCart.objects.get(product=prod)
    item.delete()
    return redirect(showCart)


def search(request):

    query = request.POST["query"]
    prodname = Product.objects.filter(p_name__icontains=query)
    prodprice = Product.objects.filter(price__icontains=query)
    searchreci = prodname.union(prodprice)
    return render(request, "search.html", {"searchreci":searchreci, "query":query})

