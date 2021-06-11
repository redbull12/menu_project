from rest_framework import serializers

from .models import Dish, Ingredient, MenuForWeek


###
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['ingredients'] = IngredientSerializer(instance.ingredients, context=self.context).data
        # representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        # representation['likes'] = instance.likes.count()
        # return representation

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise serializers.ValidationError('Название блюда не должно повторяться')
        return title

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['category'] = CategorySerializer(instance.category, context=self.context).data
    #     representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
    #     representation['likes'] = instance.likes.count()
    #     return representation

class DishListSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='dish-detail', lookup_field='slug')

    class Meta:
        model = Dish
        # fields = ['title', 'slug', 'price', 'details']
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuForWeek
        fields = '__all__'