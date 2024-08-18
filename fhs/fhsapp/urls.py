from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('logout',views.logout,name='logout'),
    path("delete/<int:eid>", views.delete, name="delete"),
    path('ad',views.admin,name="admin"),
    path('addma', views.addma, name="addma"),
    path('adres', views.adres, name="adres"),
    path('viewcus', views.viewcus, name="viewcus"),
    path('viewma', views.viewma, name="viewma"),
    path('viewres',views.viewres,name="viewres"),
    path('cus',views.cus,name="cus"),
    path('cart', views.cart, name="cart")

    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


