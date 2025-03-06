# from rest_framework import generics
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer

# Реализация сериализатора
class WomenAPIView(APIView):
    def get(self, request):
        # Формирование списка из объекта классов Women
        w = Women.objects.all()
        # Передача параметров на Сериализатор
        return Response({'posts': WomenSerializer(w, many=True).data}) # many - для списка записей

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],            # request.data используется для получения данных
            content=request.data['content'],        # которые были отправлены в запросе 
            cat_id=request.data['cat_id']           # POST, PUT или PATCH
        )
        return Response({'post': WomenSerializer(post_new).data})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
