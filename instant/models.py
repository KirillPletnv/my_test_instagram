from django.db import models
from django.urls import reverse
from django import forms
from django.views import generic
from django.contrib.auth.models import User
from django.conf import settings




class Genre(models.Model):
    gen = models.CharField(max_length=30)

    def __str__(self):
        return self.gen


class Image(models.Model):
    name = models.FileField(upload_to='images1/', help_text='выберите файл')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    inserts = models.ManyToManyField('Comment')
    description = models.CharField(max_length=120, null=True)
    #genre = models.ManyToManyField('Genre')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])


class Follows2(models.Model):
    userers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person1')
    friends = models.ManyToManyField(User, related_name='person2')

    def __str__(self):
        return ' {}:  {}'.format(self.userers,  self.friends)


#class User(models.Model):
#    nickname = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.nickname.username


#class Account(models.Model):
#    login = models.CharField(max_length=20)
#    password = models.CharField(max_length=20)
#    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)


class Comment(models.Model):
    post = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=120)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment by {}:  {}'.format(self.authors,  self.text)

class Images(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['author', 'name', 'description']


class Comms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'authors', 'text']



class CommentList(generic.ListView):
    model = Comment

class PostList(generic.ListView):
    model = Image