# member_test
Django使用session會員登入,以及簡單的ajax聊天室

執行Django:
>python manage.py runserver localhost:80

開啟瀏覽器進入網址: http://localhost

可以立刻註冊一個帳號，建立後右上角登入後，就記錄在session裡面，下次訪問時就會檢查session是否有存留。

更換瀏覽器訪問和按下登出或是runserver重啟，就會清除session資料。  
  
# 訪客首頁  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_1.jpg)
# 註冊判斷輸入的帳號、密碼、Email判斷  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_2.jpg)
# 右上登入頁面  
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_3.jpg)
# 聊天室  
必須登入才能訪問聊天室頁面，否則會跳回首頁
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_4.jpg)
# 每秒利用ajax的方式回傳聊天室是否有更新訊息，發訊息也是利用ajax post留言，即時更新
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_5.jpg)
# 判斷自己的留言會顯示 藍色框底，清楚自己發訊息有哪些，移到上面可以看到留言時間。
![](https://raw.githubusercontent.com/kenson2998/member_test/master/img/member_6.jpg)