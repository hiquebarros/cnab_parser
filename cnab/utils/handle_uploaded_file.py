from cnab.models import Transaction
from cnab.serializers import TransactionSerializer

def handle_uploaded_file(f):
    with open('data.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_list(list):
    for line in list:
        type = line[:1]
        date = line[1:9]
        value = int(line[9:19]) / 100.00
        cpf = line[19:30]
        credit_card = line[30:42]
        hour = line[42:48]
        owner = line[48:62]
        name = line[62:80]

        transaction_dict = {
            'type': type,
            'date': date,
            'value': value,
            'cpf': cpf,
            'credit_card': credit_card,
            'hour': hour,
            'owner': owner,
            'name': name
        }

        serializer = TransactionSerializer(data=transaction_dict)
        validator = serializer.is_valid()
        serializer.save()
    return validator
        


        

