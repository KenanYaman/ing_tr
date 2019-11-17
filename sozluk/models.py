from django.db import models

# Create your models here.


class eng_tr(models.Model):
    eng = models.CharField(max_length=20, verbose_name="İngilizce")
    tr = models.CharField(max_length=20, verbose_name="Türkçe")
    exam = models.CharField(max_length=100, default="", verbose_name="Örnek")

    def __str__(self):
        return ("%s-%s" % (self.eng, self.tr))
