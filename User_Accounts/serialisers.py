from rest_framework import serializers
from .models import User
from .models import Log_Activity



class Log_Activity_serialiser(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model = Log_Activity
        fields=['start_time','end_time','id']
        read_only_fields=('log_activity',)

    def create(self, validated_data):
        return Log_Activity.objects.get_or_create(**validated_data)


class User_serialiser(serializers.ModelSerializer):
    activity_period=Log_Activity_serialiser(many=True,read_only=True)
    class Meta:
        model=User
        fields=['id','full_name','country','city','activity_period']

    def create(self, validated_data):
        return User.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        instance.id  = validated_data.get('id',instance.id)
        instance.full_name   = validated_data.get('full_name',instance.full_name)
        instance.country     = validated_data.get('country',instance.country)
        instance.city        = validated_data.get('city',instance.city)




