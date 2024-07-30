from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
month_seasons = {
              "january":"winter",
              "february":"winter",
              "march":"spring",
              "april":"spring",
              "may":"summer",
              "june":"summer",
              "july":"summer",
              "august":"summer",
              "september":"Autumn",
              "october":"Autumn",
              "november":"winter",
              "december":"winter",
              }

def index(request):
    try:
        # list_items =""
        months = list(month_seasons.keys())
        return render(request,"challenges/index.html",{
            "months": months
        })
        # for month in months:
        #     month_capitalized = month.capitalize()
        #     month_path = reverse("monthly_seasons",args=[month])
        #     list_items += f"<li><a href=\"{month_path}\">{month_capitalized}</a></li>"   
        # response_data = f"""<ul>{list_items}</ul>"""
        # return HttpResponse(response_data)
    except:
        return HttpResponseBadRequest("Error fetching the page")
    
    
def monthly_season_int(request,month):
    # derive month from numeral entrered
    season_list = list(month_seasons.keys())
    if month > len(season_list):
        return HttpResponseNotFound("Invalid month.")
    season_of_month = (season_list[month - 1])
    redirect_path = reverse("monthly_seasons",args=[season_of_month])
    # return HttpResponseRedirect("/seasons/"+season_of_month) --> URL is hardcoded, Hence reverse is used to it more dynamic
    return HttpResponseRedirect(redirect_path)
 
 
def monthly_season(request,month):
    try:
        response_data = f"The month falls in {month_seasons[month.lower()]}."
        
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(f"<h1>{response_data}</h1>") --> method 1
        
        #method-2 below, is preferrred
        
        return render(request,"challenges/challenge.html", {
            "month" : month,
            "text":response_data
        })
        
    except:
        return HttpResponseBadRequest("Please enter a valid month.")
