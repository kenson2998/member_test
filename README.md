# member_test
Django使用session會員登入,以及簡單的ajax聊天室

執行Django:
>python manage.py runserver localhost:80

開啟瀏覽器進入網址: http://localhost

可以立刻註冊一個帳號，建立後右上角登入後，就記錄在session裡面，下次訪問時就會檢查session是否有存留。

更換瀏覽器訪問和按下登出或是runserver重啟，就會清除session資料。
