from django.conf.urls import url
import views

urlpatterns = [
	url(r'$^',views.upload_file),
]
