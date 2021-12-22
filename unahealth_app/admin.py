from django.contrib import admin
from unahealth_app.models import GlucoseLevel, User

# Register your models here.

# Register GlucoseLevel Model for django admin
admin.site.register(GlucoseLevel)
admin.site.register(User)
