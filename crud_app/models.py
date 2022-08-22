from django.db import models

# Create your models here.
class Employee(models.Model):
    # employee_id = models.IntegerField(primary_key=True)
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 ,default="")
    job_role = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.employee_id} ({self.first_name})"


