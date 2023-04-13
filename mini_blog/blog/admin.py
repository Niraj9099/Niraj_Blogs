from django.contrib import admin
from .models import blog_model, ContactForm

# Register your models here.

@admin.register(blog_model)
class model_blog(admin.ModelAdmin):
    list_display= ['id','user','title', 'disc', 'img']


@admin.register(ContactForm)
class ContactForm_Admin(admin.ModelAdmin):
    list_display= ['full_name','email', 'message']