from django.contrib import admin

from invoicing.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

