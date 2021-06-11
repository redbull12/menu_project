"""MenuProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dish_app.views import api_root, IngredientsListView, CreateIngredientView, DeleteIngredientView, DishViewSet, MenuViewSet

router = DefaultRouter()
router.register('dishes', DishViewSet)
router.register('menu', MenuViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),
    path('', api_root),
    path('api/v1/ingredients', IngredientsListView.as_view(), name='ingredients-list'),
    path('api/v1/ingredients/create', CreateIngredientView.as_view(), name='create-ingredient'),
    path('api/v1/ingrediens/delete/<int:pk>', DeleteIngredientView.as_view(), name='delete-ingredient')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
