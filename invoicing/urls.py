from django.conf.urls import url

from invoicing.views import InvoiceSingleTableView, InvoiceFormView, InvoiceUpdateView

urlpatterns = [
    url(r'^$', InvoiceSingleTableView.as_view(), name='invoice_list'),
    url(r'^new-invoice/$', InvoiceFormView.as_view(), name='invoice_add'),
    url(r'^edit-invoice/(?P<pk>\d+)/$$', InvoiceUpdateView.as_view(), name='invoice_edit'),
]
