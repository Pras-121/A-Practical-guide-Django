from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    
    
    def __str__(self) -> str:
        return f"{self.country} - {self.code}" 
    
    class Meta:
        verbose_name_plural = "Countries"
        
        
class Address(models.Model):
    street=models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
         return f"{self.street}, {self.city}, {self.postal_code} "


    class Meta:
        verbose_name_plural = "Address Entries"
    
class Author(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)    
     
     def __str__(self) -> str:
         return self.full_name()
     
     def full_name(self):
         return f"{self.first_name} {self.last_name}"
     
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               null=True, related_name="bk_author")
    is_bestselling = models.BooleanField(default=False)
    slug =models.SlugField(default="",blank=True,
                           null=False,db_index=True) # building URL using slug
    published_country = models.ManyToManyField(Country)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title.lower())
    #     super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("Book-Details-page", kwargs={"slug": self.slug})
        # return reverse("Book-Details-page", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f"{self.title} ({self.rating} {self.author} {self.is_bestselling})"  
    
     
     