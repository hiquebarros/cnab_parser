from django.shortcuts import render
from .forms import UploadFileForm
from .utils.handle_uploaded_file import handle_list
from .utils.handle_store_get import getTransactions, getBalance
from django.core.files.storage import FileSystemStorage


def upload_file(request):
    context = {}
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            uploaded_file = request.FILES['arquivo']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            with open(f"media/{uploaded_file.name}", "r", encoding="utf8") as destination:
                lines = destination.readlines()
                handle_list(lines)
                successfull = handle_list(lines)
                if successfull:
                    context['url'] = fs.url(name)
                else:
                    context['error'] = "Upload falhou"
    else:
        form = UploadFileForm()
        context['form'] = form
    return render(request, "upload.html", context)

def get_operations(request, store_name):
    transactions = getTransactions(store_name)
    balance = getBalance(store_name)
    return render(request, "store.html", {"balance": balance, "transactions": transactions, "name": store_name})
    
