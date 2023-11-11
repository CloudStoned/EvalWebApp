from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Evaluation(models.Model):
    eval_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    eval_name = models.CharField(max_length=100)
    date_created = models.DateTimeField ("Eval Date Created")

    def __str__(self):
        return f"{self.eval_author} - {self.eval_name} - {self.date_created}"
    
class Question(models.Model):
    eval_form = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.eval_form} - {self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answers = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.question} - {self.choice_text} - {self.answers}"
    
