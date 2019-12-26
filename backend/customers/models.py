from django.db import models

# Create your models here.
from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# from django.contrib.auth.models import UserManager

from project.settings import base

from employees.models import Employee



# Customer Model Manager
class CustomerManager(models.Manager):
  """ Model Manager for Customers to create Customers and check permissions """
 
  def create_customer(self, email, username=None, password=None, **extra_fields):
    # Create Standard Customer using User Model
    if not email:
      raise ValueError("User must enter a valied email address")
    if not password:
      raise ValueError("Users must have a valid password")
    customer = UserManager.create_user(self,
      email = self.normalize_email(email),
      username = username,
      password = password,
      first_name = extra_fields['first_name'],
      last_name = extra_fields['last_name']
    )
    customer.status = True
    
    #Set Customer Attributes
    
    #Bind employee to Group paid or free
      #Custoemrs have a group with no permissions except to view own profile

    #Bind employee to Merchant
      #Any user can add an employee to their company

    #Save Customer
    customer.save(using=self._db)
    return customer
  



# Customer Model
class Customer(models.Model):
  user              = models.OneToOneField(base.AUTH_USER_MODEL, on_delete=models.CASCADE)
  sales_rep         = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, blank=True)
  customer_id       = models.CharField(max_length=9, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  company_name      = models.CharField(max_length=250, blank=True, null=True)
  dob               = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
  ssn               = models.CharField(max_length=9, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  barcode           = models.CharField(max_length=10, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  mailing_address 	= models.CharField(max_length=20, null=True, blank=True)
  status            = models.BooleanField(default=True)
  mailing_city 	  	= models.CharField(max_length=20, null=True, blank=True)
  mailing_state 		= models.CharField(max_length=20, null=True, blank=True)
  mailing_zip 			= models.CharField(max_length=5, null=True, 
                      blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
  resale_id         = models.CharField(max_length=20, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,20}$')])
  customer_type     = models.CharField(max_length=100, null=True, blank=True)
 
  objects	= CustomerManager()
  
  def __str__(self):
    return self.full_name

  def has_perm(self, perm, obj=None):
    # I can place logic here to set permissions for site in general?
    "Does the user have a specific permission?"
    return print("This is the has_perm method")

  def has_module_perms(self, app_label):
    # I can put logic in here to set permissions for each module in a Dictionary and return T/F accordingly
    "Does the user have permissions to view the app `app_label`?"
    return True

  def get_fullname():
    return self.full_name

  def is_active(self):
    "Is the user a member of staff?"
    return self.is_active


