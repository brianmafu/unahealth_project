from rest_framework import serializers, validators
from unahealth_app.models import GlucoseLevel

# GlucoseLevel Serializer
class GlucoseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseLevel
        fields = "__all__"
