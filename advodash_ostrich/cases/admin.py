from django.contrib import admin
from .models import Case, Court, CaseType, CaseStage

# Register your models here.
admin.site.register(Case)
admin.site.register(CaseType)
admin.site.register(CaseStage)
admin.site.register(Court)
