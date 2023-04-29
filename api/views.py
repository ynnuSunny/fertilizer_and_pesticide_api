# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np


 

from django.shortcuts import render

import pickle
import requests

class FertilizerView(APIView):
    def post(self, request):
        user_input = request.data.get('npk_value', None)
        url = "https://github.com/ynnuSunny/fertilizer_and_pesticide_api/blob/main/models/classifier1.pkl?raw=true"
        response = requests.get(url)
        model = pickle.loads(response.content)
        if user_input is not None:
            list_numbers = user_input.split(',')
            npk_value = list(map(int, list_numbers)) 

            #print(npk_value[1])
            
            result = model.predict(np.array([npk_value]))
            # print(result)
            if result[0] == 0:
                result = 'TEN-TWENTY SIX-TWENTY SIX'
            elif result[0] == 1:
                result = 'Fourteen-Thirty Five-Fourteen'
            elif result[0] == 2:
                result = 'Seventeen-Seventeen-Seventeen'
            elif result[0] == 3:
                result = 'TWENTY-TWENTY'
            elif result[0] == 4:
                result = 'TWENTY EIGHT-TWENTY EIGHT'
            elif result[0] == 5:
                result = 'DAP'
            else:
                result = 'UREA'

            return Response({'result': result, 'status':"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'npk_value not provided','status':"error"}, status=status.HTTP_400_BAD_REQUEST)

class CropView(APIView):
    def post(self, request):
        user_input = request.data.get('values', None)
        model = pickle.load(open('models/crop_random.pkl','rb'))
        if user_input is not None:
            list_numbers = user_input.split(',')
            npk_value = list(map(float, list_numbers)) 

            #print(npk_value[1])
            result = model.predict(np.array([npk_value]))
            print(result)
            
            output =['apple',
                'banana',
                'blackgram',
                'chickpea',
                'coconut',
                'coffee',
                'cotton',
                'grapes',
                'jute',
                'kidneybeans',
                'lentil',
                'maize',
                'mango',
                'mothbeans',
                'mungbean',
                'muskmelon',
                'orange',
                'papaya',
                'pigeonpeas',
                'pomegranate',
                'rice',
                'watermelon']

            return Response({'result': output[result[0]], 'status':"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'npk_value not provided','status':"error"}, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request,"index.html")

