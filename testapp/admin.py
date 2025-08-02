from django.contrib import admin
from testapp.models import Ads,Contact,Categories,Member
# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display=['category']
class AdsAdmin(admin.ModelAdmin):
    list_display=['category','brand','email','mobile']

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','subject']

class MemberAdmin(admin.ModelAdmin):
    list_display=['name','role','email','mobile']

admin.site.register(Ads,AdsAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Categories,CatAdmin)
admin.site.register(Member,MemberAdmin)
