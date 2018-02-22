from django.contrib import admin
from blog.models import Blog , UploadFileForm, add_teacher ,  Category , CategoryFile ,Time_table , Documentation



admin.site.register(Blog)
admin.site.register(UploadFileForm)
admin.site.register(add_teacher)
admin.site.register(Category)
admin.site.register(CategoryFile)
admin.site.register(Time_table)
admin.site.register(Documentation)
