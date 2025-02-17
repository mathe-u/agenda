"""Contact Form"""

from django.shortcuts import render
from contact.forms import ContactForm





def create(request):
    """Create forms"""

    title = 'Form'

    if request.method == 'POST':
        context = {
            'title': title,
            'form': ContactForm(data=request.POST)
        }

        return render(
            request=request,
            template_name='contact/create.html',
            context=context,
        )

    context = {
        'title': title,
        'form': ContactForm()
    }

    return render(
        request=request,
        template_name='contact/create.html',
        context=context,
    )
