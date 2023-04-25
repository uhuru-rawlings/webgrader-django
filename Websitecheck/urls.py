from django.contrib import admin
from django.urls import path
from dashboard.views import check_website_view
# get_page_speed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', check_website_view, name='website_checker'),
    # path('dashboard/', get_page_speed, name='dashboard'),
]
