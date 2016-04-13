from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    def __unicode__(self):
        que = self.question
        pub = self.pub_date
        return "question:"+str(que)+"pub_date:"+str(pub)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text