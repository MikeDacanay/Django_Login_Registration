# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password= models.CharField(max_length=255)
	datehired= models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True) 
	updated_at = models.DateTimeField(auto_now = True)

class Items(models.Model):
	Item = models.CharField(max_length=255)
	creator= models.ForeignKey(Users, related_name="created_item")
	users = models.ManyToManyField(Users, related_name = "items")
	created_at = models.DateTimeField(auto_now_add = True) 
	updated_at = models.DateTimeField(auto_now = True)
