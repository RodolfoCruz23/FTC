from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from videos.models import Video

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)
