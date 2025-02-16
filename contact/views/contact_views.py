"""Contact View"""

from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.

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
