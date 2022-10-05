from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .utils.handle_uploaded_file import handle_uploaded_file, handle_list


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            with open("data.txt", "r", encoding="utf8") as destination:
                lines = destination.readlines()
                iSsuccessful = handle_list(lines)
                if iSsuccessful == False:
                    return HttpResponseRedirect("/failed/url/")
                return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
