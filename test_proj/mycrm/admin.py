from django.contrib import admin
from mycrm.models import Restoration
from mycrm.models import Customer

from import_export.admin import ImportExportModelAdmin

from import_export import resources

# Register your models here.
class RestorationAdmin(admin.ModelAdmin):
    list_display = ("id","name", "price")
    search_fields = ("name",)

# class CustomerAdmin(admin.ModelAdmin):

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = (		
	        "id",
			"create_date",
			"name",
			"phone_number",
			"address",
			"tooth_diagram",
			"tooth_number",
			"restoration_request",
			"amount",
			"note"
		)

class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = CustomerResource
	list_display = (
		"id",
		"create_date",
		"name",
		"phone_number",
		"address",
		"tooth_diagram",
		"tooth_number",
		"restoration_request",
		"amount",
		"note"
	)

	# def get_restoration(self, obj):
	# 	return obj.restoration_request.name

	list_filter = (
		"restoration_request",
	)


	search_fields = (
		"id",
		"name",
		"phone_number",
		"address",)

admin.site.register(Restoration, RestorationAdmin)
admin.site.register(Customer, CustomerAdmin)

