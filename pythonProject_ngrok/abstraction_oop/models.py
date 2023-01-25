from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def _our_test_method_inside(self):
        # some code here
        pass
