from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django_tables2 import SingleTableView

from invoicing.forms import InvoiceForm, ItemInvoiceFormSet, ItemInvoiceUpdateFormSet
from invoicing.models import Invoice
from invoicing.tables import InvoiceTable


class InvoiceFormView(SuccessMessageMixin, FormView):
    form_class = InvoiceForm
    template_name = 'invoice_form.html'
    success_url = reverse_lazy('invoicing:invoice_list')
    success_message = 'The invoice was created correctly.'

    def get_context_data(self, **kwargs):
        context = super(InvoiceFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemInvoiceFormSet(self.request.POST, prefix='items')
        else:
            context['formset'] = ItemInvoiceFormSet(prefix='items')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        total = 0
        if formset.is_valid():
            invoice = form.save(commit=False)
            invoice.total = 0
            invoice.save()
            for item_form in formset.forms:
                item = item_form.save(commit=False)
                item.invoice = invoice
                item.save()
                total += item.quantity * item.unit_price
            invoice.total = total
            invoice.save()
            return super(InvoiceFormView, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class InvoiceUpdateView(SuccessMessageMixin, UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice_edit.html'
    success_url = reverse_lazy('invoicing:invoice_list')
    success_message = 'The invoice was edited correctly.'

    def get_context_data(self, **kwargs):
        context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        invoice = self.get_object()
        productos = invoice.item_set.all()
        if self.request.POST:
            context['formset'] = ItemInvoiceUpdateFormSet(self.request.POST, self.request.FILES, prefix='items')
        else:
            context['formset'] = ItemInvoiceUpdateFormSet(queryset=productos, prefix='items')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        total = 0
        if formset.is_valid():
            invoice = form.save(commit=False)
            for item_form in formset.forms:
                item = item_form.save(commit=False)
                item.invoice = self.get_object()
                item.save()
                total += item.quantity * item.unit_price
            formset.save()
            invoice.total = total
            invoice.save()
            return super(InvoiceUpdateView, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class InvoiceSingleTableView(SingleTableView):
    table_class = InvoiceTable
    queryset = Invoice.objects.all()
    template_name = 'invoice_list.html'
