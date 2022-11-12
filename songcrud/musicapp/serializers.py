from rest_framework import serializers
from .models import song , Artiste


class songSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artiste_id",
        )
        model = song
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            "id",
            "first_name",
            "last_name",
            "age",
        )
        model = Artiste

            
        

