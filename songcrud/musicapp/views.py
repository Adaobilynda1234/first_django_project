from rest_framework import generics

# Create your views
from .models import song,Artiste
from .serializers import songSerializer,ArtisteSerializer

class songList(generics.ListCreateAPIView):
    queryset = song.objects.all()
    serializer_class = songSerializer

class songDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = song.objects.all()
    serializer_class = songSerializer

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
     

