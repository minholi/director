from django.contrib import admin
from .models import Lead, Cadastral, Origem, Status, Atendimento

admin.site.register(Lead)
admin.site.register(Cadastral)
admin.site.register(Origem)
admin.site.register(Status)
admin.site.register(Atendimento)
