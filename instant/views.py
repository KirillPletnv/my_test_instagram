from django.contrib.auth.decorators import login_required
#import os
#import cv2
#import cvlib as cv
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.backends import django
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.views.generic import DetailView
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Image, User, Images, Comment, Comms, Follows2
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, FormMixin, ModelFormMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.db import models
import django.middleware.csrf
from  django.shortcuts import get_object_or_404



def index(request):
    num_images = Image.objects.all().count()
    num_authors = User.objects.all().count()
    print(django.middleware.csrf.get_token(request))

    return render(request, 'index.html', context={'num_images': num_images, 'num_authors': num_authors } )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class ImageDetailView(FormMixin, DetailView):
    template_name = 'instant/image_detail.html'
    form_class = CommentForm
    model = Image


    def post(self, request, *args, **kwargs):
        """ Обработка POST при использовани FormMixin в DetailView """
        self.object = self.get_object()
        form = self.get_form()
        #print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("image_detail", kwargs={"pk": self.object.pk})


def authors(request, id):
    image = Image.objects.filter(author=id)
    auth = image[0].author
    user1 = request.user.id
    return render(request, 'author.html', {'image': image, 'auth': auth, 'user1':user1})

def usr(request, id):
    image = Image.objects.filter(author=id)
    user1 = request.user.id
    auth = image[0].author
    return render(request, 'user.html', {'image': image, 'auth': auth,  'user1':user1})


@csrf_exempt
def followed(request):
    if request.method == 'POST':
        print('testaq')
        user = request.user
        print(user)
        fol = Follows2.objects.get_or_create(userers=user)[0]
        print(fol)


        user2 = request.POST.get('auth')
        print(user2)
        fol.friends.add(user2)
        print(fol.friends.all())
        fol2 = Follows2.objects.filter(userers=user)[0]
        print(fol2.friends.all())
        print('testaq-final')
        user1 = request.user.id

    return redirect('success')



@login_required(login_url="/login/", redirect_field_name="redirect_to")
def followers(request):
    #followe = Follows2.objects.all()

    print(request.user.id)
    #follower = followe.friends.all()
    user = request.user
    follows = Follows2.objects.get_or_create(userers=user)[0]
    fol = follows.friends.all()
    #follower = Follows.objects.get(userers=request.user).friends.all()
    user1 = request.user.id

    return render(request, 'followers.html', {'followers': follows, 'follows': fol,  'user1':user1})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@csrf_exempt
def image_view(request):
    user1 = request.user.id
    if request.method == 'POST':

        form = Images(request.POST, request.FILES)
        #print(form)
        #img = request.FILES.temporary_file_path()
        imagest = request.FILES['name']
        #g = imagest.temporary_file_path()
        print(imagest)
        #print(g)

        #image = cv2.imread(g)
        #box, label, count = cv.detect_common_objects(image)
        #for i in label:
        #    a_record = Genre.objects.get_or_create(gen=i)
        #    print(a_record[0].pk)
        #    print("this", i)
        #    if form.is_valid():
        #        just_created = form.save()
        #        print(just_created.id)
        #        new_image = Image.objects.get(id=just_created.id)
        #        new_image.genre.add(a_record[0].pk)
        #print(label)
        #for j in Genre.objects.all():
        #    print(j.pk)
        #    print(j)
        if form.is_valid():
            just_created = form.save()
            print(just_created.id)
            new_image = Image.objects.get(id=just_created.id)
        #
        #    new_image.genre.add(a_record)
        return redirect('success')

    else:
        form = Images()
        print(request.COOKIES)

    return render(request, 'upload.html', {'form': form,  'user1':user1})


def success(request):
    return HttpResponse('successfully uploaded')


def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Images = Image.objects.all()
        comments = Comment.objects.all()
        request.session['user'] = request.user.id
        definite = request.user.id
        print(request.session['user'])
        user1 = request.user.id

        # form = Comms(request.POST)

        # if form.is_valid():
        #    form.save()
        #    return redirect('success')

        return render(request, 'image_list.html', {'images': Images, 'user1':user1, 'definite': definite, 'comments': comments })



def authors(request, id):
    image = Image.objects.filter(author=id)
    auth = image[0].author
    user1 = request.user.id
    return render(request, 'author.html', {'image': image,  'user1':user1, 'auth': auth})



def display_images2(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Images = Image.objects.all()
        #Images1 = Image.objects.filter(genre=28)
        #Images2 = Image.objects.filter(genre=21)
        #Images3 = Image.objects.filter(genre=22)
        #Images4 = Image.objects.filter(genre=23)
        #Images5 = Image.objects.filter(genre=24)
        #Images6 = Image.objects.filter(genre=25)
        #Images7 = Image.objects.filter(genre=26)
        #Images8 = Image.objects.filter(genre=27)
        #Images9 = Image.objects.filter(genre=28)
        #Images10 = Image.objects.filter(genre=29)
        #Images11 = Image.objects.filter(genre=30)
        comments = Comment.objects.all()


        #print(len(Images2), '-')
        comments = Comment.objects.all()

        #imagened = [Images1, Images2, Images3, Images4, Images5, Images6, Images7, Images8, Images9, Images10, Images11]
        imgs = []
        #for img in imagened:
        #    if len(img) >= 1:
        #        for i in img:
        #            imgs.append(i)
        imagn = []
        n = 0
        while len(imagn) < len(Images) / 9:

            #imagn = [imgs[n:9]]
            imagn.append(Images[n:n+10])
            n += 9
        #print(len(imgs))
        #print(len(imagn))


        request.session['user'] = request.user.id
        definite = request.user.id
        print(request.session['user'])
        user1 = request.user.id


        # form = Comms(request.POST)

        # if form.is_valid():
        #    form.save()
        #    return redirect('success')

        return render(request, 'image_list2.html', {'images': Images, 'user1':user1, 'imagn': imagn, 'definite': definite, 'comments': comments})




def create(request):
    user1 = request.user.id
    if request.method == "POST":
        comment = Comment()
        comment.id = Image.objects.get(id=id)
        comment.post = comment.id
        comment.authors = request.POST.get("authors")
        comment.text = request.POST.get("text")
        comment.save()
        return HttpResponseRedirect("image_detail")


class PostList(generic.ListView):
    model = Image


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('images')


def comment_post(request):
    user1 = request.user.id
    if request.method == 'POST':
        form_comment = Comms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form_comment = Comms()
    return render(request, 'image_detail.html', {'form_comment': form_comment, 'user1':user1})





