from django.shortcuts import render
from django.http import HttpResponseBadRequest
import joblib

model = joblib.load("static/ModelGBC.joblib")
# Create your views here.
def home(request):
    return render(request,"home.html")

def tipstrick(request):
    return render(request,"tipstrick.html")

def app(request):
    if request.method == "POST":
        try:
            Age = int(request.POST.get("age"))
            Gender = int(request.POST.get("gender"))
            Hormonal = int(request.POST.get("Hormonal"))
            family = int(request.POST.get("History"))
            race = int(request.POST.get("Ethnicity"))
            body = int(request.POST.get("Weight"))
            calcium = int(request.POST.get("Calcium"))
            vitamin = int(request.POST.get("Vitamin"))
            physical = int(request.POST.get("Activity"))
            smoking = int(request.POST.get("Smoking"))
            alcohol = int(request.POST.get("Alcohol"))
            medical = int(request.POST.get("Medical"))
            amedication = int(request.POST.get("Medication"))
            priot = int(request.POST.get("Priot"))
            
            pred = model.predict([[Age, Gender, Hormonal, family, race, body, calcium, vitamin, physical, smoking,alcohol,medical,amedication,priot]])
            print(f'Hasil Prediksi {pred[0]}')
            if pred ==1:
                pred = "Risk Osteoporosis"
            else:
                pred = "No Risk"


            output = {"output": pred}
            return render(request, 'app.html', output)
        
        except Exception as e:
            error_message = f"Error occurred during prediction: {e}"
            return HttpResponseBadRequest(error_message)
    else:
        return render(request, 'app.html')