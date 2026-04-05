from django import forms
import joblib
import os
from django.conf import settings

# Helper function to load cities safely
def get_city_choices():
    try:
        models_dir = os.path.join(settings.BASE_DIR, 'predictor', 'ml_models')
        city_list_path = os.path.join(models_dir, 'city_classes.pkl')
        if os.path.exists(city_list_path):
            cities = joblib.load(city_list_path)
            
            return [(city, city.capitalize()) for city in cities]
    except Exception:
        pass
    # Fallback to basic choices if missing
    return [('ajah', 'Ajah'), ('lekki', 'Lekki'), ('ikeja', 'Ikeja'), ('surulere', 'Surulere')]


class HousePriceForm(forms.Form):
    beds = forms.IntegerField(label='Bedrooms', min_value=0, max_value=20, initial=3)
    baths = forms.IntegerField(label='Bathrooms', min_value=0, max_value=20, initial=3)
    toilets = forms.IntegerField(label='Toilets', min_value=0, max_value=20, initial=4)
    city = forms.ChoiceField(label='City/Location', choices=get_city_choices)
    
    # Enable crispy forms styling classes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
    # Refresh choices dynamically
    def update_city_choices(self):
        self.fields['city'].choices = get_city_choices()


class LoanApproverForm(forms.Form):
    income = forms.IntegerField(label='Annual Income ($)', min_value=0, initial=60000)
    credit_score = forms.IntegerField(label='Credit Score', min_value=300, max_value=850, initial=650)
    loan_amount = forms.IntegerField(label='Loan Amount Requested ($)', min_value=0, initial=25000)
    years_employed = forms.IntegerField(label='Years Employed', min_value=0, initial=5)
    points = forms.IntegerField(label='Loyalty/Reward Points', min_value=0, initial=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
