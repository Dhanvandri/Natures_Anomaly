from django.shortcuts import render
from django.http import JsonResponse
import joblib

# Load the Isolation Forest model
model_path = 'D:/Hackathons/CyentifiqHackathon/anomaly_detection/anomaly/isolation_forest_model.joblib'
model = joblib.load(model_path)

def detect_anomaly(request):
    if request.method == 'POST':
        feature1 = float(request.POST.get('feature1', 0))
        feature2 = float(request.POST.get('feature2', 0))

        input_data = [feature1, feature2]
        result = model.predict([input_data])[0]

        if result == -1:
            response_data = {'anomaly': True}
        else:
            response_data = {'anomaly': False}

        return JsonResponse(response_data)

    return render(request, 'anomaly/cyent.html')
