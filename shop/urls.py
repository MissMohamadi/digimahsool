
from django.urls import path
from .views import helloworld,FreeDelivery,NewYear,Bellow200,JanebiPc,Behdashti,NewTechnology,PetFood,Pushak,Stationary,Laptop,Office,GamingMonitor,Login,signup,resetPassword,category_summary,category,logout

urlpatterns = [

    path('', helloworld, name='helloworld'),

    path('FreeDelivery/', FreeDelivery , name='FreeDelivery'),

    path('NewYear/', NewYear , name='NewYear'),

    path('Bellow200/', Bellow200 , name='Bellow200'),

    path('JanebiPc/', JanebiPc , name='JanebiPc'),

    path('Behdashti/', Behdashti , name='Behdashti'),

    path('NewTechnology/', NewTechnology , name='NewTechnology'),

    path('PetFood/', PetFood , name='PetFood'),

    path('Pushak/', Pushak , name='Pushak'),

    path('Stationary/', Stationary , name='Stationary'),

    path('Laptop/', Laptop , name='Laptop'),

    path('Office/', Office , name='Office'),

    path('GamingMonitor/', GamingMonitor , name='GamingMonitor'),

    path('Login/', Login , name='Login'),

    path('signup/', signup , name='signup'),

    path('resetPassword/', resetPassword , name='resetPassword'),

    path('category/<str:cat>/',category, name='category'),

    path('category/',category_summary, name='category_summary'),

    path('logout/',logout, name='logout'),

]
