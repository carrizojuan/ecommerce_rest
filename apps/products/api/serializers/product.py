from apps.products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

    
    # Sirve para mostrar unos ciertos campos
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "image": instance.image if instance.image != "" else "", 
            "measure_unit": instance.measure_unit.description,
            "category": instance.category.description
        }
    
    