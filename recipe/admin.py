from django.contrib import admin
from .models import Post, PostType,category
# Register your models here.
def status_publish(modeladmin, request, queryset):
    queryset.update(status=3)
status_publish.short_description = 'publish'
def status_draft(modeladmin, request, queryset):
    queryset.update(status=0)
status_draft.short_description = 'draft'
class postAdmin(admin.ModelAdmin):
    def get_readonley_fields(obj=None):
        if obj:
            return ["created_on", "updated_on"]
        else:
            return []
    fieldsets = (
        (None, {
            'fields': ('title','slug','type', 'thumbnail', 'meta_description',)
        }),
        ('blog content', {
            'classes': ('collapse',),
            'fields': ('status','body'),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('author', 'categorys','created_on', 'updated_on'),
        }),
    )
    actions = [status_publish,status_draft ] 

    
    readonly_fields = ['created_on', 'updated_on']
    list_display = ('slug','title','status','author',)
    search_fields = ['slug','title',]
    list_filter = ('status','type',)
    prepopulated_fields = {'slug': ('title',),}
    

admin.site.register(Post,postAdmin)
admin.site.register(category)
admin.site.register(PostType)