# context_processors.py
from .models import CompanyInfo, SisterConcern, ProductCategory

def company_info(request):
    info = CompanyInfo.objects.first()
    sisters = SisterConcern.objects.all()
    return {
        'info': info,
        'sisters': sisters,
    }
