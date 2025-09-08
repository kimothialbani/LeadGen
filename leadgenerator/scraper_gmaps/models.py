# scraper/models.py

from django.db import models


class ZipCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    STATUS_CHOICES = [
        ('NOT SCRAPED', 'Not Scraped'),
        ('SCRAPED', 'Scraped'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT SCRAPED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    place_id = models.CharField(max_length=255, unique=True)
    # This links the lead back to the search that found it
    zip_code = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    smart_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

