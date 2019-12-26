from django.db import models
from django.utils import timezone
# from project.settings import base
from django.core.validators import RegexValidator

from datacom.common_models import CommonCompanyBase
from employees.models import Employee
from customers.models import Customer
# from datacom.helper import auto_increment

# Datacom SuperCompany Model Manager
class DatacomManager(models.Manager):
  def create_company(self, dba_name, legal_name, description=None, main_phone=None, main_fax=None, 
  tax_id=None, corp_address=None, corp_city=None, corp_state=None, corp_zip=None, mailing_address=None, 
  mailing_city=None, mailing_state=None, mailing_zip=None, website=None, account_number=None, barcode=None, 
  shipping_address=None, shipping_city=None, shipping_state=None, shipping_zip=None, billing_first_name=None, 
  billing_last_name=None, billing_phone=None, billing_email=None, resale_id=None):
    if not dba_name:
      raise ValueError("User must enter a valid business name")
    if not legal_name:
      raise ValueError("User must enter a valid Legal Business Name")
    datacom = self.model(
      dba_name= dba_name,
      legal_name = legal_name,
      description = description,
      main_phone = main_phone,
      main_fax = main_fax,
      tax_id = tax_id,
      corp_address = corp_address,
      corp_city = corp_city,
      corp_state = corp_state,
      corp_zip = corp_zip,
      mailing_address = mailing_address,
      mailing_city = mailing_city,
      mailing_state = mailing_state,
      mailing_zip = mailing_zip,
      website = website,
      account_number = account_number,
      # account_number = auto_incriment.create_account_Number(),
      barcode = barcode,
      shipping_address = shipping_address,
      shipping_city = shipping_city,
      shipping_state = shipping_state,
      shipping_zip = shipping_zip,
      billing_first_name = billing_first_name,
      billing_last_name = billing_last_name,
      billing_phone = billing_phone,
      billing_email = billing_email,
      resale_id = resale_id,
  )
    datacom.save(using=self._db)	

# Datacom Model SuperCompany
class Datacom(CommonCompanyBase):
  class Meta:
    ordering = ['-created_at', 'dba_name']
  
  employee 		        = models.ManyToManyField(Employee, related_name='datacom_employees', blank=True)  
  customer 		        = models.ManyToManyField(Customer, related_name='datacom_customers', blank=True)
  created_by 		      = models.ForeignKey(Employee, related_name='datacom_creator', 
                        on_delete=models.DO_NOTHING, blank=True, null=True)
  website 			      = models.CharField(max_length=100, blank=True, null=True)
  account_number      = models.CharField(max_length=16, null=True, blank=True, validators=[RegexValidator(r'^\d{1,16}$')])
  barcode             = models.CharField(max_length=10, null=True, 
									      blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  shipping_address 	  = models.CharField(max_length=20, blank=True, null=True)
  shipping_city 	  	= models.CharField(max_length=20, blank=True, null=True)
  shipping_state 		  = models.CharField(max_length=20, blank=True, null=True)
  shipping_zip 			  = models.CharField(max_length=5, null=True, 
                        blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
  

  billing_first_name  = models.CharField(max_length=50, blank=True, null=True)
  billing_last_name   = models.CharField(max_length=50, blank=True, null=True)
  billing_phone       = models.CharField(max_length=50, blank=True, null=True)
  billing_email       = models.CharField(max_length=50, blank=True, null=True)
  resale_id           = models.CharField(max_length=20, blank=True, null=True, 
									      validators=[RegexValidator(r'^\d{1,20}$')])

  objects	= DatacomManager()

  def __str__(self):
    return self.dba_name


'''Types of Model inheritance
Abstract Inheritance - Provides a base class and inheriting classes use its fields to generate the new classes. 
There is  not base class generated in the database of the Abstract model. Use the folowing syntax
    Parent model class:
    class Meta:
    abstract = true

Multi-Table Inheritance - Used when each model (parent and child) in the hierarchy needs to have its own table in the database.

Proxy Inheritance - Inherit from base class and add own properties but not fields.  
Cannot add fields. Cannot Use abstract class. Can override parent models but not extend. Query would take place on the parent model.

'''
