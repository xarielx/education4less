from django.contrib.auth.models import User
from .models import Scholar
import django_filters
from crispy_forms.helper import FormHelper

class ScholarFilter(django_filters.FilterSet):
    scholarship_name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    requirements = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Scholar
        fields = ['scholarship_name', 'description', 'requirements', ]
    def __init__(self, *args, **kwargs):
        super(ScholarFilter, self).__init__(*args, **kwargs)
        self.helper = FormHelper()