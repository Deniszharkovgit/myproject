import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from pycbrf.toolbox import ExchangeRates
from .models import TableNumbers
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from notifiers import get_notifier
from datetime import datetime



def send_from_user(text_message):
    token = '5502952184:AAFqjDlmpwl21Lx35PIIyA7Md4EnWAqNypQ'
    chat_id = '387274652'
    telegram = get_notifier('telegram')
    telegram.notify(token=token, chat_id=chat_id, message=text_message)


def create_credentials():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'myproject_app/keys.json',
        scopes=scopes
    )

    return gspread.authorize(credentials)

class NumbersList(APIView):
    def get(self, request):
        now = datetime.now()
        TableNumbers.objects.all().delete()
        rates = ExchangeRates()
        gc = create_credentials()
        gc = gc.open_by_key("1Xc13UDoPCHh1_yQoNwfieFMovmhAcrzsqU_XsQz44SM")
        values = gc.get_worksheet(0).get_all_values()
        for i in range(1, len(values)):
            if datetime.strptime(values[i][3],'%d.%m.%Y') < now:
                send_from_user(f'Срок поставки {values[i][1]} истёк')        
            purchase = TableNumbers(number=values[i][0],
            order=values[i][1], 
            price_dollar=values[i][2],
            delivery_data=datetime.strptime(values[i][3],'%d.%m.%Y'),
            price_rub=str(float(values[i][2]) * float(rates['USD'].value)))
            purchase.save()
        numbers = TableNumbers.objects.all()
        serializer = NumbersSerializer(numbers, many=True)
        return Response(serializer.data)