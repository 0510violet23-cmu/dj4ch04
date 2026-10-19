from django.shortcuts import redirect, render
from django.http import Http404
from datetime import datetime
from mysite.models import Post, Product


# 新聞直播頻道
TV_LIST = [
    {
        'name': '中天',
        'tvcode': 'wUPPkSANpyo',
        'official_url': 'https://www.youtube.com/live/we6ZSwxyS30?si=6IMPoiE6uN15f80o'
    },
    {
        'name': '華視',
        'tvcode': 'wMOg8EoUZ_E',
        'official_url': 'https://www.youtube.com/live/wM0g8EoUZ_E?si=tg5mkZOiXlM2S4zm'
    },
    {
        'name': '民視',
        'tvcode': 'yguQ1SzPM5U',
        'official_url': 'https://www.ftvnews.com.tw/'
    },
    {
        'name': '中視',
        'tvcode': 'TCnaIE_SAtM',
        'official_url': 'https://www.ctv.com.tw/'
    },
]


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def about(request):
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())


def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')

    return render(request, 'disp.html', locals())


# 新聞直播
def news_live(request, tvno=0):

    # 如果網址輸入不存在的頻道編號，就回到新聞直播首頁
    if not 0 <= tvno < len(TV_LIST):
        return redirect('news-live-home')

    tv_list = TV_LIST
    tv = tv_list[tvno]
    now = datetime.now()

    return render(request, 'news.html', {
        'tv': tv,
        'tvno': tvno,
        'tv_list': tv_list,
        'now': now,
    })

def musiclist(request, category=0):

    music_category = [
        '華語音樂',
        '西洋音樂',
        '日韓音樂',
        '純音樂'
    ]

    music_list = [
        ['流行歌曲', '抒情歌曲', '樂團歌曲'],
        ['Pop', 'Rock', 'Country'],
        ['J-POP', 'K-POP', '動漫歌曲'],
        []
    ]

    category_name = music_category[category]
    songs = music_list[category]

    return render(request, 'musiclist.html', locals())
