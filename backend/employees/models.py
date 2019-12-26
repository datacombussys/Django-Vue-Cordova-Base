from django.db import models

# Create your models here.
from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib import auth

from project.settings import base
# from users.models import MainUserManager

# from employees.helper import auto_incriment

# Employee Model Manager
class EmployeeManager(models.Manager):
  def create_employee(self, email, first_name, last_name, salary=None, password=None, username=None,  
									mobile_phone=None, home_address=None, home_city=None, home_state=None, 
									home_zip=None, bio=None, salary_type=None, position_title=None, work_phone=None, 
                  hire_date=None, ssn=None, dob=None):
    # Create Employee using email address as login id
    print(self)
    userModel = auth.get_user_model()
    user = userModel.objects.create_user(
      email=email,
      password=password,
			first_name = first_name,
			last_name = last_name,
			username = username,
			mobile_phone = mobile_phone,
			home_address = home_address,
			home_city = home_city,
			home_state = home_state,
			home_zip = home_zip,
			bio = bio,
      is_staff= True,
    )
    saved_user = userModel.objects.last()
    employee = Employee(
      user = saved_user,
      salary = salary,
      salary_type = salary_type,
      position_title = position_title,
      work_phone = work_phone,
      status = True,
      hire_date = hire_date,
      ssn = ssn,
      dob = dob,
    )
    
    employee.save(using=self._db)
    return employee

    #Bind employee to Group
      #if user == datacom admin then fire datcom group method
      #if user == partner admin then fire partner group method
      #if user == company admin then fire company group method

    #Bind employee to Merchant
      #if current usergroup == datacom admin then add to choice of companies and partners and self.datacom
      #if current usergroup == partner admin then add to choice of companies and self.partner
      #if current usergroup == company admin then add to current self.company

  def create_employeeadmin(self, email, first_name, last_name, salary=None, password=None, username=None,  
									mobile_phone=None, home_address=None, home_city=None, home_state=None, 
									home_zip=None, bio=None, salary_type=None, position_title=None, work_phone=None, 
                  hire_date=None, ssn=None, dob=None, is_staff=None, is_admin=None):
    # Create Admin Employee using email address as login id
    userModel = auth.get_user_model()
    user = userModel.objects.create_user(
      email=email,
      password=password,
			first_name = first_name,
			last_name = last_name,
			username = username,
			mobile_phone = mobile_phone,
			home_address = home_address,
			home_city = home_city,
			home_state = home_state,
			home_zip = home_zip,
			bio = bio,
      is_staff= is_staff,
      is_admin= is_admin,
    )
    saved_user = userModel.objects.last()
    employee = Employee(
      user = saved_user,
      salary = salary,
      salary_type = salary_type,
      position_title = position_title,
      work_phone = work_phone,
      status = True,
      hire_date = hire_date,
      ssn = ssn,
      dob = dob,
    )
    
    employee.save(using=self._db)
    return employee

  def set_employee_groups(self, perm, obj):
      employee = Employee.objects.filter(id = obj.id)
      avaialble_permissions = EmployeePermissions.objects.all()
      if not perm in avaialble_permissions:
        raise ValueError("You must supply a valid permission and user object")
      employee = Employee.objects.filter(id = obj.id)
      employee = self.model(
        user_permissions = obj.user_permissions + perm
      )
      employee.save()
      return self.user_permissions
  

# Employee Model
class Employee(models.Model):
  # SALARY = 'SALARY'
  # WAGES = 'WAGES'
  # SALARYORWAGE_CHOICES = [
  #   (SALARY, 'Salary'),
  #   (WAGES, 'Hourly'),
  # ]
  # FULL_TIME = 'FULL_TIME'
  # PART_TIME = 'PART_TIME'
  # SEASONAL = 'SESONAL'
  # TEMPORARY = 'TEMPORARY'
  # EMPLOYEETYPE_CHOICES = [
  #   (FULL_TIME, 'Full Time'),
  #   (PART_TIME, 'Part Time'),
  #   (SEASONAL, 'Seasonal'),
  #   (TEMPORARY, 'Temporary'),
  # ]
  # ACTIVE = 'ACTIVE'
  # INACTIVE = 'INACTIVE'
  # SALARYORWAGE_CHOICES = [
  #   (ACTIVE, 'Active Profile'),
  #   (INACTIVE, 'Inactive Profile'),
  # ]
  user              = models.OneToOneField(base.AUTH_USER_MODEL, on_delete=models.CASCADE)
  employee_id       = models.CharField(max_length=9, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  salary            = models.IntegerField(blank=True, null=True)
  salary_type       = models.CharField(max_length=2, blank=True, null=True)
  position_title    = models.CharField(max_length=50, blank=True, null=True)
  employee_type     = models.CharField(max_length=12, blank=True, null=True)
  work_phone        = models.CharField(max_length=10, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  status            = models.BooleanField(default=True)
  hire_date         = models.DateField(auto_now_add=True)
  termination_date  = models.DateField(auto_now_add=False, blank=True, null=True)
  termination_reason= models.CharField(max_length=250, blank=True, null=True)
  ssn               = models.CharField(max_length=9, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,9}$')])
  dob               = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
  barcode           = models.CharField(max_length=10, null=True, 
									    blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
  employee_type     = models.CharField(max_length=100, null=True, blank=True)

  objects	= EmployeeManager()
  
  class Meta:
    ordering = ['user']


