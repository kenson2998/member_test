from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth,UserManager
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import sema_member.models as sm

def index(request):
    import datetime
    if "username" in request.session:
        username=request.session['username']
        message =request.session['message']

    else:
        username="訪客"
        request.session['message']=''

    # response = HttpResponse('訪問次數為:'+str(counter))
    # tomorrow = datetime.datetime.now()+datetime.timedelta(days=1)
    # tomorrow = datetime.datetime.replace(tomorrow,hour=0,minute=0,second=0)
    # expires = datetime.datetime.strftime(tomorrow,"%a, %d-%b-%Y %H:%M:%S GMT")
    # response.set_cookie('visit',counter,expires=expires)


    return render(request, 'index.html',locals())

def show(request):
    chats = list(reversed(sm.Chat.objects.all()))[-10:]
    for i in chats:
        i.time=i.time.strftime("%Y-%m-%d %H:%M:%S")
        print(i.time)
        # print(i.time.strftime("%Y-%m-%d %H:%M:%S"))

def login (request):

    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None :
            if user.is_active :
                auth.login(request,user)
                request.session['message']=username + "您好!登入成功"
                status = "login"
                UID=User.objects.get(username=username)
                request.session['username'],request.session['id']=username=username,UID.id

                return redirect(index)
            else:
                message="帳號尚未啟用!"
        else:
            message="登入失敗!"
    else:
        if not "username" in request.session:
            message = '請先登入系統'
        else:
            message = '已登入'
            return redirect(index)

    return render(request,'login.html',locals())

def logout(request):
    if 'username' in request.session:
        message=request.session['username']+'您已登出'
        del(request.session['username'])
    return redirect(index)


def database(request):
    if 'username' in request.session:
        username=request.session['username']
        if request.method == "GET":
            a=request.GET.get('key')
            if a == 'auth_user' :
                a = User.objects.filter(username=username)
            if a == 'all':
                a = User.objects.all()
        return render(request, 'database.html', locals())

    else:

        return redirect(login)

def sign(request):
    uname,pwd,email=request.POST.get('username'),request.POST.get('password'),request.POST.get('email')
    # User.objects.create(username=uname,password=pwd,email=email)
    u = User()
    u.username = uname
    u.set_password(pwd)
    u.email = email
    u.save()
    # u=UserManager()
    # u.create_user(username = uname)

    return redirect(index)


@csrf_exempt
def msg (request):
    sm.Chat.objects.create(content=request.POST.get('content'), sender_id=request.session['id'])
    # chats = sm.Chat.objects.filter(id__gt=4)
    # print(chats)
    return HttpResponse()

def chatroom(request):
    if 'username' in request.session:
        username=request.session['username']
    chats = list(reversed(sm.Chat.objects.all()))[:10]
    # for i in chats :
        # i.time = i.time.strftime("%H:%M:%S")
    return render(request, 'chat.html', locals())

def fresh(request):
    last_chat_id = int(request.POST.get('last_chat_id'))
    chats = sm.Chat.objects.filter(id__gt = last_chat_id)
    # for i in chats :
        # i.time = i.time.strftime("%H:%M:%S")
    return render(request,'chat-list.html',{'chats':chats})




#---------practice------------------------------------------
def createacc(request):
    return render(request, 'createacc.html')
def set_cookie(request):
    response = HttpResponse('cookie save')
    response.set_cookie('name','le',max_age=10)
    return response
def get_cookie(request):
    if 'name' in request.COOKIES:
        return HttpResponse('%s : %s' %('name',request.COOKIES['name']))
        # return HttpResponse(request.COOKIES)
    else:
        return HttpResponse('no 存在')
def set_session(request,key=None,value=None):
    response = HttpResponse('session save')
    request.session[key]=value
    return response
def get_session(request,key=None):
    if key in request.session:
        return HttpResponse('%s : %s' %(key,request.session[key]))
        # return HttpResponse(request.COOKIES)
    else:
        return HttpResponse('noss 存在')
def del_session(request):
    # del(request.session)
    request.session.clear()
    resz= HttpResponse('del')
    resz.delete_cookie('counter')
    response = HttpResponse('dele')
    return response

def vote(request):
    if not "vote" in request.session:
        request.session["vote"] = 1
        msg="您第一次投票"
    else:
        msg='您已投過票'

    response = HttpResponse(request.session["vote"])
    return response


def champ_know (request):
    champ='Elise'
    return render(request, 'champ-jpg.html',locals())

def champ_p(request):
    import requests
    import json
    dd_ver = '8.17.1'
    if 'chname' in request.GET :
        champ=request.GET.get('chname')
    httml = ['https://ddragon.leagueoflegends.com/cdn/' + dd_ver + '/data/zh_TW/champion.json',
             'https://ddragon.leagueoflegends.com/cdn/' + dd_ver + '/data/zh_TW/champion/'+champ+'.json',
             'https://ddragon.leagueoflegends.com/cdn/' + dd_ver + '/img/sprite/spell0.png',
             'https://ddragon.leagueoflegends.com/cdn/' + dd_ver +'/img/spell/',
             'https://ddragon.leagueoflegends.com/cdn/' + dd_ver + '/img/passive/Aatrox_Passive.AatroxUpdate.png',
             'https://ddragon.leagueoflegends.com/cdn/img/champion/loading/'+champ+'_0.jpg'
             ]
    s_url='https://ddragon.leagueoflegends.com/cdn/' + dd_ver +'/img/spell/'
    pa_url='https://ddragon.leagueoflegends.com/cdn/' + dd_ver +'/img/passive/'
    req = requests.get(httml[1])
    resp = json.loads(req.text)
    resp = resp['data'][champ]
    return render(request, 'champ-jpg1.html',locals())
