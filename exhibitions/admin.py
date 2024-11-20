from django.contrib import admin
from exhibitions.models import Exhibition, Contact

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')