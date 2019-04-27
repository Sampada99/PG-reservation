from django.contrib import admin
from .models import PG_selection, Help_and_Support
from .models import Landdetails
from .models import Custdetails
from .models import Designation


class Help_and_SupportAdmin(admin.ModelAdmin):
	list_display = ('PG_selection', 'customer_name', 'date', 'satisfied','email' ,)
	list_filter = ('PG_selection', 'date',)
	search_fields = ('PG_selection', 'comments_on_PG',)
 
	class Meta:
		model = Help_and_Support

class LanddetailsAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'Hostel_name', 'Female_or_Male', 'Rent','Mess','date',)
	list_filter = ('Hostel_name', 'Rent','date',)
	search_fields = ('Hostel_name', 'Rent',)

 
	class Meta:
		model = Landdetails

class CustdetailsAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'retype_email' , 'Female_or_Male', 'Designation',)
	list_filter = ('Female_or_Male', 'Designation',)
	search_fields = ('Designation', 'Female_or_Male',)
 
	class Meta:
		model = Custdetails




admin.site.register(Help_and_Support, Help_and_SupportAdmin)
admin.site.register(PG_selection)
admin.site.register(Designation)
admin.site.register(Landdetails, LanddetailsAdmin)
admin.site.register(Custdetails, CustdetailsAdmin)




	

