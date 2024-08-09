from django.urls import path, include

urlpatterns = [
    path('contact/', include('api.v1.contact.urls')),
]
