from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    TreeBlocks,
    AboutUs,
    MiniBlocksMain,
    MiniBlocks,
    OurStatsMain,
    OurStats,
    OurWorkMain,
    WorksMain,
    WebDesignBlock1,
    WebDesignBlock2,
    GraphicDesignBlock1,
    GraphicDesignBlock2,
    CampaignsBlock1,
    CampaignsBlock2,
    Testimonials,
    TestimonialsBlocks
)


def index(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "tree_blocks": TreeBlocks.objects.all().first(),
        "about_us": AboutUs.objects.all().first(),
        "mini_blocks_main": MiniBlocksMain.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all().first(),
        "our_stats_main": OurStatsMain.objects.all().first(),
        "our_stats": OurStats.objects.all().first(),
        "our_work_main": OurWorkMain.objects.all().first(),
        "works_main": WorksMain.objects.all(),
        "web_design1": WebDesignBlock1.objects.all(),
        "web_design2": WebDesignBlock2.objects.all(),
        "graphic_design1": GraphicDesignBlock1.objects.all(),
        "graphic_design2": GraphicDesignBlock2.objects.all(),
        "campaigns1": CampaignsBlock1.objects.all(),
        "campaigns2": CampaignsBlock2.objects.all(),
        "testimonials": Testimonials.objects.all().first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all()
    } 
    return render(request,"home.html", context)


def premium(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    } 
   
    return render(request, "premium.html", context)


def about(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    
    return render(request, "about.html", context)


def contact(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    return render(request, "contact.html", context)



def gallery(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    return render(request, "gallery.html", context)



def premium(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    return render(request, "premium.html", context)


def products(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first()
    }
    return render(request, "products.html", context)
