from django.contrib import admin
from import_export import resources

from account.models import  BookData ,Personal_details
# ister your models here.
# admin.site.register(RoyaltyDetails)
# admin.site.register(Net_amount_Payable_Details)
admin.site.register(BookData)
admin.site.register(Personal_details)
# admin.site.register(Personal_details)
# class BookResource(resources.ModelResource):
# 	class Meta:
# 		model = BookData

