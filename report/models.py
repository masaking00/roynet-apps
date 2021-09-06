from django.db.models.fields import files
import register
from django.db import models
from django.db.models.fields.related import ForeignKey

from register.models import User

class ReportDate(models.Model):
    ReportDate_year = models.CharField(max_length=4,verbose_name="報告年")
    ReportDate_month = models.CharField(max_length=2,verbose_name="報告月")

    def __str__(self) -> str:
        return self.ReportDate_year + " - " + self.ReportDate_month

class FoundItems(models.Model):
    hotels = ForeignKey(User,on_delete=models.CASCADE,verbose_name="ホテル名")
    FoundItems_Year = models.CharField(max_length=4,verbose_name="報告年")
    FoundItems_Month = models.CharField(max_length=4,verbose_name="報告月")
    files = models.FileField(upload_to='item/%Y/',blank=True)
    create_user = models.CharField(max_length=20,verbose_name="報告者名",blank=True)
    create_date = models.DateField()
    memo = models.TextField(verbose_name="コメント",blank=True, default=None,max_length=100)

    def save(self, *args, **kwargs):
        try:
            this = FoundItems.objects.get(id=self.id)
            if this.files != self.files:
                this.files.delete()
        except:
            pass
        super(FoundItems, self).save(*args, **kwargs)