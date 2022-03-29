from django.db import models


class Spider(models.Model):
    id = models.CharField(max_length=50, primary_key=True)


class JobData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    num_errors = models.IntegerField()
    num_items = models.IntegerField()
    date = models.DateTimeField()
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE)
