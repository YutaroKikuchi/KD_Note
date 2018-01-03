from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, user_name, password):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		if not user_name :
			raise ValueError('Users must have an user name')

		if not password :
			raise ValueError('users must have a password')

		user = self.model(
			email=self.normalize_email(email),
			user_name=user_name,
			password=password
		)

		user.set_password(password)
		user.set_create_date()
		user.set_update_date(timezone.now())
		user.save(using=self._db)
		return user

	def create_superuser(self, email, user_name, password):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		if not user_name :
			raise ValueError('Users must have an user name')

		if not password :
			raise ValueError('users must have a password')

		user = self.model(
			email=self.normalize_email(email),
			user_name=user_name,
			password=password
		)

		#user.is_staff = True
		user.set_admin()
		user.set_password(password)
		user.set_create_date()
		user.set_update_date(timezone.now())
		user.save(using=self._db)
		return user

class CustomUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
		primary_key=True
	)
	USERNAME_FIELD='email'
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	user_name = models.CharField(verbose_name='user name',max_length=255)
	create_date = models.DateField()
	update_date = models.DateField()

	objects = UserManager()

	REQUIRED_FIELDS=['user_name']

	def get_full_name(self):
		return self.user_name

	def get_short_name(self):
		return self.user_name

	def set_create_date(self):
		self.create_date = timezone.now()
	
	def set_update_date(self, date):
		self.update_date = date
	
	def set_admin(self):
		self.is_admin = True

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
	
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

class Team(models.Model):
	team_name = models.CharField(max_length=64,unique=True,primary_key=True,default='DEFAULT NAME')

	def __str__(self):
		return self.team_name

class Score(models.Model):
	id = models.BigIntegerField(primary_key=True,default=1)
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	group = models.ForeignKey(Team, on_delete=models.SET_NULL,null=True)

	kill = models.IntegerField()
	death = models.IntegerField()

	win = models.BooleanField()

	RULES = (('FR','フラッグ戦'),
			('EL','全滅戦'),
			('GR','大将戦'),
			('RE','復活戦'),
			('ME','メディック戦'),
			('SP','スパイ戦'),
			('OD','攻守戦'),
			('HG','ハンドガン戦'),
			('FX','キツネ狩り'),
			('RE',' リアルカウント戦')
			)
	
	rule = models.CharField(max_length=2,choices=RULES,default='FR')

	date = models.DateField()

	def __str__(self):
		return str(self.id)