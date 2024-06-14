from django.db import models

class ParentTitle(models.Model):
    id = models.AutoField(primary_key=True)
    parent_no = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class SubTitle(models.Model):
    id = models.AutoField(primary_key=True)
    sub_no = models.IntegerField()
    title = models.CharField(max_length=255)
    parent_id = models.ForeignKey(ParentTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ChildTitle(models.Model):
    id = models.AutoField(primary_key=True)
    child_no = models.IntegerField()
    title = models.CharField(max_length=255)
    sub_id = models.ForeignKey(SubTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
