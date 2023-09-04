from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import views using an absolute import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    # ...
]
