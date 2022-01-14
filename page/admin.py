from django.contrib import admin
from .models import *

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Pricing)
admin.site.register(Reviews)