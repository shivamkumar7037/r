from django.shortcuts import render
from testapp.models import Ads,Contact,Categories,Member
from testapp.forms import ContactForm

# Create your views here.
def cat_list(request,category):
    ads = Ads.objects.filter(category=category)
   # ads = Ads.objects.get()
    return render(request,'testapp/category_list.htm',{'ads':ads,'cats':category})
    

def index(request):
    ads = Ads.objects.all()
    cats = Categories.objects.all()
    return render(request,'testapp/index.htm',{'ads':ads,'cats':cats})

def contact(request):
    form = ContactForm()
    msg =""
    try:
        if request.method=='POST':
            con = ContactForm(request.POST)
            if con.is_valid():
                con.save(commit=True)
                msg = "Contact has successfully saved."
            else:
                msg = "Sorry Contact does not saved."
    except Exception as e:
        msg = e        

    return render(request,'testapp/contact.htm',{'form':form,'msg':msg})

def about(request):
    members = Member.objects.all()
    return render(request,'testapp/about.htm',{'members':members})

def detail(request,id):
    ads = Ads.objects.get(id=id)
    return render(request,'testapp/details.htm',{'ads':ads})

