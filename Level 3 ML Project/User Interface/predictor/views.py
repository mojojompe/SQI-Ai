import os
import joblib
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from .forms import HousePriceForm, LoanApproverForm

# Helper functions to load models lazily
_house_model = None
_city_encoder = None
_loan_model = None
_loan_features = None

def get_house_model():
    global _house_model, _city_encoder
    models_dir = os.path.join(settings.BASE_DIR, 'predictor', 'ml_models')
    if _house_model is None:
        try:
            _house_model = joblib.load(os.path.join(models_dir, 'house_price_model.pkl'))
            _city_encoder = joblib.load(os.path.join(models_dir, 'city_label_encoder.pkl'))
        except Exception as e:
            print(f"Error loading house model: {e}")
    return _house_model, _city_encoder

def get_loan_model():
    global _loan_model, _loan_features
    models_dir = os.path.join(settings.BASE_DIR, 'predictor', 'ml_models')
    if _loan_model is None:
        try:
            _loan_model = joblib.load(os.path.join(models_dir, 'loan_approver_model.pkl'))
            _loan_features = joblib.load(os.path.join(models_dir, 'loan_features.pkl'))
        except Exception as e:
            print(f"Error loading loan model: {e}")
    return _loan_model, _loan_features


def home(request):
    return render(request, 'home.html')

def house_price(request):
    prediction = None
    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            beds = form.cleaned_data['beds']
            baths = form.cleaned_data['baths']
            toilets = form.cleaned_data['toilets']
            city = form.cleaned_data['city']
            
            model, encoder = get_house_model()
            if model and encoder:
                try:
                    # Encode city
                    city_encoded = encoder.transform([city])[0]
                    
                    # Create dataframe matching the training features
                    input_data = pd.DataFrame({
                        'beds': [beds],
                        'baths': [baths],
                        'toilets': [toilets],
                        'city_encoded': [city_encoded]
                    })
                    
                    pred = model.predict(input_data)[0]
                    prediction = f"₦{pred:,.0f}"
                except Exception as e:
                    prediction = f"Error making prediction: {e}"
            else:
                prediction = "Model not found. Please ensure house_price_model.pkl exists."
    else:
        form = HousePriceForm()
        # Form choices try to populate from joblib on load
        # If city classes change dynamic update requires method call
        # form.update_city_choices()
        
    return render(request, 'house_price.html', {'form': form, 'prediction': prediction})

def loan_approver(request):
    prediction = None
    probability = None
    if request.method == 'POST':
        form = LoanApproverForm(request.POST)
        if form.is_valid():
            model, features = get_loan_model()
            if model and features:
                try:
                    # Create input dict
                    input_dict = {
                        'income': [form.cleaned_data['income']],
                        'credit_score': [form.cleaned_data['credit_score']],
                        'loan_amount': [form.cleaned_data['loan_amount']],
                        'years_employed': [form.cleaned_data['years_employed']],
                        'points': [form.cleaned_data['points']]
                    }
                    
                    input_data = pd.DataFrame(input_dict)
                    
                    # Ensure column order matches training data
                    if set(input_data.columns) == set(features):
                        input_data = input_data[features]
                        
                    pred = model.predict(input_data)[0]
                    prob = model.predict_proba(input_data)[0]
                    
                    if pred == 1:
                        prediction = "APPROVED"
                        probability = f"{prob[1]*100:.1f}%"
                    else:
                        prediction = "DENIED"
                        probability = f"{prob[0]*100:.1f}%"
                        
                except Exception as e:
                    prediction = f"Error: {e}"
            else:
                prediction = "Model missing! Please compile notebooks first."
    else:
        form = LoanApproverForm()
        
    return render(request, 'loan_approver.html', {
        'form': form, 
        'prediction': prediction,
        'probability': probability
    })
