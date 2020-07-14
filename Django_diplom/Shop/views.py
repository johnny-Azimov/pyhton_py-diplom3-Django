from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from Shop.models import Section, Product, Review, Phone, Cultural, Miscellaneous, Section, Cart, ProductsInCart
from django.contrib.auth.models import User
from .forms import ReviewForm
from .functions import pagination


def main(request):
    template_name = 'index.html'
    section_name = Section.objects.filter(location='section 1')[0]
    phones = Product.objects.filter(section__name=section_name).order_by("-id")[0:3]
    other_products = Product.objects.exclude(section__name=section_name).order_by("-id")[0:10]

    context = {
        'phones': phones,
        'other_products': other_products,
    }

    return render(request, template_name, context)


def gadgets(request, slug):
    template_name = f'Shop/sections.html'
    menu_section = Section.objects.get(slug=slug)
    context = pagination(request, Product.objects.filter(section__name=str(menu_section)).order_by("id"), 3)
    context.update({'title': menu_section})
    return render(request, template_name, context)


def product(request, slug):
    template = 'Shop/product_detail.html'
    name_url = request.resolver_match.url_name
    print('name_url:', name_url)
    if request.method == 'POST':
        product_get = get_object_or_404(Product, slug=slug)
        if 'merchandise_id' in request.POST:
            if not ('cart' in request.session):
                request.session['cart'] = []
            product_to_cart = {'id': product_get.id,
                               'quantity': int(request.POST['merchandise_id']),
                               'price': product_get.price,
                               'name': product_get.name,
                               'description': request.POST['description']
                               }
            cart_current = request.session['cart']
            cart_current.append(product_to_cart)
            request.session['cart'] = cart_current
            if 'template' in request.POST:
                return redirect(reverse(name_url, args=[slug]))
            return redirect(reverse('index', args=[product_get.section.slug]))
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                product=product_get,
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating']
            )
            review.save()
        return redirect(reverse(name_url, args=[slug]))
    else:
        form = ReviewForm
        product_get = Product.objects.get(slug=slug)
        product_reviews = Review.objects.all().filter(product_id=product_get.id)
        section_name = Section.objects.get(name=product_get.section)

        try:
            if section_name.template_name == 'phone':
                product_detailed = Phone.objects.get(product_id=product_get.id)
            elif section_name.template_name == 'culture':
                product_detailed = Cultural.objects.get(product_id=product_get.id)
            elif section_name.template_name == 'miscellaneous':
                product_detailed = Miscellaneous.objects.get(product_id=product_get.id)
            else:
                product_detailed = ''
        except Exception:
            product_detailed = ''

        context = {
            'form': form,
            'product': product_get,
            'section_name': str(section_name),
            'product_template': f'Shop/{section_name.template_name}_detail.html',
            'reviews': product_reviews,
            'name_url': name_url,
            'detailed': product_detailed
        }
        return render(request, template, context)