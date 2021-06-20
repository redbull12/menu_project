from rest_framework.routers import DefaultRouter
from dish_app.views import MenuViewSet, DishViewSet, IngredientsListView, CreateIngredientView, DeleteIngredientView
from django.urls import path, include


router = DefaultRouter()
router.register('dishes', DishViewSet)
router.register('menu', MenuViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ingredients.', IngredientsListView.as_view(), name='ingredients-list'),
    path('ingredients/create.', CreateIngredientView.as_view(), name='create-ingredient'),
    path('ingrediens/delete/<int:pk>.', DeleteIngredientView.as_view(), name='delete-ingredient')
]