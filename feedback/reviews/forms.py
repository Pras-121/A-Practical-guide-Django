from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name",max_length=30, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!" 
#     })
    
#     review_text = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=300)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
     model = Review
     fields = "__all__" # else list fields as ['user_name'] or exclude = ['field name'] 
     labels  = {
         
         "user_name": "Your Name",
         "review_text": "Your Feedback",
         "rating": "Your Rating"
     }
     
     error_messages = {
         "user_name":{
          "required": "Your name must not be empty",
         "max_length": "Please enter a shorter name!"    
            
         }
     }