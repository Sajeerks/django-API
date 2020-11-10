# this is serailizer page
from rest_framework import serializers
from .models import Course

class  CourseSerializer(serializers.HyperlinkedModelSerializer):#ModelSerializer
	class Meta:
		model = Course
		fields = ('id', 'url','name', 'language', 'price')

