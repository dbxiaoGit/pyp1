from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    name = models.CharField(null=False, max_length=32)   # 创建一个varchar(20)类型的不能为空的字段

    def __str__(self):
        return "<{}-{}>".format(self.id, self.name)