from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Guest(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    profession = models.CharField(max_length=180, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='guests/', blank=True, null=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    website = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Invitado'
        verbose_name_plural = 'Invitados'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Episode(models.Model):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
    STATUS_CHOICES = [(DRAFT, 'Borrador'), (PUBLISHED, 'Publicado')]

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    subtitle = models.CharField(max_length=220, blank=True)
    description = models.TextField(blank=True)
    youtube_url = models.URLField()
    youtube_id = models.CharField(max_length=40, blank=True)
    thumbnail_url = models.URLField(blank=True)
    duration = models.CharField(max_length=20, blank=True)
    reflection = models.TextField(blank=True, help_text='Reflexión del episodio')
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True, related_name='episodes')
    categories = models.ManyToManyField(Category, blank=True, related_name='episodes')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PUBLISHED)
    featured = models.BooleanField(default=False)
    published_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Episodios'
        ordering = ['-published_at', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.youtube_id:
            self.youtube_id = extract_youtube_id(self.youtube_url)
        if self.youtube_id and not self.thumbnail_url:
            self.thumbnail_url = f'https://img.youtube.com/vi/{self.youtube_id}/hqdefault.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Recurso / Artículo'
        verbose_name_plural = 'Recursos / Artículos'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email

def extract_youtube_id(url):
    import re
    patterns = [r'v=([a-zA-Z0-9_-]{11})', r'youtu\.be/([a-zA-Z0-9_-]{11})', r'embed/([a-zA-Z0-9_-]{11})']
    for pattern in patterns:
        match = re.search(pattern, url or '')
        if match:
            return match.group(1)
    return ''
