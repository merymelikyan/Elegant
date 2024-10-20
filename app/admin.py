from django.contrib import admin


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


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(TreeBlocks)
admin.site.register(AboutUs)
admin.site.register(MiniBlocksMain)
admin.site.register(MiniBlocks)
admin.site.register(OurStatsMain)
admin.site.register(OurStats)
admin.site.register(OurWorkMain)
admin.site.register(WorksMain)
admin.site.register(WebDesignBlock1)
admin.site.register(WebDesignBlock2)
admin.site.register(GraphicDesignBlock1)
admin.site.register(GraphicDesignBlock2)
admin.site.register(CampaignsBlock1)
admin.site.register(CampaignsBlock2)
admin.site.register(Testimonials)
admin.site.register(TestimonialsBlocks)


