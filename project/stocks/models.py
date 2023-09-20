from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class plants(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="stocks/", null=True, blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    uploaded_date = models.DateField()


    def __str__(self):
        return self.common_name
    
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plants = models.ManyToManyField(plants, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("DONE", "Done")
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")      

    def __str__(self):
        return f"Order #{self.pk}"

    def total_cost(self):
        return sum(plant.price for plant in self.plants.all())

    def total_items(self):
        return self.plants.count()