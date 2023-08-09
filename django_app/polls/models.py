from django.db import models
from django.utils import timezone
import datetime



# Create your models here.


class Question (models.Model):
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField("date published / dato de publicación")
    #método para visualizar los registros por medio de la shell interactive
    def __str__(self):
        return self.question_text
        #método para saber si una pregunta es actual menor a un dia de publicada
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice (models.Model):
    #question= models.ForeignKey(Question, on_delete=models.CASCADE, related_name=‘question_choices’)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text