import django_filters
from django.db.models import Q
from django.forms import SelectMultiple

from .models import corpora
from django import template
from django import forms

#the filters are created here some filters are created automatically others require an extra method

class CorporaFilter(django_filters.FilterSet):
    search_filter = django_filters.CharFilter(
        #this filter requires an extra method wich can be seen below
        method='my_search_filter',
        #the widget is added so that the bootstrap css style could be added to the filters
        widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    discipline = django_filters.ChoiceFilter(
        #this filter does not require an extra method and is just the choices that can be made in discipline
        widget=forms.Select(attrs={'class':'form-select'}),
        choices=corpora.discipline_choices)
    category = django_filters.ChoiceFilter(
        # this filter does not require an extra method and is just the choices that can be made in category
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=corpora.categories_choices)
    annotated = django_filters.ChoiceFilter(
        method='annotated_isnull_filter',
        #this filter does require an extra method
        widget=forms.Select(attrs={'class':'form-select'}),
        choices=(('annotated','annotated'),('not annotated','not annotated'))
    )

    # the model and filters are registered here, the fields metioned below can be seen on the site
    class Meta:
        model = corpora
        fields = ['search_filter','discipline','category','annotated']

    #This filter searches in name annotated anonymization and research
    def my_search_filter(self, queryset, name, value):
        return corpora.objects.filter(
            Q(name__icontains=value) |  Q(annotated__icontains=value) | Q(anonymization__icontains=value) | Q(research__icontains=value)
        )
    #This filter checks if annotated is empty or not
    def annotated_isnull_filter(self, queryset, name, value):
        if(value=='not_annotated'):
            return corpora.objects.filter(Q(annotated__isnull=True))
        else:
            return corpora.objects.filter(Q(annotated__isnull=False))

