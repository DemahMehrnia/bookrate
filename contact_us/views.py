from django.shortcuts import render
from .forms import contact_us_form
from .models import ContactUs

# Create your views here.


# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        contact_form = contact_us_form(request.POST)
        if contact_form.is_valid():
            content = ContactUs(
                title=contact_form.cleaned_data.get('subject'),
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                message=contact_form.cleaned_data.get('text'),
                is_read_by_admin=False

            )
            content.save()
            return render(request, 'contact_us/Succes.html')

    else:
        contact_form = contact_us_form()
    return render(request, 'contact_us/contact_page.html', {'contact_form': contact_form})

