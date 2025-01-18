from django.contrib import admin
from .models import *



admin.site.site_title = "Zuventure Login" 
admin.site.site_header = "Zuventure Panel"  
admin.site.index_title = "Welcome to the Zuventure Dashboard"  

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(SliderView)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Gallery)
admin.site.register(SisterConcern)
admin.site.register(CompanyInfo)
admin.site.register(Contact)
admin.site.register(Chairman)
admin.site.register(ManagingDirector)
admin.site.register(TeamMember)
@admin.register(CvCatagory)
class CvCatagory(admin.ModelAdmin):
    list_display = [field.name for field in CvCatagory._meta.fields]

@admin.register(DropCV)
class DropCV(admin.ModelAdmin):
    list_display = [field.name for field in DropCV._meta.fields]
    list_filter = ('cv_catagory',) 