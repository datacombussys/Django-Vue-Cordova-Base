from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from project.settings import base
from django.core.validators import RegexValidator

from datacom.common_models import CommonCompanyBase
from employees.models import Employee
from customers.models import Customer


# Company / Merchant Model Manager
class CompanyManager(models.Manager):
  '''Create a company instance'''

  def create_company(self, dba_name, legal_name, description=None, main_phone=None, main_fax=None, 
    tax_id=None, corp_address=None, corp_city=None, corp_state=None, corp_zip=None, mailing_address=None, merchant_id=None,
    mailing_city=None, mailing_state=None, mailing_zip=None, website=None, account_number=None, barcode=None, 
    status=True, shipping_address=None, shipping_city=None, shipping_state=None, shipping_zip=None, primary_first_name=None, 
    primary_last_name=None, primary_phone=None, primary_email=None, billing_first_name=None, 
    billing_last_name=None, billing_phone=None, billing_email=None, resale_id=None, purchasing_terms=None, board_date=None, 
    acct_closure_date=None, closure_reason=None):
    if not dba_name:
      raise ValueError("User must enter a valid business name")
    if not legal_name:
      raise ValueError("User must enter a valid legal business name")
    
    company = self.model(
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
      merchant_id = merchant_id,
      status = status,
      primary_first_name = primary_first_name,
      primary_last_name = primary_last_name,
      primary_phone = primary_phone,
      primary_email = primary_email,
      purchasing_terms = purchasing_terms,
      board_date = board_date,
      acct_closure_date = acct_closure_date,
      closure_reason = closure_reason,
      )


    company.save(using=self._db)
    return company

# Company / Merchant Model
class Company(CommonCompanyBase):
  employee 		        = models.ManyToManyField(Employee, related_name='company_employees', blank=True)
  customer 		        = models.ManyToManyField(Customer, related_name='company_customers', blank=True)
  created_by 		      = models.OneToOneField(base.AUTH_USER_MODEL,  related_name="company_creator", on_delete=models.DO_NOTHING, blank=True, null=True)
  website 			      = models.CharField(max_length=100, blank=True, null=True)
  account_number      = models.CharField(max_length=16, null=True, blank=True, validators=[RegexValidator(r'^\d{1,16}$')])
  merchant_id         = models.CharField(max_length=9, null=True, 
									      blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  tax_id              = models.CharField(max_length=9, null=True, 
									      blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  barcode             = models.CharField(max_length=10, null=True, 
									      blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  status              = models.BooleanField(default=True)
  shipping_address 	  = models.CharField(max_length=20, blank=True, null=True)
  shipping_city 	  	= models.CharField(max_length=20, blank=True, null=True)
  shipping_state 		  = models.CharField(max_length=20, blank=True, null=True)
  shipping_zip 			  = models.CharField(max_length=5, null=True, 
                        blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
  primary_first_name  = models.CharField(max_length=50, blank=True, null=True)
  primary_last_name   = models.CharField(max_length=50, blank=True, null=True)
  primary_phone       = models.CharField(max_length=50, blank=True, null=True)
  primary_email       = models.CharField(max_length=50, blank=True, null=True)
  billing_first_name  = models.CharField(max_length=50, blank=True, null=True)
  billing_last_name   = models.CharField(max_length=50, blank=True, null=True)
  billing_phone       = models.CharField(max_length=50, blank=True, null=True)
  billing_email       = models.CharField(max_length=50, blank=True, null=True)
  resale_id           = models.CharField(max_length=20, null=True, 
									      blank=True, validators=[RegexValidator(r'^\d{1,20}$')])
  purchasing_terms    = models.CharField(max_length=250, blank=True, null=True)
  board_date          = models.DateField(auto_now_add=True)
  acct_closure_date   = models.DateField(auto_now_add=False, blank=True, null=True)
  closure_reason      = models.CharField(max_length=250, blank=True, null=True)

  objects	= CompanyManager()

def __str__(self):
  return self.dba_name
