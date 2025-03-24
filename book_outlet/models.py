
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

"""class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False)
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"  """
        

#from django.db import models
#from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name ="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)  # Ensure unique slugs

    def save(self, *args, **kwargs):
        # Generate the slug if it doesn't already exist
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"








