from rest_framework import serializers
from .models import MovieData


class movieDataTitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ('title',)


class movieDataRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ('rating',)


class movieDataReleaseDateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ('relase_date',)


class movieDataDescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ('description',)


class movieDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = '__all__'

