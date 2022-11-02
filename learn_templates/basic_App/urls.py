from django.urls import path
from basic_App import views

# FOR TEMPLATE TAGGING
app_name = 'basic_App'  #this allows us to use template tagging

urlpatterns=[

    path('relative/',views.relative, name = 'relative'),
    path('other/',views.other, name = 'Other'),

]
