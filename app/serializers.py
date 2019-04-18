from .models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('name', 'description', 'point', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10')