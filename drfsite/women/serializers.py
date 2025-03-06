from rest_framework import serializers


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True) # read_only=True - читается при добаление в БД
    time_update = serializers.DateTimeField(read_only=True) # read_only=True - читается при добаление в БД
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()





# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# # Кодирование JSON информации
# def encode():
#     model = WomenModel("Angelina Jolie", "Content: Angelina Jolie")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# # Декодирование JSON инфомации
# def decode():
#     stream = io.BytesIO(
#         b'{"title":"Angelina Jolie", "content":"Content: Angelina Jolie"}'
#     )
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
