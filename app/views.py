from django.shortcuts import render,redirect
from django.views import View
from . models import *
from django.db.models import Q



class ProductView(View):
 def get(self,request):
  mobile = Product.objects.filter(category="M")
  laptop = Product.objects.filter(category="L")
  topwear = Product.objects.filter(category="TW")
  bottomwear = Product.objects.filter(category="BW")
  print(bottomwear)
  return render(request,"app/home.html",
                {
                 "mobile":mobile,
                 "laptop":laptop,
                 "topwear":topwear,
                 "bottomwear":bottomwear
                },)

class ProductDetailView(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        item_alredy_in_cart = False
        if request.user.is_authenticated:
            item_alredy_in_cart=Cart.objects.filter(
            Q(product=product.id)& Q(user = request.user)
              ).exists()
            return render(request,"app/productdetail.html",{"product":product,"item_alredy_in_cart":item_alredy_in_cart})    
        else:
            return render(request,"app/productdetail.html",{"product":product,"item_alredy_in_cart":item_alredy_in_cart})




    

# def home(request):
#  return render(request, 'app/home.html')

# def add_to_cart(request):
#  user = request.user
#  product_id = request.GET.get("prod_id")
#  product = Product.objects.get(id=product_id)
#  Cart(user=user,product=product).save()
#  return redirect("/cart")
        
# def minus_cart(request):
#   if request.method =="GET":
#     prod_id = request.get['pord_id']




# def remove_cart(request):
#   if request.method =="POST":
#     prod_id = request.GET["prod_id"]
#     c = Cart.objects.get(Q(product=prod_id)&Q(User=request.user))
#     c.delete()
#     amount =0.0
#     shopping_amount =70.0
#     cart_product = [p for p in Cart.objects,all()]
        



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')