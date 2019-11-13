from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from project.settings import base
from users.common_models import CommonUserBase, CommonCompanyBase, CommonGroup


class Company(CommonCompanyBase):
	created_by 		= models.ForeignKey(base.AUTH_USER_MODEL, related_name='usernames', 														on_delete=models.DO_NOTHING, blank=True)
	website 			= models.CharField(max_length=100, blank=True)


class UserManager(BaseUserManager):
	def create_user(self, email, username, password):
		# Create Standard User using email address as login id
		if not email:
				raise ValueError("User must enter a valied email address")
		if not password:
				raise ValueError("Users must have a valid password")
		user = self.model(
			email=self.normalize_email(email),
			username = username
		)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, username, password):
		# Create Superuser using email address as login id
		if not email:
				raise ValueError("User must enter a valied email address")
		if not password:
				raise ValueError("Users must have a valid password")
		user = self.create_user(
			email = self.normalize_email(email),
			password = password,
			username = username
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)									
		return user

		def create_employee(self, email, username, password, merchant, CommonGroup, is_admin=False):
			#Create Employee from MerchantEmployee Model
			if not merchant:
					raise ValueError("Employees must be registered with a merchant company")
			if not email:
					raise ValueError("User must enter a valied email address")
			if not password:
				raise ValueError("Users must have a valid password")
			user = self.create_user(
				email = self.normalize_email(email),
				password = password,
				username = username
			)
			merchant = request.UserProfile.Company.dba_name
			CommonGroupBase.is_employee = True
			user.save(using=self._db)									
			return user


class User(CommonUserBase):
	merchant 		= models.ManyToManyField(Company, related_name='dba_names', 									blank=True)
	rating 			= models.IntegerField(blank=True, null=True)
	is_admin 		= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects	= UserManager()

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
		return self.active

	def is_admin(self):
		return self.admin

	def is_staff(self):
		return self.staff

# Django already has the following field in the User:
# username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined
