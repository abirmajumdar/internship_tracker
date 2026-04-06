from django.db import models

class Internship(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.role}"