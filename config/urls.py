from django.contrib import admin
from django.urls import path
from damawkaIkki.views import damawka_ikki

urlpatterns = [
    path('', damawka_ikki),
    path('admin/', admin.site.urls),
]
