from django.db import models
from django.urls import reverse

# Create your models here.

class Restaurant(models.Model):
    KECAMATAN_CHOICE = [
        ("Kebayoran Lama", "Kebayoran Lama"),
        ("Kebayoran Baru", "Kebayoran Baru"),
        ("Cilandak", "Cilandak"),
        ("Jagakarsa", "Mampang Prapatan"),
        ("Pancoran", "Pancoran"),
        ("Pasar Minggu", "Pasar Minggu"),
        ("Pesanggrahan", "Pesanggrahan"),
        ("Setiabudi", "Setiabudi"),
        ("Tebet", "Tebet"),
    ]
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100, choices=KECAMATAN_CHOICE)
    location = models.TextField(help_text="Detailed address of the restaurant")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.pk})

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Makanan Laut', 'Makanan Laut'),
        ('Makanan Tradisional', 'Makanan Tradisional'),
        ('Makanan Sehat', 'Makanan Sehat'),
        ('Makanan Cepat Saji', 'Makanan Cepat Saji'),
        ('Makanan Penutup', 'Makanan Penutup'),
    ]

    name = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} at {self.restaurant.name}"

    def get_absolute_url(self):
        return reverse('menu-item-detail', kwargs={'pk': self.pk})