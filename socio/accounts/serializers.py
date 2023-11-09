"""
Accounts Serializers 

"""
from rest_framework import serializers
from accounts.models import User
from util_base.serializer._initSerializer import TimeStampMixinSerializer



# login serializers
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','password']




## User Password Change Serializers 
class UserChangePasswordSerializer(serializers.Serializer):
  
  old_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  confirm_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)

  class Meta:
    fields = ['password', 'confirm_password']

  def validate(self, attrs):
    old_password = attrs.get('old_password')
    password = attrs.get('password')
    confirm_password = attrs.get('confirm_password')

    user = self.context.get('user')
    if not user.check_password(old_password):
       raise serializers.ValidationError("Old Password didn`t Match !")
    if password != confirm_password:
      raise serializers.ValidationError("Password and Confirm Password doesn't match !")
    
    user.set_password(password)
    user.save()
    return attrs
  

### ### ###########
### Register Profile for Socio 

class CreateProfileSocioSerializer(TimeStampMixinSerializer):
    

    password = serializers.CharField(max_length=255, 
                                     style={'input_type':'password'}, write_only=True)
    confirm_password = serializers.CharField(max_length=255, 
                                      style={'input_type':'password'}, write_only=True)
   
    class Meta:
        from socio_profile.models import SocioUser
        model = SocioUser
        fields = [
          "full_name",
          "phone_number",
          "email",
          "password",
          "confirm_password"
        ]


    def create(self, validated_data):
       
      from django.contrib.auth.hashers import make_password
      from accounts.models import User
      from util_base.utils._utils import SocialUtility
      from socio_profile.models import SocioUser
      

      ## Getting fields 
      email = validated_data.get("email")
      phone_number = validated_data.get("phone_number")
      password  = validated_data.pop("password")
      confirm_password = validated_data.pop("confirm_password")

      ## checking password 
      if password != confirm_password :
         raise serializers.ValidationError("Password Mismatch")
      
      ## checking unique email
      if SocioUser.objects.filter(
         email=email
      ).only(
         "email"
      ).exists():
         raise serializers.ValidationError("Email is Already registerd !")
      
      ## checking unique phone number
      if SocioUser.objects.filter(
         phone_number=phone_number
      ).only(
         "phone_number"
      ).exists():
         raise serializers.ValidationError("Phone Number Already Exists !")

      ## declaring auth info
      auth_info = {
         "username" : SocialUtility.generate_username(instance=User),
         "password" : make_password(password),
         "confirm_password" : make_password(confirm_password)
      }
      
      ## saving User
      user_obj = User(**auth_info)
      user_obj.save()

      ## Saving Socio profile
      socio_profile_obj = SocioUser(user=user_obj, **validated_data)
      socio_profile_obj.save()

      return socio_profile_obj