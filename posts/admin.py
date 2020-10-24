from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user')
    list_display_links = ('pk', 'title')
    search_fields = (
        'pk',
        'title',
        'user__username',
        'user__lastname',
        'profile__website'
    )
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at','updated_at')


