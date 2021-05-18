import django_filters
from django.db.models import Q
from django.forms import SelectMultiple

from .models import corpora
from django import template
from django import forms

class CorporaFilter(django_filters.FilterSet):
    #register = template.Library()
    search_filter = django_filters.CharFilter(
        method='my_search_filter',
        widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    discipline = django_filters.ChoiceFilter(
        widget=forms.Select(attrs={'class':'form-select'}),
        choices=corpora.discipline_choices)
    category = django_filters.ChoiceFilter(
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=corpora.categories_choices)
    annotated = django_filters.ChoiceFilter(
        method='annotated_isnull_filter',
        widget=forms.Select(attrs={'class':'form-select'}),
        choices=(('annotated','annotated'),('not annotated','not annotated'))
    )
    class Meta:
        model = corpora
        fields = ['search_filter','discipline','category','annotated']


    #@register.filter(name='search')
    def my_search_filter(self, queryset, name, value):
        return corpora.objects.filter(
            Q(name__icontains=value) | Q(annotated__icontains=value) | Q(annotated__icontains=value) | Q(anonymization__icontains=value) | Q(research__icontains=value)
        )

    #@register.filter(name='annotated_isnull_filter')
    def annotated_isnull_filter(self, queryset, name, value):
        if(value=='not_annotated'):
            return corpora.objects.filter(Q(annotated__isnull=True))
        else:
            return corpora.objects.filter(Q(annotated__isnull=False))

