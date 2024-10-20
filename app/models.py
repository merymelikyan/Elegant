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








