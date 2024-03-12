from django.db import models

class UserModel(models.Model):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    patient_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100 , default = '')
    profile_picture = models.FileField(null=True , blank=True)
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.first_name + " " + str(self.last_name)
