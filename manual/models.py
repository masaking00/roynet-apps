from django.db import models
from django.db.models.fields.related import ForeignKey

class Category(models.Model):
    category_name = models.CharField(verbose_name="カテゴリー",max_length=20)
    c_order = models.IntegerField(verbose_name="表示順",unique=True)

    def __str__(self):
        return self.category_name

class CategoryRank(models.Model):
    cr_category_name = ForeignKey(Category,on_delete=models.CASCADE,verbose_name="カテゴリー")
    cr_rank = models.CharField(verbose_name="ランク名",max_length=10)
    cr_order = models.IntegerField(verbose_name="表示順")

    def __str__(self):
        return self.cr_rank

class Post(models.Model):
    p_title = models.CharField(verbose_name="タイトル",max_length=100)
    p_order = models.IntegerField(verbose_name="表示順")
    p_category = ForeignKey(CategoryRank,on_delete=models.CASCADE,verbose_name="カテゴリー")
    p_body = models.TextField(verbose_name="本文")

    def __str__(self):
        return str(self.p_order) + "：" + self.p_title