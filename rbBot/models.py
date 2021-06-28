from django.db import models

# Create your models here.

class Temp(models.Model):
    user_id = models.BigIntegerField(unique=True, primary_key=True)

class User(models.Model):
    user_id     = models.BigIntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64, default="null")
    username    = models.CharField(max_length=64)
    is_started    = models.BooleanField(default=True)
    is_planning = models.BooleanField(default=False)
    latest    = models.BigIntegerField()

    class Meta:
        ordering = ['user_id']

    def __str__(self):
        return f'{self.user_id}'

class Route(models.Model):
    route_id = models.BigIntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['route_id']

    def __str__(self):
        return f'{self.route_id} belonging to {self.user_id}'

class Location(models.Model):
    postal_code  = models.BigIntegerField()
    long_address  = models.TextField(max_length=6)
    longtitude = models.DecimalField(max_digits = 18, decimal_places = 15)
    latitude = models.DecimalField(max_digits = 17, decimal_places = 15)
    route = models.ManyToManyField(Route)

    class Meta:
        ordering = ['postal_code']

    def __str__(self):
        return f'Location: long-{self.longtitude};lat-{self.latitude}'

class PlanningSession(models.Model):
    
    chat_id = models.BigIntegerField(unique=True)
    message_id = models.BigIntegerField(unique=True)
    instance = models.BigIntegerField(unique=True)
    message = models.TextField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['chat_id']

    def __str__(self):
        return f'Latest Planning Session {self.message_id} by {self.chat_id}'