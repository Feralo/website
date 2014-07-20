from django.db import models
import datetime

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default='')
    modified = models.DateTimeField('modified',default=datetime.datetime.today())
    created = models.DateTimeField('created', default=datetime.datetime.today())

    def __str__(self):
        return(self.title)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Lesson, self).save(*args, **kwargs)
