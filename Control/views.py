from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View,generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from Home.models import purePerson,student,faculty
from Course.models import course


