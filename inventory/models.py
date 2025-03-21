from django.db import models
from django.utils import timezone
from personal.models import Personal


class Inventory_status(models.Model):
    # rental_status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Inventarnik(models.Model):
    # equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    inventory_number = models.IntegerField(unique=True)
    registration_date = models.DateField()
    photo = models.ImageField(upload_to='inventory/') # ?
    description = models.TextField()
    status = models.ForeignKey(Inventory_status, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Arenda(models.Model):
    # rental_id = models.AutoField(primary_key=True)
    equipment_id = models.ForeignKey(Inventarnik, on_delete=models.CASCADE)
    renter_id = models.ForeignKey(Personal, related_name='renter', on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Personal, related_name='assigned_rentals', on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    actual_return_time = models.DateTimeField(null=True, blank=True)
    event_location = models.CharField(max_length=100)
    arenda_description = models.TextField()

    def __str__(self):
        return self.equipment_id.name

class Teh_obslujiwanie(models.Model):
    # maintenance_id = models.AutoField(primary_key=True)
    equipment_id = models.ForeignKey(Inventarnik, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(Personal, related_name='reported_issues',on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Personal, related_name='assigned_issues',on_delete=models.CASCADE)
    issue_description = models.TextField()
    status = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.equipment_id.name # ?