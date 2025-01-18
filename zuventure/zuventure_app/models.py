from django.db import models
from ckeditor.fields import RichTextField


# About Us Model
class AboutUs(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to="about-images")
  description = models.CharField(max_length=500)
  
  def __str__(self):
        return self.name
  class Meta:
    verbose_name_plural = "About Us"

# Slider Model
class SliderView(models.Model):
  title = models.CharField(max_length= 200)
  sub_title = models.CharField(max_length=100)
  image = models.ImageField(upload_to = "slider-images", null=True)
  
  def __str__(self):
        return self.title
  class Meta:
    verbose_name_plural = "Slider View"

# All Products Model
class Product(models.Model):
  image = models.ImageField(upload_to="product_images")
  name = models.CharField(max_length = 100)
  category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, null=True, related_name="products")
  product_of = models.ForeignKey("SisterConcern", on_delete=models.CASCADE, null=True, related_name="product_of")
  descriptions = RichTextField(max_length=10000)
  is_popular = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name
   
# Product Categories Model
class ProductCategory(models.Model):
  name = models.CharField(max_length= 100)
  
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = "Product Categories"

#Gallery Model
class Gallery(models.Model):
  image = models.ImageField(upload_to="gallery-images")
  short_description = models.CharField(max_length=300, null=True, blank=True)
  
  def __str__(self):
    return self.short_description if self.short_description else "No Description"

  class Meta:
    verbose_name_plural = "Gallery"

# Sister Concerns Model
class SisterConcern(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to="sister-concern-images")
  
  def __str__(self):
        return self.name
  class Meta:
    verbose_name_plural = "Sister Concerns"
    
# Company Informations Model
class CompanyInfo(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to="logo")
  primary_phone = models.CharField(max_length=15)
  secondary_phone = models.CharField(max_length=15, null=True, blank=True)
  location = models.CharField(max_length=100)
  email = models.CharField(max_length=100, null=True)
  facebook_url = models.CharField(max_length=200 , null=True, blank=True)
  instagram_url = models.CharField(max_length=200, null=True, blank=True)
  linkedin_url = models.CharField(max_length=200  , null=True, blank=True)
  youtube_url = models.CharField(max_length=200  , null=True, blank=True)
  
  
  
  def __str__(self):
        return self.name
  class Meta:
    verbose_name_plural = "Company Informations"
  
# Contact Us Models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
  
# Chairman  Models
class Chairman(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="chairman-image")
    description = RichTextField(max_length=10000)
    

    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "Chairman"
  
# MD  Models
class ManagingDirector(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="md-image")
    description = RichTextField(max_length=10000)

    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "Managing Director"
      
#Team Members Models
class TeamMember(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to="Team-images")
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "Team Members"


class CvCatagory(models.Model):
    title = models.CharField(max_length=100, blank=True, null = True)

    class Meta:
        verbose_name_plural = "Cv Category"

    def __str__(self):
        return f"{self.title}"

class DropCV(models.Model):
    cv_catagory = models.ForeignKey(CvCatagory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null = True)
    email = models.CharField(max_length=100, blank=True, null = True)
    photo = models.ImageField(upload_to='cv_photo/', blank=True, null = True)
    cv = models.FileField(upload_to='cv_pdf/', blank=True, null = True)
    phone_number = models.CharField(max_length=100, blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Dropped CV"

    def __str__(self):
        return f"{self.name}"
  
  
