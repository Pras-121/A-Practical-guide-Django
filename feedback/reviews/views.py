from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
# Create your views here.

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
    
#         return render(request,"reviews/review.html",{
#         "form": form
#     })
        
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you") 
#         return render(request,"reviews/review.html",{
#         "form": form
#     })

# Using FormView for above case
# for POST we need success-url

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# FormView + save data. Fields can be configured based on form_class =  form.py
# Or customly here itself' BUT lables and errors cannot be customised

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


 

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank-you.html")
    
class ThankYouView(TemplateView):
        template_name = "reviews/thank-you.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["message"] = "This works!"
            return context

# class  ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
 
# Instead of above we can use ListView Temple, gets all data of "model"(model needs to be pointed to the model) 
# and passes it as context
# In HTML template Object_list needs to be used as context variable or use context-object-name property

class  ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name =  "reviews"
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# use detailview to display data pertaining to a single piece of data
# class DetailView(TemplateView):
#     template_name = "reviews/detail_view.html"
#     def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        review_id = kwargs["id"]
#        review = Review.objects.get(pk=review_id)
#        context["review"] = review
#        return context
     
# uses either slug or pk
# Takes model name in lowercase as context variable. Context variable can also be named with context_object_name property


class SingleView(DetailView):
    template_name = "reviews/detail_view.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.get_object()
        # print(self.get_context_object_name.id)
        request =  self.request
        # fav_id = request.session["favourite_review"]
        fav_id = request.session.get("favourite_review")
        context["is_fav"] = (fav_id == str(loaded_review.pk))
        return context


class AddFavoriteView(CreateView):
    def post(self,request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

  ### below COde only for reference. Ignore
       
def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST['username']
        
    #     if entered_username == "":
    #         return render (request,"reviews/review.html",{
    #           "has_error": True    
    #         })
            
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name = form.cleaned_data['user_name'],
            #                 review_text =form.cleaned_data['review_text'],
            #                 rating = form.cleaned_data['rating'] )
            # review.save()
            # if modelbased form is used above code is not required, the below would do
            
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")     
    else:
        form = ReviewForm()
    
    return render(request,"reviews/review.html",{
        "form": form
    })

# def thank_you(request):
#     return render(request, "reviews/thank-you.html")