import urllib.parse
from django.core.paginator import Paginator


def pagination(request, model_obj, objects_to_page):
    page_number = request.GET.get('page')
    paginator = Paginator(model_obj, objects_to_page)
    page_object = paginator.get_page(page_number)
    objects_show = paginator.page(page_object.number).object_list

    if page_object.has_next():
        next_page = '?' + urllib.parse.urlencode({'page': page_object.next_page_number()})
    else:
        next_page = ''
    if page_object.has_previous():
        prev_page = '?' + urllib.parse.urlencode({'page': page_object.previous_page_number()})
    else:
        prev_page = ''

    context = {
        'objects': objects_show,
        'current_page': page_object.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
        'num_pages': list(range(1, paginator.num_pages + 1))
    }
    return context


def cart_parse(products_str):
    products = []
    products_in_cart_rest = products_str

    def str_parse(str_in, s1, s2):
        product_out = str_in[str_in.index(s1) + 1:str_in.index(s2)]
        parsed_out = {
            'product_out': product_out,
            'id': int(product_out.split(',')[0].split(':')[1]),
            'qty': int(product_out.split(',')[1].split(':')[1]),
            'products_rest': str_in[str_in.index(s2) + 1:]
        }
        return parsed_out

    for i in range(0, products_str.count('{')):
        product_from_cart = str_parse(products_in_cart_rest, '{', '}')
        products.append({
            'id': product_from_cart['id'],
            'qty': product_from_cart['qty']
        })
        products_in_cart_rest = product_from_cart['products_rest']

    return products

