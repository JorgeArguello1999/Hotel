from django.contrib import admin

# Models 
from billing.models import BillingModel
from billing.models import PricingModel
from billing.models import IVAModel
from billing.models import DiscountsModel

# Register
admin.site.register(BillingModel)
admin.site.register(PricingModel)
admin.site.register(IVAModel)
admin.site.register(DiscountsModel)