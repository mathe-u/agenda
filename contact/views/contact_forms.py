"""Contact Form"""

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contact.forms import ContactForm
from contact.models import Contact


@login_required(login_url='contact:login')
def create(request):
    """Create forms"""

    form_action = reverse('contact:create')
    title = 'Form'

    if request.method == 'POST':
        form = ContactForm(data=request.POST, files=request.FILES)
        context = {
            'title': title,
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request=request,
            template_name='contact/create.html',
            context=context,
        )

    context = {
        'title': title,
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request=request,
        template_name='contact/create.html',
        context=context,
    )


@login_required(login_url='contact:login')
def update(request, contact_id):
    """Create forms"""

    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
        owner=request.user,
    )
    form_action = reverse('contact:update', args=(contact_id,))
    title = 'Form'

    if request.method == 'POST':
        form = ContactForm(data=request.POST, files=request.FILES, instance=contact)
        context = {
            'title': title,
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request=request,
            template_name='contact/create.html',
            context=context,
        )

    context = {
        'title': title,
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request=request,
        template_name='contact/create.html',
        context=context,
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    """Delete"""
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
        owner=request.user,
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request=request,
        template_name='contact/contact.html',
        context={
            'contact': contact,
            'confirmation': confirmation,
        },
    )
