from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, Permission


# User Model Manager
class MainUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None, username=None,  
									mobile_phone=None, home_address=None, home_city=None, home_state=None, 
									home_zip=None, bio=None, is_staff=None, is_admin=None):
		if not email:
			raise ValueError("User must enter a valied email address")
		if not password:
			raise ValueError("Users must have a valid password")
		user = self.model(
			email=self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			username = username,
			mobile_phone = mobile_phone,
			home_address = home_address,
			home_city = home_city,
			home_state = home_state,
			home_zip = home_zip,
			bio = bio,
			full_name = first_name + " " + last_name,
			
			)
		
		user.is_staff= is_staff
		user.is_admin= is_admin

		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, first_name, last_name, password=None, username=None,  mobile_phone=None, home_address=None, home_city=None, home_state=None, 
											home_zip=None, bio=None):
		# Create Superuser using email address as login id
		if not email:
				raise ValueError("User must enter a valied email address")
		if not password:
				raise ValueError("Users must have a valid password")
		superuser = self.create_user(
			email=self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			password = password,
			username = username,
			mobile_phone = mobile_phone,
			home_address = home_address,
			home_city = home_city,
			home_state = home_state,
			home_zip = home_zip,
			bio = bio,

			)
		superuser.is_admin = True
		superuser.is_staff = True
		superuser.is_superuser = True

		superuser.save(using=self._db)									
		return superuser

# User Model
class User(AbstractBaseUser):
	email 				= models.EmailField(verbose_name="email", max_length=60, 										
									unique=True)
	username 			= models.CharField(max_length=30, unique=True, null=True, blank=True)
	full_name 		= models.CharField(max_length=50, blank=True, null=True)
	first_name 		= models.CharField(max_length=50, blank=True, null=True)
	last_name 		= models.CharField(max_length=50, blank=True, null=True)
	date_added 		= models.DateTimeField(verbose_name="date joined", 														
									auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin			= models.BooleanField(default=False)
	is_active			= models.BooleanField(default=True)
	is_staff			= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)
	mobile_phone 	= models.CharField(max_length=10, null=True, 
									blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
	home_address 	= models.CharField(max_length=20, blank=True, null=True)
	home_city 		= models.CharField(max_length=20, blank=True, null=True)
	home_state 		= models.CharField(max_length=20, blank=True, null=True)
	home_zip 			= models.CharField(max_length=5, null=True, 
									blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
	bio 					= models.TextField(blank=True, null=True)
	global_id 		= models.UUIDField(primary_key=False, default=uuid4, editable=False)
	
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects	= MainUserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		# I can place logic here to set permissions for site in general?
		"Does the user have a specific permission?"
		return self.is_admin

	def has_module_perms(self, app_label):
		# I can put logic in here to set permissions for each module in a Dictionary and return T/F accordingly
		"Does the user have permissions to view the app `app_label`?"
		return True

	def get_fullname():
		return self.full_name

	def is_active(self):
		"Is the user a member of staff?"
		return self.is_active

	def is_admin(self):
		if self.user.is_admin == True:
			print("Absolutely")
			return is_admin

	def is_staff(self):
		return self.is_staff


#Django Permissions Model and Manager
# Django already has the following field in the User:
# username, first_name, last_name, email, password, groups, 
# user_permissions, is_staff, is_active, is_superuser, last_login, date_joined

class UserGroups(Group):
	# Inherits with name, and ID
	date_added      = models.DateField(verbose_name="date joined", 														
										auto_now_add=True)
	group_type      = models.CharField(max_length=100, null=True, blank=True)
	group_class     = models.CharField(max_length=100, null=True, blank=True)


#Django Permissions Model 
class UserPermissions(Permission):
	# Inherits with name, content_type(model) and codename (of permission in the model)
	date_added 						= models.DateField(verbose_name="date joined", 														
                					auto_now_add=True)
	permission_category   = models.CharField(max_length=100, null=True, blank=True)

