from django.contrib import admin
from .models import Appointment, Propriete, Space, Membre

admin.site.register(Appointment)
admin.site.register(Propriete)
admin.site.register(Space)
admin.site.register(Membre)
