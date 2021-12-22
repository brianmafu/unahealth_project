from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from unahealth_app.api.serializers import GlucoseLevelSerializer
from unahealth_app.models import GlucoseLevel



# API Views

# Glucose Level List view

# Use class-based view

class GlucoseLevelListView(generics.ListCreateAPIView):
    serializer_class = GlucoseLevelSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            levels = GlucoseLevel.objects.filter(user__id=int(user_id))
        else:
            # eitherwise return all of them
            levels = GlucoseLevel.objects.all()
        
        return levels
    

 # Glucose Detail View
 # used general funcation view   
@api_view(["GET"])
def glucose_level_detail(request, id): 
    try:
        level = GlucoseLevel.objects.get(id=id)
        serializer =  GlucoseLevelSerializer(level)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except GlucoseLevel.DoesNotExist:
        return Response(
            data = {
                "Error": "Glucose Level does not exist."
            },
            status = status.HTTP_204_NO_CONTENT
        )
            
        

    


