from django.contrib import admin
from models import *

# Register your models here.
class a_product(admin.ModelAdmin):
	list_display = ['title']
class a_category(admin.ModelAdmin):
	list_display = ['title', 'desc']
class a_upholstery(admin.ModelAdmin):
	list_display = ['title', 'code', 'flag']
class a_sub_upholstery(admin.ModelAdmin):
	list_display = ['title']
class a_material(admin.ModelAdmin):
	list_display = ['color', 'family', 'upholstery', 'image']
class a_color(admin.ModelAdmin):
	list_display = ['title']
class a_accessory(admin.ModelAdmin):
	list_display = ['title']
class a_category(admin.ModelAdmin):
	list_display = ['title']
class a_contact(admin.ModelAdmin):
	list_display = ['fname','lname','phone']
class a_pro_uph_options(admin.ModelAdmin):
	list_display = ['product', 'material']
class a_function(admin.ModelAdmin):
	list_display = ['title']
class a_feature(admin.ModelAdmin):
	list_display = ['title']
class a_dimension(admin.ModelAdmin):
	list_display = ['title', 'desc']
class a_accessory(admin.ModelAdmin):
	list_display = ['title']
class a_faq(admin.ModelAdmin):
	list_display = ['question', 'answer']
class a_spare(admin.ModelAdmin):
	list_display = ['spare_title', 'vendor_title']
class a_category_index_thumbs(admin.ModelAdmin):
	list_display = ['category']	
class a_callme(admin.ModelAdmin):
	readonly_fields=('number','user',)
	list_display = ['number', 'flag', 'remarks', 'user']
class a_gfaqcat(admin.ModelAdmin):
	list_display = ['category']
class a_gfaq(admin.ModelAdmin):
	list_display = ['category','query','answer']
class a_subscribe(admin.ModelAdmin):
	list_display = ['email']
class a_mblog(admin.ModelAdmin):
	list_display = ['title','post','image','author']

admin.site.register(product, a_product)
admin.site.register(category, a_category)
admin.site.register(upholstery, a_upholstery)
admin.site.register(pro_uph_options, a_pro_uph_options)
admin.site.register(sub_upholstery, a_sub_upholstery)
admin.site.register(material, a_material)
admin.site.register(color, a_color)
admin.site.register(function, a_function)
admin.site.register(dimension, a_dimension)
admin.site.register(accessory, a_accessory)
admin.site.register(feature, a_feature)
admin.site.register(faq, a_faq)
admin.site.register(spares, a_spare)
admin.site.register(category_index_thumbs, a_category_index_thumbs)
admin.site.register(callme, a_callme)
admin.site.register(gfaq, a_gfaq)
admin.site.register(faqcategory, a_gfaqcat)
admin.site.register(subscribe, a_subscribe)
admin.site.register(mblog, a_mblog)
admin.site.register(contact, a_contact)