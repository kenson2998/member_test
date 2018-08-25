from django.db import models

class Products (models.Model): #產品資料
    Products_ID = models.CharField(max_length=20) #產品編號
    Kind_ID = models.ManyToManyField('Product_kinds') #類別編號
    Supplier_ID = models.ManyToManyField('Suppliers') #供應商編號
    Pd_Name = models.TextField(blank=True) #產品名稱
    Price_Suggest = models.IntegerField(default=0) #建議單價
    Inventory = models.IntegerField(default=0) #庫存量

class Suppliers (models.Model): #供應商
    Supplier_ID = models.CharField(max_length=20) #供應商編號
    Supplier_Name = models.CharField(max_length=20) #供應商名稱

class Product_kinds (models.Model): #產品類別
    Kind_ID = models.CharField(max_length=20) #類別編號
    Kind_Name = models.CharField(max_length=20,blank=True) #類別名稱

class Order_Details (models.Model): #訂單明細
    Order_ID = models.ManyToManyField('Orders') #訂單編號
    Products_ID = models.ManyToManyField('Products') #產品編號
    Price_True = models.IntegerField(default=0) #實際單價
    Amount = models.IntegerField(default=0) #數量

class Orders (models.Model): #訂單
    Order_ID = models.CharField(max_length=20) #訂單編號
    Employee_ID = models.ManyToManyField('Employees') #員工編號
    Customer_ID = models.ManyToManyField('Customers') #客戶編號
    Order_Date = models.DateTimeField(auto_now_add=True) #訂單日期

class Employees (models.Model): #員工
    Employee_ID = models.CharField(max_length=20) #員工編號
    Employee_Name = models.CharField(max_length=20)  # 員工姓名

class Customers (models.Model): #客戶
    Customer_ID = models.CharField(max_length=20) #客戶編號
    Company_Name = models.CharField(max_length=20)  # 公司名稱
    Company_Contact = models.CharField(max_length=20)  # 聯絡人
    Tel = models.CharField(max_length=20,blank=True)  # 聯絡人


class Chat(models.Model):
    from django.contrib.auth.models import User
    import django.utils.timezone as timezone
    sender = models.ForeignKey(User, related_name='has_chats')
    content = models.TextField()
    time = models.DateTimeField(default = timezone.now, null=True)

    def __unicode__(self):
        return u'%s' % self.content