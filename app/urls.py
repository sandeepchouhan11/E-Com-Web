from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import(
#     loginForm,
#     MyPasswordChangeForm,
#     MyPasswordResetForm,
#     MySetPasswordForm
# )
urlpatterns = [
    # path('', views.home),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name="product-detail"),  
    path('',views.ProductView.as_view(),name="home"),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    
    path('piuscart/', views.buy_now, name='buy-now'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    # path(
    #     "acount/login/",
    #     auth_views.Loginview.as_view(
    #         template_name="app/login.html",authentication_form=LoginForm
    #     ),
    #     name="ligin",
    # ),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)