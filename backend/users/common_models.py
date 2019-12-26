from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, Group


class CommonUserBase(AbstractBaseUser):
	email 				= models.EmailField(verbose_name="email", max_length=60, 										unique=True)
	username 			= models.CharField(max_length=30, unique=True)
	date_joined 	= models.DateTimeField(verbose_name="date joined", 														auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin			= models.BooleanField(default=False)
	ia_active			= models.BooleanField(default=True)
	is_staff			= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)

	full_name 		= models.CharField(max_length=50, blank=True)
	first_name 		= models.CharField(max_length=50, blank=True)
	last_name 		= models.CharField(max_length=50, blank=True)
	mobile_phone 	= models.IntegerField(blank=True, null=True)
	street_name 	= models.CharField(max_length=20, blank=True)
	city 					= models.CharField(max_length=20, blank=True)
	state 				= models.CharField(max_length=20)
	zip 					= models.IntegerField(blank=True, null=True)
	bio 					= models.TextField(blank=True)
	global_id 		= models.UUIDField(primary_key=False, default=uuid4, editable=False)
	


	class Meta:
		abstract = True

