# -*- coding: UTF-8 -*-

"""py2copyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [

    url("user_detail", views.user_detail),
    url("user_illusts$", views.user_illusts),
    url("user_illusts_parse_qs", views.user_illusts_parse_qs),
    url("illust_detail", views.illust_detail),
    url("illust_related$", views.illust_related),
    url("illust_related_parse_qs", views.illust_related_parse_qs),
    url("illust_recommended", views.illust_recommended),
    url("illust_ranking", views.illust_ranking),
    url("search_illust", views.search_illust),
    url("ranking_all$", views.ranking_all),
    url("ranking_all_parse_qs", views.ranking_all_parse_qs),
    url("image_download", views.image_download),
    url("ugoira_metadata", views.ugoira_metadata),
    url("trending_tags_illust", views.trending_tags_illust),

]
