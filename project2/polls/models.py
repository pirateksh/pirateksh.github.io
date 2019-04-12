from django.db import models

# Create your models here.


class Question(models.Model):

    ques_no = models.IntegerField(verbose_name="Question Number")  # verbose_name-> Name of column
    ques_text = models.CharField(max_length=1000, verbose_name="Text")
    pub_date = models.DateField(verbose_name="Publication Date")

    def __str__(self):
        return self.ques_text


class Choice(models.Model):

    choice_no = models.IntegerField(verbose_name="Choice Number")
    choice_text = models.CharField(max_length=500, verbose_name="Text")
    no_of_votes = models.IntegerField(verbose_name="Number of Votes")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.choice_text
