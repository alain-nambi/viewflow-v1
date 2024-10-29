from django.db import models
from viewflow.models import Process

class HelloWorldProcess(Process):
    text = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)