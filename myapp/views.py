from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def profit_view(request):
    scheme_code = request.GET.get('scheme_code', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    capital = request.GET.get('capital', '1000000.0')
    api_url = f'https://api.mfapi.in/mf/'+scheme_code
    response = requests.get(api_url)
    start_date_nav = float()
    end_date_nav = float()
    if response.status_code == 200:
        data = response.json()
        data1 = data['data']
        try:
            for i in data1:
                if i['date'] == start_date:
                    start_date_nav = str(i['nav'])
                if i['date'] == end_date:
                    end_date_nav = str(i['nav'])
            number_of_units_alloted_on_startdate = float(capital) / float(start_date_nav)
            value_as_on_end_date = number_of_units_alloted_on_startdate * float(end_date_nav)
            Net_Profit = value_as_on_end_date - float(capital)
            data = {'Net_Profit':Net_Profit}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'Response':'No Data Found.... Please try again.'})
    else:
        return Response({'Response':'No Data Found.... Please try again.'})