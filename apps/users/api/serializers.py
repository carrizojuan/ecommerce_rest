from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    #Sirve para solo mostrar unos campos especificos y de forma personalizada al recibir un request de tipo GET
    # No pongo fields = ('id','name') ya que si recibo un un POST solo se podra rellenar los campos id y name y estaria mal
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.name
        }







""" class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def validate_name(self, name):

        

        if "juancho" == name:
            raise serializers.ValidationError("el nombre no puede ser juancho")
        return name

    def validate_email(self, email):

        if email == "":
            raise serializers.ValidationError("El email no puede estar vacio")

        if self.context["name"] in email:
            raise serializers.ValidationError("El nombre no puede estar contenido en el email")
            
        return email
    
    def validate(self, data):
        
        if data["name"] in data["email"]:
            raise serializers.ValidationError("El nombre no puede estar contenido en el email")
        return data
    
    def create(self, validate_data):
        return User.objects.create(**validate_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance """
    
