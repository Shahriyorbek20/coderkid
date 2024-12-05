# from django.db import models

# class Debtor(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     due_date = models.DateField()

#     def __str__(self):
#         return self.name
from django.db import models

class Debtor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# models.py
from django.db import models



from django.db import models

class Plan(models.Model):
    PLAN_TYPE_CHOICES = [
        ('yearly', 'Yillik'),
        ('monthly', 'Oylik'),
        ('weekly', 'Haftalik'),
        ('daily', 'Kunlik'),
    ]

    plan_type = models.CharField(max_length=10, choices=PLAN_TYPE_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title
