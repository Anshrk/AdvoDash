from django.contrib import admin
from .models import Cases, CaseStage, CaseType, Court

# Register your models here.
admin.site.register(Cases)
admin.site.register(CaseStage)
admin.site.register(CaseType)
admin.site.register(Court)