from django.db import models

class HeaderText(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="header_text")
 
    def __str__(self):
        return f"{self.title1} {self.title2}"

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"

 
class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"



class TreeBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    url_name = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tree Blocks"
        verbose_name_plural = "Tree Blocks"


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)

 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"



class MiniBlocksMain(models.Model):
    image = models.ImageField(upload_to="mini_blocks_main.image.url", blank=True, null=True)

 
    def __str__(self):
        return f"{self.image}"
    
    class Meta:
        verbose_name = "Mini Blocks Main"
        verbose_name_plural = "Mini Blocks Main"


class MiniBlocks(models.Model):
    icon_class = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)

 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Mini Blocks"
        verbose_name_plural = "Mini Blocks"



class OurStatsMain(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Our Stats Main"
        verbose_name_plural = "Our Stats Main"


class OurStats(models.Model):
    count = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
 
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Our Stats"
        verbose_name_plural = "Our Stats"



class OurWorkMain(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Our Work Main"
        verbose_name_plural = "Our Work Main"



class WorksMain(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Works Main"
        verbose_name_plural = "Works Main"


class WebDesignBlock1(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_image = models.ImageField(upload_to="web_design1.image.url", blank=True, null=True)
    image = models.ImageField(upload_to="web_design1.image.url", blank=True, null=True)
   
 
    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = "Web Design block1"
        verbose_name_plural = "Web Design block1"


class WebDesignBlock2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_video = models.FileField(upload_to='media/videos/', blank=True, null=True)
    image = models.ImageField(upload_to="web_design2.image.url", blank=True, null=True)
   
 
    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = "Web Design block2"
        verbose_name_plural = "Web Design block2"


class GraphicDesignBlock1(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_image = models.ImageField(upload_to="graphic_design1.image.url", blank=True, null=True)
    image = models.ImageField(upload_to="graphic_design1.image.url", blank=True, null=True)
    
 
    def __str__(self):
       return self.image_title
    
    class Meta:
        verbose_name = "Graphic Design block1"
        verbose_name_plural = "Graphic Design block1"

        
class GraphicDesignBlock2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_video = models.FileField(upload_to='media/videos/', blank=True, null=True)
    image = models.ImageField(upload_to="graphic_design2.image.url", blank=True, null=True)
 
    def __str__(self):
       return self.image_title
    
    class Meta:
        verbose_name = "Graphic Design block2"
        verbose_name_plural = "Graphic Design block2"        


class CampaignsBlock1(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_image = models.ImageField(upload_to="campaigns1.image.url", blank=True, null=True)
    image = models.ImageField(upload_to="campaigns1.image.url", blank=True, null=True)
   
    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = "Campaigns block1"
        verbose_name_plural = "Campaigns block1"


class CampaignsBlock2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    url_video = models.FileField(upload_to='media/videos/', blank=True, null=True)
    image = models.ImageField(upload_to="campaigns2.image.url", blank=True, null=True)
   
    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = "Campaigns block2"
        verbose_name_plural = "Campaigns block2"


class Testimonials(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"



class TestimonialsBlocks(models.Model):
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="testimonials_blocks.image.url", blank=True, null=True)
    
 
    def __str__(self):
        return self.description2
    
    class Meta:
        verbose_name = "Testimonials blocks"
        verbose_name_plural = "Testimonials blocks"


class ContactUsMain(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "ContactUsMain"
        verbose_name_plural = "ContactUsMain"


class Address(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"


class Email(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Email"


class Phone(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=255, blank=True, null=True) 
    phone_number2 = models.CharField(max_length=255, blank=True, null=True)
    phone_number3 = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phone"


class Contact(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class ContactAddress(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contact Address"
        verbose_name_plural = "Contact Address"


class ContactEmail(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contact Email"
        verbose_name_plural = "Contact Email"


class ContactPhone(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=255, blank=True, null=True) 
    phone_number2 = models.CharField(max_length=255, blank=True, null=True)
    phone_number3 = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contact Phone"
        verbose_name_plural = "Contact Phone"



class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True) 
    description2 = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"



class GalleryBlocks(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True) 
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="block.image.url", blank=True, null=True)
   
    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = "Gallery Blocks"
        verbose_name_plural = "Gallery Blocks"        




class AboutMain(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=555, blank=True, null=True)
    description2 = models.CharField(max_length=555, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Main"
        verbose_name_plural = "About Main" 


class About(models.Model):
    title1 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    description1 = models.CharField(max_length=2000, blank=True, null=True)
    description2 = models.CharField(max_length=2000, blank=True, null=True)
    image1 = models.ImageField(upload_to="about_image.image.url", blank=True, null=True)
    description3 = models.CharField(max_length=2000, blank=True, null=True)
    image2 = models.ImageField(upload_to="about_image.image.url", blank=True, null=True)
    description4 = models.CharField(max_length=2000, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title1}, {self.title2}"
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"            



class OpeningHours(models.Model):
    title = models.CharField(max_length=60)
    days1 = models.CharField(max_length=60)
    days2 = models.CharField(max_length=60)
    days3 = models.CharField(max_length=60)
    days4 = models.CharField(max_length=60)
    days5 = models.CharField(max_length=60)
    days6 = models.CharField(max_length=60)
    open_time1 = models.CharField(max_length=60)
    open_time2 = models.CharField(max_length=60)
    open_time3 = models.CharField(max_length=60)
    open_time4 = models.CharField(max_length=60)
    open_time5 = models.CharField(max_length=60)
    open_time6 = models.CharField(max_length=60)
    close_day = models.CharField(max_length=60)
    close_time = models.CharField(max_length=60)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Opening Hours"
        verbose_name_plural = "Opening Hours"       



class Products(models.Model):
    title1 = models.CharField(max_length=255)
    description1 = models.CharField(max_length=2000, blank=True, null=True) 
    description2 = models.CharField(max_length=2000, blank=True, null=True)
    title2 = models.CharField(max_length=200)
    description3 = models.CharField(max_length=2000, blank=True, null=True) 
   
    def __str__(self):
      return f"{self.title1}, {self.title2}"
    
    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"



class ProductsBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000) 
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Products Blocks"
        verbose_name_plural = "Products Blocks"        



class PremiumMain(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Premium Main"
        verbose_name_plural = "Premium Main"        


class Premium(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="premium")
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Premium"
        verbose_name_plural = "Premium"                