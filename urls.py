from django.conf.urls import url
from . import views


     
app_name = "Pg"

urlpatterns = [
		    
			 url(r"^base/$", views.base, name="base"),
			 url(r"^about/$", views.about, name="about"),
			 url(r"^logo/$", views.logo, name="logo"),
			 url(r"^logo1/$", views.logo1, name="logo1"),
			 url(r'^mainpg/$', views.mainpg, name='mainpg'),
			 url(r'^q/$', views.q, name='q'),
			 url(r'^backg1/$', views.backg1, name='backg1'),
			 url(r'^backg2/$', views.backg2, name='backg2'),
			 url(r'^home/$', views.home, name='home'),
			 url(r'^cont/$', views.cont, name='cont'),
			 url(r'^how_it_works/$', views.how_it_works, name='how_it_works'),
			 url(r'^help_and_support/$', views.help_and_support, name='help_and_support'),
			 url(r'^Cust_register/$', views.Cust_register, name='Cust_register'),
			 url(r"^Cust_login/$", views.Cust_login, name="Cust_login"),
			 url(r"^logout/$", views.logout, name="logout"),
			 url(r"^Ldetails/$", views.Ldetails, name="Ldetails"),
			 url(r'^Land_register/$', views.Land_register, name='Land_register'),
			 url(r"^Ldisplay/$", views.Ldisplay, name="Ldisplay"),
			 url(r"^Cdetails/$", views.Cdetails, name="Cdetails"),
			 url(r"^Maindisplay/$", views.Maindisplay, name="Maindisplay"),
			 url(r"^payment/$", views.payment, name="payment"),
			 url(r"^forgot/$", views.forgot, name="forgot"),
             url(r"^Hostelselect/$", views.Hostelselect, name="Hostelselect"),
             url(r"^own_message/$", views.own_message, name="own_message"),
             
			
			 
		   ]
		   





