from django.http import HttpResponse

import sys
from datetime import datetime, timedelta
from pixivpy3 import *
import json

if sys.version_info >= (3, 0):
    import imp
    imp.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


_REFRESH_TOKEN = "FZpHHpYzR-agDJF7okOXqzRyStbnscan73oegMM-FO8"


def pixivPassSniAuthApi():
    # api = AppPixivAPI()
    api = ByPassSniApi()
    api.require_appapi_hosts(hostname="public-api.secure.pixiv.net")
    api.set_accept_language('zh-cn')
    api.auth(refresh_token=_REFRESH_TOKEN)
    # api.login("lishalom@sina.com", "p6569653")
    return api


def pixivAuthApi():
    api = AppPixivAPI()
    api.set_accept_language('zh-cn')
    api.set_additional_headers(headers="Referer:https://app-api.pixiv.net/")
    api.auth(refresh_token=_REFRESH_TOKEN)
    # api.login("lishalom@sina.com", "p6569653")
    return api


def pixivApi():
    # api = AppPixivAPI()

    api = ByPassSniApi()
    api.require_appapi_hosts(hostname="public-api.secure.pixiv.net")
    api.set_accept_language('zh-cn')
    return api


# 获取作者详情
def user_detail(request):
    api = pixivPassSniAuthApi()
    json_result = api.user_detail(request.GET.get('user_id'))
    return HttpResponse(json.dumps(json_result))


# 用户作品列表 
def user_illusts(request):
    api = pixivPassSniAuthApi()
    json_result = api.user_illusts(request.GET.get('user_id'))
    return HttpResponse(json.dumps(json_result))
    

# 用户作品列表-下一页 (.parse_qs(next_url) 用法)
def user_illusts_parse_qs(request):
    api = pixivPassSniAuthApi()
    next_qs = api.parse_qs(request.GET.get('next_url'))
    json_result = api.user_illusts(**next_qs)
    return HttpResponse(json.dumps(json_result))
    

# 作品详情 (无需登录，同PAPI.works)
def illust_detail(request):
    api = pixivPassSniAuthApi()
    json_result = api.illust_detail(request.GET.get('illust_id'))
    return HttpResponse(json.dumps(json_result))


# 相关作品列表
def illust_related(request):
    api = pixivPassSniAuthApi()
    json_result = api.illust_related(request.GET.get('illust_id'))
    return HttpResponse(json.dumps(json_result))


# 作品相关推荐-下一页 (.parse_qs(next_url) 用法)
def illust_related_parse_qs(request):
    api = pixivPassSniAuthApi()
    next_qs = api.parse_qs(request.GET.get('next_url'))
    json_result = api.illust_related(**next_qs)
    return HttpResponse(json.dumps(json_result))


# 插画推荐 (Home - Main) 
# content_type: [illust, manga]
def illust_recommended(request):
    api = pixivPassSniAuthApi()
    json_result = api.illust_recommended()
    return HttpResponse(json.dumps(json_result))


# xxxx-xx-xx的过去一周排行
def illust_ranking(request):
    api = pixivPassSniAuthApi()
    json_result = api.illust_ranking('week', date=request.GET.get('date'))
    return HttpResponse(json.dumps(json_result))


# 按标签搜索作品
def search_illust(request):
    api = pixivPassSniAuthApi()
    json_result = api.search_illust(request.GET.get('keyword'))
    return HttpResponse(json.dumps(json_result))


# 排行榜/过去排行榜
# mode:
#   daily - 每日
#   weekly - 每周
#   monthly - 每月
#   male - 男性热门
#   female - 女性热门
#   original - 原创
#   rookie - Rookie
#   daily_r18 - R18每日
#   weekly_r18 - R18每周
#   male_r18
#   female_r18
#   r18g
def ranking_all(request):
    api = pixivPassSniAuthApi()
    json_result = api.ranking_all(request.GET.get('mode'), 1, 50)
    return HttpResponse(json.dumps(json_result))


# 下载图片
def image_download(request):
    api = pixivPassSniAuthApi()
    json_result = api.download(request.GET.get('image_url'), "", request.GET.get('path'))
    return HttpResponse(json.dumps(json_result))


# 获取图片ZIP信息
def ugoira_metadata(request):
    api = pixivPassSniAuthApi()
    json_result = api.ugoira_metadata(request.GET.get('illust_id'))
    return HttpResponse(json.dumps(json_result))


# 趋势标签 (Search - tags) 
def trending_tags_illust(request):
    api = pixivPassSniAuthApi()
    json_result = api.trending_tags_illust()
    return HttpResponse(json.dumps(json_result))