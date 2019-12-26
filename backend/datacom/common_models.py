from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group


class CommonCompanyBase(models.Model):
  
  dba_name 			      = models.CharField(max_length=200)
  legal_name 		      = models.CharField(max_length=200)
  description 	      = models.TextField(blank=True, null=True)
  created_at 		      = models.DateTimeField(default=timezone.now, editable=False)
  main_phone 		      = models.CharField(max_length=10, null=True, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  main_fax 		        = models.CharField(max_length=10, null=True, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  tax_id              = models.CharField(max_length=9, null=True, blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  global_id 		      = models.UUIDField(primary_key=False, default=uuid4, editable=False)
  corp_address 	      = models.CharField(max_length=20, blank=True, null=True)
  corp_city 	  	    = models.CharField(max_length=20, blank=True, null=True)
  corp_state 		      = models.CharField(max_length=20, blank=True, null=True)
  corp_zip 			      = models.CharField(max_length=5, null=True, 
                        blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
  mailing_address     = models.CharField(max_length=200, blank=True, null=True)
  mailing_city        = models.CharField(max_length=200, blank=True, null=True)
  mailing_state       = models.CharField(max_length=200, blank=True, null=True)
  mailing_zip         = models.CharField(max_length=5, null=True, blank=True, validators=[RegexValidator(r'^\d{1,5}$')])
  
  class Meta:
      abstract 	= True


