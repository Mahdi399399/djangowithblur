from rest_framework import serializers
from .models import awsimage
class awsimagesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=awsimage
        fields=('title','images')

    '''def validate(self, images):
        """
        Check that start is before finish.
        """
        fm > 100:
        if images=

        raise serializers.ValidationError("finish must occur after start")

    return data'''