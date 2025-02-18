"""Contact Form"""

from django.shortcuts import render, redirect
from contact.forms import ContactForm





def create(request):
    """Create forms"""

    title = 'Form'

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
            'title': title,
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

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
