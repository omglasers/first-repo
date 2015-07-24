from rest_framework import serializers, viewsets
from .models import Card



class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ['name', 'owner', 'url_field', 'image', 'media_type', 'created_at']

		

class CardViewSet(viewsets.ModelViewSet):
	queryset = Card.objects.all()
	serializer_class = CardSerializer
