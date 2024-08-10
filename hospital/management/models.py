from django.db import models

#Store Patient information
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()

#Store doctor details
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()

#Links a patient to a doctor with an appointment date and time
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField()