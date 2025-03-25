"""
Serializer for recipe APIs
"""

from rest_framework import serializers

from core import models


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe app"""

    class Meta:
        model = models.Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only = ['id']


class RecipeDetailSerializer(RecipeSerializer):
     """Serializer for recipe detail view."""
 
     class Meta(RecipeSerializer.Meta):
         fields = RecipeSerializer.Meta.fields + ['description']