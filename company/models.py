from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'countries'


class Region(models.Model):
    country = models.ForeignKey('company.Country', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'regions'


class Company(models.Model):
    region = models.ForeignKey('company.Region', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'companies'


class Job(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    incentive = models.IntegerField()
    stack = models.CharField(max_length=200)

    class Meta:
        db_table = 'jobs'


class Apply(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    job = models.ForeignKey('company.Job', on_delete=models.CASCADE)

    class Meta:
        db_table = 'applies'
