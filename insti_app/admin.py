from django.contrib import admin
from .models import InstiModel ,ContactModel # Import the InstiModel model from your models.py file

# Register the InstiModel model with the admin site
admin.site.register(InstiModel)
admin.site.register(ContactModel)