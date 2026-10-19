from django.contrib import admin
from django.contrib import admin
from django.urls import path
from mysite.views import (
    homepage,
    showpost,
    about,
    listing,
    disp_detail,
    news_live,
    musiclist,
)
from phone import views as phone_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', homepage),

    path('post/<slug:slug>/', showpost),

    path('about/', about),

    path('list/', listing),

    path('list/<str:sku>/', disp_detail),

    path('news/', news_live, name='news-live-home'),

    path('news/<int:tvno>/', news_live, name='news-live'),

    path('musiclist/', musiclist),

    path('musiclist/<int:category>/', musiclist, name='musiclist-url'),
    
    path('phone/', phone_views.phone_list, name='phone-list'),

    path('phone/<int:id>/', phone_views.phone_detail, name='phone-detail'),

 ]