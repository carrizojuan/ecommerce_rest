from rest_framework import serializers

from apps.users.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','name', 'last_name','email', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


    def update(self, instance, validated_data):
        user_update = super().update(instance, validated_data)
        user_update.set_password(validated_data["password"])
        user_update.save()
        return user_update


#Este serializer se usaria solo para listar los usuarios asi no interfiere con el funcionamiento cuando se realizar un update o create

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
 
    #Sirve para solo mostrar unos campos especificos y de forma personalizada al recibir un request de tipo GET
    # No pongo fields = ('id','name') ya que si recibo un un POST solo se podra rellenar los campos id y name y estaria mal
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'password': instance.password
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
    
