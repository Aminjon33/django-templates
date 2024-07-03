from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.name} by {self.email}"
 
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} by {self.email}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    slug = models.SlugField(unique=True, blank=True)  # Slug maydoni qo'shildi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

        return f"{self.name}"
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    slug = models.SlugField(unique=True, blank=True)  # Slug maydoni qo'shildi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
