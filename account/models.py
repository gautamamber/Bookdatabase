from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #create user profile


# Create your models here.


class BookData(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	opening_balance = models.IntegerField(null = True, blank = False)
	copies_printed = models.IntegerField(null = True, blank = False)
	total_copies = models.IntegerField(null = True, blank = False)
	no_of_specimen_copies_issued = models.IntegerField(null = True, blank = False)
	defective_copies = models.IntegerField(null = True, blank = False)
	domestic_sales = models.IntegerField(null = True, blank = False)
	international_sales = models.IntegerField(null = True, blank = False)
	total_sales = models.IntegerField(null = True, blank = False)
	closing_stock = models.IntegerField(null = True, blank = False)
	royalty_rate = models.IntegerField(null = True, blank = False)
	royalty_amount = models.IntegerField(null = True, blank = False)
	total_royalty = models.FloatField(null = True, blank = False)
	advances = models.FloatField(null = True, blank = False)
	tds = models.FloatField(null = True, blank = False)
	net_amount_payable = models.FloatField(null = True,blank = False)
	payment_details = models.CharField( max_length = 100 ,blank = False)
	title_name = models.CharField(max_length= 30 , blank = False)
	title_id = models.IntegerField(null = True, blank = False)
	title_isbn = models.CharField(max_length = 20, blank = False)
	edition = models.CharField(max_length = 20, blank = False)
	price = models.FloatField(null = True ,blank = False)
	version = models.CharField(max_length=30, blank = False)

	def __str__(self):
		return self.user.username
	class Meta:
		db_table = 'Book_Data'


# class Personal_details(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	pan_card_no = models.CharField(max_length = 20, blank =  True)
# 	aadhar_card_no = models.CharField(max_length = 20 , blank = True)
# 	permanent_address = models.CharField(max_length = 100, blank = True)
# 	permanent_city = models.CharField(max_length = 20, blank = True)
# 	permanent_state = models.CharField(max_length = 20, blank = True)
# 	permanent_pin = models.CharField(max_length = 20, blank = True)
# 	permanent_country = models.CharField(max_length = 20, blank = True)
# 	postal_address = models.CharField(max_length = 100, blank = True)
# 	postal_city = models.CharField(max_length = 20, blank = True)
# 	postal_state = models.CharField(max_length = 20, blank = True)
# 	postal_pin = models.CharField(max_length = 20, blank = True)
# 	postal_country = models.CharField(max_length = 20, blank = True)
# 	mobile1 = models.CharField(max_length = 20, blank = True)
# 	mobile2 = models.CharField(max_length = 20, blank = True)
# 	personal_email = models.CharField(max_length = 20, blank = True)
# 	office_email = models.CharField(max_length = 20, blank = True)

# 	def __str__(self):
# 		return self.user
# 	def get_detail(self):
# 		return reverse('post_edit', kwargs={'pk': self.pk})

# 	class Meta: 
# 		db_table = "personal_details"
	 
# 	def __str__(self):
# 		return self.user.username



# def create_profile(sender , **kwargs):
# 	if kwargs['created']:
# 		user_profile = BookData.objects.create(user = kwargs['instance'])

# post_save.connect(create_profile, sender = User) #user = default django user