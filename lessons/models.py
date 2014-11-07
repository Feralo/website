from django.db import models
import datetime

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default='')
    modified = models.DateTimeField('modified',default=datetime.datetime.now, editable=False)
    created = models.DateTimeField('created', default=datetime.datetime.now, editable=False)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=40)

    def get_absolute_url(self):
        return "/%s/%s/%s/%s/" % (self.created.year, self.created.month, self.created.day,self.id)

    def __str__(self):
        return(self.title)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Lesson, self).save(*args, **kwargs)
