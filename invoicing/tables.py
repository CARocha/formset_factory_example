from django.urls import reverse
from django.utils.safestring import mark_safe
from django_tables2 import tables

from invoicing.models import Invoice


class InvoiceTable(tables.Table):
    total = tables.columns.Column(verbose_name='Total', orderable=False, empty_values=(),
                                  attrs={'td': {"class": "text-right"}})
    options = tables.columns.Column(verbose_name='Options', orderable=False, empty_values=(),
                                    attrs={'td': {"class": "text-center"}})

    class Meta:
        model = Invoice
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped'}

    def render_options(self, value, record):
        edit = reverse('invoicing:invoice_edit', kwargs={'pk': record.pk})
        return mark_safe(
            '''
            <a href="{0}" class="btn btn-xs btn-warning">
                <i class="glyphicon glyphicon-search"></i>
            </a>
            '''.format(edit))

