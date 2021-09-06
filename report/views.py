from dateutil.relativedelta import relativedelta
from datetime import date, datetime,timedelta

from django import forms, views
from django.contrib.auth import models
from django.db.models.query import QuerySet
from django.http import request
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import get_object_or_404,redirect,render,resolve_url
from django.views import generic
from django.urls import reverse

from django.views.generic import ListView

from report.forms import FoundItemsForm,FoundItemUpdateForm
from report.models import FoundItems,ReportDate
from register.models import User

#templateはviewのクラス名になる
class FindItemView(generic.ListView):
    model = FoundItems
    template_name = "list.html"
    paginate_by = 50

    def get_queryset(self,*args, **kwargs):

        #FoundItems.objects.all()と同じ
        queryset = super().get_queryset(**kwargs)

        y = self.request.GET.get('year')
        m = self.request.GET.get('month')
        c = self.request.GET.get('check')
        u = self.request.user.pk

        if y is not None:
            pass
        else:
            today = datetime.today()
            dd = today - relativedelta(months=1)
            y = dd.strftime('%Y')
            m = dd.strftime('%m')

        queryset = queryset.filter(FoundItems_Year=y,FoundItems_Month=m)

        return queryset

    def get_context_data(self, **kwarg):
        context = super().get_context_data()
        context['search_y'] = ReportDate.objects.values('ReportDate_year').distinct()
        context['search_m'] = ReportDate.objects.values('ReportDate_month').distinct()
 
        return context

class FoundItemUpdateView(generic.UpdateView,generic.DetailView):
    template_name = "report/item-update.html"
    model = FoundItems
    form_class = FoundItemUpdateForm

    def get_success_url(self):
        return resolve_url('report:list')    

def FoundItemsView(request):

    data = ReportDate.objects.all()

    params ={
        'data':data,
    }
    
    if request.method == 'POST':
        today = datetime.today()
        y = request.POST['year']
        m = request.POST['month']

        for i in User.objects.filter(is_staff=False):
            form = FoundItems(
                hotels = i,
                FoundItems_Year= y,
                FoundItems_Month= m,
                files = "",
                create_user = "",
                create_date = today,
                memo = "",
                )
            form.save()
        ReportDate(
            ReportDate_year = y,
            ReportDate_month = m
        ).save()

    return render(request,'report/all.html',params)