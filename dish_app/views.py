from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from .models import Dish, Ingredient, MenuForWeek
from .permissions import IsAdminPermission, IsAuthorPermission
from .serializers import DishSerializer, IngredientSerializer, DishListSerializer, MenuSerializer

class DishesListView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_url_kwarg = 'slug'
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['ingredient']
    search_fields = ['title']
    ordering_fields = ['title']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminPermission]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return DishListSerializer
        return self.serializer_class

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class IngredientsListView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CreateIngredientView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAdminPermission]

class DeleteIngredientView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAdminPermission]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'dishes': reverse('dish-list', request=request, format=format),
        'ingredients': reverse('ingredients-list', request=request, format=format),
    })


class MenuViewSet(ModelViewSet):
    queryset = MenuForWeek.objects.all()
    serializer_class = MenuSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}

# TODO