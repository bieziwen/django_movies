from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.home.models import TFilm, TLogname, TClassname, TLocname, TOndecade


def test1(request):
    return HttpResponse('哈哈哈哈')


def update(request):
    films=TFilm.objects.all()
    for film in films:
        film.image=film.image[14:]
        film.save()
    return HttpResponse('hhh')

#模板全局变量

# @login_required(login_url='/account/login/')
def index(request):
    username=request.user.username
    li=['短视频','电影','电视剧','动漫']
    films1=TFilm.objects.filter(cata_log_id='f39c979857a4874a0157a4a6a4fe0000')
    films2=TFilm.objects.filter(cata_log_id='f39c979857a4c8c50157a8ea80700018')
    films3=TFilm.objects.filter(cata_log_id='f39c979857a4c8c50157a8eaaee30019')
    return render(request,'index.html',locals())

# @login_required(login_url='/account/login/')
def detail(request,id):
    username=request.user.username
    film=TFilm.objects.get(id=id)
    sub_class_name = film.sub_class_name
    films=TFilm.objects.filter(sub_class_name=sub_class_name)
    return render(request,'detail.html',locals())



def cate_movie(request):
    cates = TLogname.objects.all()
    subs = TClassname.objects.all()
    locs = TLocname.objects.all()
    years = TOndecade.objects.all()
    li = [item for item in range(1994, 2019)]
    li1 = sorted(li, reverse=True)
    li2 = ['分类', '子类', '地区', '年代']
    cata_log_id=request.GET.get('cata_log_id')
    sub_class_name=request.GET.get('sub_class_name')
    loc_id=request.GET.get('loc_id')
    year=request.GET.get('year')
    lis=[{'sub_class_name':sub_class_name},{'loc_id':loc_id},{'year':year}]
    urls,films=many_keys(lis,cata_log_id)
    # if cata_log_id:
    #     films=TFilm.objects.filter(cata_log_id=cata_log_id)
    # if sub_class_name:
    #     films=TFilm.objects.filter(sub_class_name=sub_class_name)
    # if loc_id:
    #     films=TFilm.objects.filter(loc_id=loc_id)
    # if year:
    #     films=TFilm.objects.filter(on_decade=year)
    return render(request,'cate.html',locals())


def many_keys(lis,cata_log_id):
    films = TFilm.objects.filter(cata_log_id=cata_log_id)
    urls=f'cata_log_id={cata_log_id}'
    for li in lis:
        for k,v in li.items():
            if v:
                if k=='sub_class_name':
                    films=films.filter(sub_class_name=v)
                    urls=urls+f'&{k}={v}'
                if k=='loc_id':
                    films = films.filter(loc_id=v)
                    urls = urls + f'&{k}={v}'
                if k=='year':
                    films = films.filter(on_decade=v)
                    urls = urls + f'&{k}={v}'
    return urls,films


# def detail(request,id):
#     username = request.user.username
#     film = TFilm.objects.get(id=id)
#     sub_class_name=film.sub_class_name
#     films=TFilm.objects.filter(sub_class_name=sub_class_name)
#     return render(request,'detail1.html',locals())



