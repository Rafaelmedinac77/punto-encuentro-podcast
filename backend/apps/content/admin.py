from django.contrib import admin
from .models import Category, Guest, Episode, Article, Subscriber

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'featured')
    list_filter = ('featured',)
    search_fields = ('name', 'profession')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'guest', 'status', 'featured', 'published_at', 'duration')
    list_filter = ('status', 'featured', 'categories')
    search_fields = ('title', 'description', 'reflection')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    list_filter = ('published',)
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('email', 'name')
