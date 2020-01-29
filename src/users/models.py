from django.db import models
import datetime
# Create your models here.
# Model is the single definition of the data, is going to contain all the fields and behaviors of the data

class User(models.Model):
    first_name = models.CharField("first name",max_length=30)
    last_name = models.CharField("last name",max_length=30)
    cars = models.ManyToManyField("Car",verbose_name="the user's cars")

STATUS_CHOICES = (
    ('R', 'Reviewed'), # Only the first element will be stored in db, second element is what used to display
    ('N','Not Reviewed'),
    ('E','Error'),
    ('A','Accepted')
)
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete specifies what to do when the user is deleted
    
    def was_released_last_week():
        if self.release_date < datetime.date(2020,1,21):
            return "Released before last week"
        else:
            return "Released this week"
    
    @property
    def get_full_name(self):
        return f"This is my website's full name: {self.name}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/website/{self.id}"

    def save(self,*args,**kwargs):
        print("we are doing sth else here...")
        super().save(*args,**kwargs)
    class Meta:
        ordering = ['rating']
        db_table = 'website_custom_table_name'
        verbose_name = 'the website'
        verbose_name_plural = 'the websites'

class Car(models.Model):
    name = models.CharField(max_length=40,primary_key=True)

class Ox(models.Model):
    class Meta:
        verbose_name = 'ox'
        verbose_name_plural = 'oxen'
