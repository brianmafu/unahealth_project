from django.urls import path, include
from unahealth_app.api.views import GlucoseLevelListView, glucose_level_detail

urlpatterns = [
    
    path('levels/', GlucoseLevelListView.as_view(), name='glucose-level'),
    path('levels/<id>', glucose_level_detail, name='glucose-level-detail'),

]
