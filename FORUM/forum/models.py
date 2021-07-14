from django.db import models 

#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    fid = models.AutoField(primary_key=True)
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(null = True,max_length=300)
    description = models.CharField(null = True,max_length=1000,blank=True)
    link = models.CharField(null = True,max_length=100)
    date_created=models.DateField(auto_now_add=True,null=True)
    privacy = models.CharField(null= True,max_length=100,default="Private")

class Thread(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,default="anonymous" )
    tid = models.AutoField(primary_key=True)
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(null = True,max_length=300)
    description = models.CharField(null = True,max_length=1000,blank=True)
    link = models.CharField(null = True,max_length=100)
    date_created=models.DateField(auto_now_add=True,null=True)
    privacy = models.CharField(null= True,max_length=100,default="Private")

#child model
class Reply_thread(models.Model):
    thread = models.ForeignKey(Thread,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    repid = models.AutoField(primary_key=True)
    reply = models.CharField(max_length=1000)


class memeber_info(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    email = models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,default="anonymous" )

