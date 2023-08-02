

from django.urls import path ,include

urlpatterns = [

    path('first_app/',include("first_app.urls"))
    
]
