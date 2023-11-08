"""
Accounts Serializers 

"""
from rest_framework import serializers
from accounts.models import User



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