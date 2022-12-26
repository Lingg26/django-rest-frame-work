from rest_framework import serializers
from CategoryList.models import CategoryList
class CategoryListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title= serializers.CharField(max_length=255)
    slug= serializers.CharField(max_length=255)
    category_id= serializers.CharField()
    createdAt= serializers.DateTimeField(read_only= True)
    updatedAt= serializers.DateTimeField(read_only= True)

    def create(self, data):
        return CategoryList.objects.create(**data)

    def update(self, instance, data):
        instance.title=data.get('title', instance.title)
        instance.slug=data.get('slug', instance.slug)
        instance.category_id=data.get('category_id', instance.category_id)
        instance.createdAt=data.get('createdAt', instance.createdAt)
        instance.updatedAt=data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance