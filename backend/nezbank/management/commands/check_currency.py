from django.core.management.base import BaseCommand
import requests
import xmltodict
from nezbank.models import AccountType


class Command(BaseCommand):

    def handle(self, *args, **options):
        full_page = requests.get("https://www.cbr-xml-daily.ru/daily.xml")
        data = xmltodict.parse(full_page.content)
        usd = str(data['ValCurs']['Valute'][10]['Value']).replace(',', '.')
        euro = str(data['ValCurs']['Valute'][11]['Value']).replace(',', '.')
        AccountType.objects.filter(id=2).update(value=usd)
        AccountType.objects.filter(id=3).update(value=euro)
