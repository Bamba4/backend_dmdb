from django.db import models


# audit model
class Audit(models.Model):
    created_by = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True, blank=True)


# Create your models here.
class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)
    role = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class GodParent(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Tutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50,  blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pseudonyme = models.CharField(max_length=50, default=None, blank=True, null=True)
    has_memorized = models.BooleanField(default=False, blank=True, null=True)
    has_recited = models.BooleanField(default=False, blank=True, null=True)
    recite_date = models.DateTimeField(default=None, null=True)
    has_written = models.BooleanField(default=False, blank=True, null=True)
    current_surate = models.CharField(max_length=50, default=None, blank=True, null=True)
    memorize_date = models.DateTimeField(default=None, null=True)
    writting_begin_date = models.DateTimeField(default=None, null=True)
    current_step_writting = models.CharField(max_length=50, default=None, blank=True, null=True)
    writting_end_date = models.DateTimeField(default=None, null=True)
    mother = models.CharField(max_length=50, default=None, blank=True, null=True)
    father = models.CharField(max_length=50, default=None, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)
    surate = models.CharField(max_length=50, blank=True, null=True)
    joined_at = models.DateTimeField(default=None, null=True)
    avatar = models.CharField(max_length=50, blank=True, null=True)
    god_parent = models.ForeignKey(GodParent, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
