from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Women
from .serializers import WomenSerializer

# Новый сериализатор, класс представления для чтения и добавления новой записи
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# Реализация сериализатора
class WomenAPIView(APIView):
    def get(self, request):
        # Формирование списка из объекта классов Women
        w = Women.objects.all()
        # Передача параметров на Сериализатор
        return Response(
            {"posts": WomenSerializer(w, many=True).data}
        )  # many - для списка записей

    def post(self, request):
        # Проверка на корректность в POST запросе title, content, cat_id
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed, pk not provided"})

        try:
            instance = Women.objects.get(pk=pk)
        except Women.DoesNotExist:
            return Response({"error": "Object does not exist"})

        instance.delete()
        return Response({"post": "delete post" + str(pk)})
