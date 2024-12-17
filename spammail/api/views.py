from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import pandas as pd
import re
from rest_framework import status

# Create your views here.

with open('C:\\artin\\spammail\\api\\vectorizer.pkl','rb')as f :
    vectorizer = pickle.load(f)

with open('C:\\artin\\spammail\\api\\model.pkl','rb') as f:
    model=pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
    
@api_view(['POST'])
def predict(request):
    # if request.method == "POST":
        input_text = request.data.get('text')
        # if not input_text:
        #     return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)
        cleaned_text = clean_text(input_text)
        input_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(input_vector)
        label = "Spam" if prediction[0] == 1 else "Ham"
        return Response({"prediction": label}, status=status.HTTP_200_OK)
    # return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    