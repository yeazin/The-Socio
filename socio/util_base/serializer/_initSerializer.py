"""
Base serializers for the Applicaiton 
"""

from rest_framework import serializers

class TimeStampMixinSerializer(serializers.ModelSerializer):


    obj_id = serializers.CharField(source="id",read_only=True)
    
    class Meta:

        fields = [
            "obj_id", 
            "is_active", 
            "created_at", 
            "updated_at"
            ]
        
        read_only_fields = [
            "obj_id",
            "is_active",
            "created_at",
            "updated_at"
        ]
        abstract = True