#-*-coding:utf8-*-
from django.db import models

# Create your models here.
class pybugs(models.Model):
    title = models.CharField(max_length=300)#标题
    content = models.TextField()#内容
    remarks = models.TextField()#备注
    project = models.IntegerField()#项目id
    module = models.IntegerField()#模块id
    creater = models.IntegerField()#创建人id
    ccer = models.IntegerField()#抄送人id
    assigner = models.IntegerField()#指派人id
    fixer = models.IntegerField()#修复人id
    fixTime = models.DateTimeField()#修复时间
    fixWay = models.CharField(max_length=20)#解决方案
    closer = models.IntegerField()#关闭人id
    priority = models.CharField(max_length=20)#优先级
    serious = models.CharField(max_length=20)#严重级别
    closeTime = models.DateTimeField()#关闭时间
    createTime = models.DateTimeField()#创建时间
    updateTime = models.DateTimeField()#更新时间
    duplicateID = models.IntegerField()#重复bug
    relatedBugID = models.IntegerField()#关联bug id
    relatedCaseID = models.IntegerField()#关联用例 id
    file = models.FileField(upload_to = './upload/')#附件
    status = models.IntegerField()#状态

