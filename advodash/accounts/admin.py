from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FirmUser, Firm, Position
from .forms import FirmUserCreationForm
# Custom user model
class FirmUserAdmin(UserAdmin):
    model = FirmUser
    add_form = FirmUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Lawyer-Details',
            {
                'fields': (
                    'firm',
                    'position'
                )
            }
        )
    )

# Register your models here.
admin.site.register(FirmUser, FirmUserAdmin)
admin.site.register(Firm)
admin.site.register(Position)
