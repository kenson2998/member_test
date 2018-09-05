# member_test
Django使用session會員登入,以及簡單的ajax聊天室
## 訪客首頁  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_1.jpg)
## 註冊判斷輸入的帳號、密碼、Email判斷  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_2.jpg)
## 右上登入頁面  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_3.jpg)
## 聊天室  
必須登入才能訪問聊天室頁面，否則會跳回首頁
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_4.jpg)
## 每秒利用ajax的方式回傳聊天室是否有更新訊息，發訊息也是利用ajax post留言，即時更新
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_5.jpg)
## 判斷自己的留言會顯示 藍色框底，清楚自己發訊息有哪些，移到上面可以看到留言時間。
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_6.jpg)
執行Django:
>python manage.py runserver localhost:80

開啟瀏覽器進入網址: http://localhost

可以立刻註冊一個帳號，建立後右上角登入後，就記錄在session裡面，下次訪問時就會檢查session是否有存留。

更換瀏覽器訪問和按下登出或是runserver重啟，就會清除session資料。  
  


# 英雄資料demo
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/champ_demo3.jpg)
[看實例網址在這](http://loltwgg.herokuapp.com/champ/Elise/)
運用到的工具:  
[semantic-ui](https://semantic-ui.qyears.com/)、[w3school-Slideshow](https://www.w3schools.com/howto/howto_js_slideshow.asp)。  
嘗試寫看看一個介紹英雄技能的頁面並包含skin一覽。  
把之前練習的ajax請求方法拿來使用，不過這次是使用GET。

1.將主框架寫在champ-jpg.html上。  
2.將主框架請求GET ($.get("/champ_p/",{chname: '英雄英文名字')傳給champ-jpg1.html去做資料html格式處理。
3.將處理完的資料寫入到主框架的"ch_cont" div裡面，再資料呈現之前會預設呈現寫好的"載入中"動畫。


### ajax請求部分
如果不需要csrf可以拿掉。  
```javascript
<script>
$(document).ready(function() {
    $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
    $.get("/champ_p/",{chname: $('.aicon').attr('al')},
        function(data){
        $('#ch_cont').html(data);
    });
});
</script>
```
### 技能呈現的部分
view.py 加入的部分
```python
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

```
champ-jpg1.html 主要呈現技能的部分
```
{% for skill in resp.spells %}
    <div class="item">
        <div class="ui">
            <img class='skill' src="{{s_url}}{{skill.image.full}}">
        </div>
        <div class="content">
            <a class="header">{{skill.name}}</a>
            <div class="meta">
                <span>{{skill.description|safe}}</span>
            </div>
            <div class="description">
                {{skill.tooltip|safe}}
            </div>
            <div class="extra">

            </div>
        </div>
    </div>

{% endfor %}
```
champ-jpg1.html 造型資料呈現部分。
```
<div class="slideshow-container">
    {% for skin in resp.skins %}
        <div class="mySlides fade">
            <div class="numbertext">{{ skin.num|add:"1" }} / {{ resp.skins|length }}</div>
            <img class="nature loading" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{{champ}}_{{skin.num}}.jpg" >
            <div class="text"> {% if skin.name == "default" %} 原造型{% else %}{{skin.name}}{% endif %}</div>
        </div>
    {% endfor %}

    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>

    <br>

    <div style="text-align:center">
        {% for skin in resp.skins %}
          <span class="dot" onclick="currentSlide({{ skin.num|add:"1" }})"></span>
        {% endfor %}
    </div>
```
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/champ_demo1.jpg)

![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/champ_demo2.jpg)