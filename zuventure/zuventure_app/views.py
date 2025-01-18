from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import ContactForm
from django.http import JsonResponse

# Create your views here.

  
def home(request):
  sliders = SliderView.objects.all()
  gallery_photos = Gallery.objects.all()
  popular_products = Product.objects.filter(is_popular=True)
  categories = ProductCategory.objects.all()
  about = AboutUs.objects.first()
  sisters = SisterConcern.objects.all()
  
  if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your message has been sent successfully! Thank you for contacting us. We will get in touch with you shortly."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
      
  form = ContactForm()
      
  return render (request, "index.html",{
    "sliders" : sliders,
    "gallery_photos" : gallery_photos,
    "populer_products" : popular_products,
    "categories" : categories,
    "about" : about , 
    "sisters" : sisters,
    "form": form,
  })

def get_categories(request, category_name):
    sisters = SisterConcern.objects.all()
    try:
        sister_concern = SisterConcern.objects.get(name=category_name)
        filtered_products = Product.objects.filter(product_of=sister_concern)      
    except SisterConcern.DoesNotExist:
        filtered_products = [] 
    return render(request, "products.html", {
        "sister_concern": sister_concern,
        "filtered_products": filtered_products,
        "sisters" : sisters,

    })

def get_products(request, category_name, id):
  
    try:
        sister_concern = SisterConcern.objects.get(name=category_name)
        product_details = Product.objects.get(id=id, product_of=sister_concern)
        
    except (SisterConcern.DoesNotExist, Product.DoesNotExist):
        product_details = []
    
    return render(request, "product-details.html", {
        "product_details": product_details,
    })

def about(request):
  about = AboutUs.objects.first()
  sisters = SisterConcern.objects.all()
  chairman = Chairman.objects.first()
  md = ManagingDirector.objects.first()
  team_members = TeamMember.objects.all()
  return render (request, "about.html",{
    "about" : about , 
    "sisters" : sisters,
    "chairman" : chairman,
    "md" : md,
    "team_members" : team_members
  })

def gallery(request):
    galleries = Gallery.objects.all()
    
    return render(request, "gallery.html", {
        "galleries" : galleries
    })

def contact(request):
    about = AboutUs.objects.first()
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your message has been sent successfully! Thank you for contacting us. We will get in touch with you shortly."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
      
    form = ContactForm()
    
    return render(request, "contact.html", {
        "about" : about , 
        "form": form,
    })

def drop_cv(request):

    cv_categories = CvCatagory.objects.all()

    if request.method == 'POST':     
        cv_category_id = request.POST.get('cv_category', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        photo = request.FILES.get('photo')
        cv = request.FILES.get('cv')

        if not (cv_category_id and name and email and phone_number and photo and cv):
            return JsonResponse({'success': False, 'message': 'All fields are required.'})

        cv_catagory = get_object_or_404(CvCatagory, id=cv_category_id)

        DropCV.objects.create(
            cv_catagory=cv_catagory,
            name=name,
            email=email,
            phone_number=phone_number,
            photo=photo,
            cv=cv,
        )

        return JsonResponse({'success': True})
    context = {
        'cv_categories': cv_categories,	
    }

    return render(request, 'career.html', context)