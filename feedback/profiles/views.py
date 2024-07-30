from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import ListView


# Create your views here.
def store_file(file):
    with open("temp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk) 

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
             "form": form
        })

    def post(self, request):
        sub_form = ProfileForm(request.POST, request.FILES)
        # store_file(request.FILES["image"])

        
        if sub_form.is_valid():
            profile = UserProfile(image=request.FILES["image"])
            profile.save()
            # store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html",{
             "form": sub_form
        })
    
class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html" 
    context_object_name="profiles" 
        