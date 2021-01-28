from django.db import models

# Create your models here.
JOB = (('info', '学生'),('success','社会人'),('dark','無職'),)

class Todohuman(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(
        default=20
    )
    job=models.CharField(
        choices=JOB,
        max_length=50,
        default='社会人'
    )
    memo=models.TextField(
        max_length=200,
        null=True,
    )
    birth=models.DateField()

    def __str__(self):#/admin内のデータを見やすくする
        return self.name
