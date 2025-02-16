"""Contact View"""

from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from contact.models import Contact


def index(request):
    """Main page"""

    contacts = Contact.objects.filter(show=True).order_by('-id') # pylint: disable=no-member

    context = {
        'contacts': contacts,
        'title': 'Contatos',
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context,
    )

def search(request):
    """Main page"""

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter( # pylint: disable=no-member
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
        ).order_by('-id')

    context = {
        'contacts': contacts,
        'title': 'Search',
        'search_value': search_value,
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context,
    )

def contact(request, contact_id):
    """Contact page"""

    # single_contact = Contact.objects.filter(pk=contact_id).first() # pylint: disable=no-member
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    # if single_contact is None:
        # raise Http404()

    title = f'{single_contact.first_name}'

    context = {
        'contact': single_contact,
        'title': title,
    }

    return render(
        request=request,
        template_name='contact/contact.html',
        context=context,
    )
