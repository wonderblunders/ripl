from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.
class countries(models.Model):
	name = models.CharField(max_length=60)
	code = models.CharField(max_length=6)
class states(models.Model):
	name = models.CharField(max_length=60)
	country = models.ForeignKey('countries', on_delete=models.DO_NOTHING)
class cities(models.Model):
	name = models.CharField(max_length=60)
	state = models.ForeignKey('states', on_delete=models.DO_NOTHING)
class product(models.Model):
	title = models.CharField(max_length=45)
	desc = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='prothumb', verbose_name="Thumbnail")
	cover = models.ImageField(upload_to='cover', verbose_name="cover image")
	function = models.ManyToManyField('function')
	dimension = models.ManyToManyField('dimension')
	features = models.ManyToManyField('feature')
	accessory = models.ManyToManyField('accessory')
	material = models.ManyToManyField('material')
	faq = models.ManyToManyField('faq')
	added_on = models.CharField(max_length=200,default=datetime.now)
	category = models.ManyToManyField('category')
	'''COUNTRIES_CHOICES=(('India', 'IN'),)
	name = models.CharField(max_length=60, default="India", choices=COUNTRIES_CHOICES)
	code = models.CharField(max_length=6)'''
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.title)
class function(models.Model):
	title = models.CharField(max_length=45)
	image = models.ImageField(upload_to='prothumb/fun_images', verbose_name="img")
	def __unicode__(self):
		return str(self.title)
class dimension(models.Model):
	title = models.CharField(max_length=45)
	desc = models.CharField(max_length=45)
	image = models.ImageField(upload_to='prothumb/dim_images', verbose_name="img")
	def __unicode__(self):
		return str(self.title)
class feature(models.Model):
	title = models.CharField(max_length=45)
	image = models.ImageField(upload_to='prothumb/feat_images', verbose_name="img")
	def __unicode__(self):
		return str(self.title)
class accessory(models.Model):
	title = models.CharField(max_length=45)
	image = models.ImageField(upload_to='prothumb/acc_images', verbose_name="img")
	def __unicode__(self):
		return str(self.title)
class faq(models.Model):
	question = models.CharField(max_length=100)
	answer = models.CharField(max_length=100)
	def __unicode__(self):
		 return str(self.question)
class category(models.Model):
	title = models.CharField(max_length=45)
	desc = models.CharField(max_length=200)
	image = models.ImageField(upload_to='thu', verbose_name="img")
	fimage = models.ImageField(upload_to='prothumb', verbose_name="Featured Image")
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.title)
def delete(self, *args, **kwargs):
	try:
		self.MyImageFieldName.delete(save=True)
	except: pass

class category_index_thumbs(models.Model):
	category = models.ForeignKey('category', on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(upload_to='category/index/thumbs', verbose_name="img")	
	def __unicode__(self):
		return str(self.category)	
class color(models.Model):
	title = models.CharField(max_length=45)
	code = models.CharField(max_length=45)
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.title)

class upholstery(models.Model):
	title = models.CharField(max_length=45)
	code = models.CharField(max_length=5)
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.title)

class sub_upholstery(models.Model):
	title = models.CharField(max_length=45)
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str(self.title)

class material(models.Model):
	upholstery = models.ForeignKey('upholstery', on_delete=models.CASCADE)
	color = models.ForeignKey('color', on_delete=models.CASCADE)
	family = models.ForeignKey('sub_upholstery', on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(upload_to='upholstery', verbose_name="img")
	flag = models.BooleanField(default=True)
	def __unicode__(self):
		return str("{1} {0} {2}".format(self.color,self.family,self.upholstery))

class spares(models.Model):
	spare_title = models.CharField(max_length=45)
	s_image = models.ImageField(upload_to='spare', verbose_name="img")
	spare_desc = models.CharField(max_length=1000)
	vendor_title = models.CharField(max_length=45)
	v_image = models.ImageField(upload_to='spare/vendor', verbose_name="img")
	vendor_desc = models.CharField(max_length=1000)
	def __unicode__(self):
		return str("{1} {0}".format(self.spare_title,self.vendor_title))

class pro_uph_options(models.Model):
	product = models.ForeignKey('product', on_delete=models.DO_NOTHING)
	material = models.ForeignKey('material', on_delete=models.DO_NOTHING)

class contact(models.Model):
	fname =  models.CharField(max_length=45)
	lname =  models.CharField(max_length=45)
	occupation =  models.CharField(max_length=45)
	reason = models.CharField(max_length=45)
	phone =  models.CharField(max_length=15)
	email =  models.EmailField(max_length=200)
	message = models.CharField(max_length=450)
	country = models.CharField(max_length=100)

class servicing(models.Model):
	fname =  models.CharField(max_length=45)
	lname =  models.CharField(max_length=45)
	serial =  models.CharField(max_length=45)
	phone =  models.CharField(max_length=15)
	email =  models.EmailField(max_length=200)
	country =  models.CharField(max_length=45)
	message = models.CharField(max_length=450)

class callme(models.Model):
	number = models.CharField(max_length=15)
	remarks = models.CharField(max_length=450, blank=True, null=True)
	user = models.CharField(max_length=45, blank=True, null=True)
	flag = models.BooleanField(default=False)
	def update(self, *args, **kwargs):
		self.user = "aoo"
		super(model.callme, self).update(self.user, *args, **kwargs)
		pass
class subscribe(models.Model):
	email = models.EmailField(max_length=200)
	def __unicode__(self):
		return self.email
class faqcategory(models.Model):
	category = models.CharField(max_length=45)
	def __unicode__(self):
		return self.category

class gfaq(models.Model):
	category = models.ForeignKey('faqcategory', on_delete=models.DO_NOTHING)
	query = models.CharField(max_length=45)
	answer = models.CharField(max_length=450)
	def __unicode__(self):
		return str("{0} {1}".format(self.query, self.answer))
class mblog(models.Model):
	title = models.CharField(max_length=100)
	post = models.CharField(max_length=2000)
	image = models.ImageField(upload_to='mblog')
	timestamp = models.DateTimeField(default=datetime.now())
	author = models.CharField(max_length=45)
	flag = models.BooleanField(default=True)
	
'''class category(models.Model):
	name = models.CharField(max_length=20)

class color(models.Model):
	name = models.CharField(max_length=20)

class material(models.Model):
	name = models.CharField(max_length=20)

class accessory(models.Model):
	name = models.CharField(max_length=20)


	image = models.TextField(
			db_column='thumb',
			blank=True)

	def set_data(self, data):
		self.image = base64.encodestring(thumb)

	def get_data(self):
		return base64.decodestring(self.image)

	data = property(get_data, set_data)'''