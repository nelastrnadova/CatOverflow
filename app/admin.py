from django.contrib import admin

# Register your models here.
from app.models import Post, Comment


class CommentInline(admin.StackedInline):
    fields = ['user_fk', 'votes', 'comment_text']
    readonly_fields = ['user_fk', 'votes']
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields': ['title', 'votes', 'post_text']}),
    ]
    readonly_fields = ['votes']
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
