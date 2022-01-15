from django.contrib import admin
from .models import *

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['cardtitle','price','pricingfirst']
admin.site.register(Pricing,PricingAdmin)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['reviewsname','reviewstext']
admin.site.register(Reviews,ReviewsAdmin)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["email",'questiontext']
admin.site.register(Question,QuestionAdmin)
