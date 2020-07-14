from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    LOCATION = (
        ('---', '---'),
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('left', 'Left'),
        ('right', 'Right')

    )
    TEMPLATE = (
        ('phone', 'Телефон'),
        ('cultural', 'Культура'),
        ('miscellaneous', 'Разный')
    )
    name = models.CharField(verbose_name='Name', max_length=30)
    template_name = models.CharField(max_length=30, choices=TEMPLATE, default='Разный')
    location = models.CharField(max_length=30, choices=LOCATION, default='---')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='User')
    price = models.CharField(verbose_name='Price', max_length=10)
    qty = models.CharField(verbose_name='Quantity', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + '_' + str(self.id) + '_' + str(self.price)


class Product(models.Model):
    STATUS_CHOICE = (
                    ('available', 'Available'),
                    ('not available', 'Not available'),
                    ('awaiting delivery', 'Awaiting delivery'),
                    ('discontinued', 'Discontinued')
                    )
    id = models.AutoField(verbose_name='ID', primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=30)
    price = models.CharField(verbose_name='Price', max_length=10)
    qty = models.CharField(verbose_name='Quantity', max_length=10)
    image = models.CharField(verbose_name='Image', max_length=128)
    release_date = models.DateField(verbose_name='Release date')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default='available')
    slug = models.SlugField(max_length=100)
    cart = models.ManyToManyField(Cart, through='ProductsInCart', verbose_name='Корзина')

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICE = (
                    ('1', '★'),
                    ('2', '★★'),
                    ('3', '★★★'),
                    ('4', '★★★★'),
                    ('5', '★★★★★')
                    )
    publish_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Author\'s name', max_length=30)
    text = models.TextField(verbose_name='Review text', max_length=255)
    rating = models.CharField(max_length=30, choices=RATING_CHOICE, default='1')

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]


class Phone(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField(verbose_name='Model', max_length=30)
    cpu = models.CharField(verbose_name='CPU type', max_length=15)
    cpu_cores = models.DecimalField(verbose_name='CPU cores', max_digits=3, decimal_places=0)
    ram = models.DecimalField(verbose_name='RAM Gb', max_digits=3, decimal_places=0)
    int_flash = models.DecimalField(verbose_name='Internal flash disk Gb', max_digits=10, decimal_places=0)
    ext_flash_type = models.CharField(verbose_name='External flash support', max_length=30)
    ext_flash = models.DecimalField(verbose_name='External flash disk Gb', max_digits=10, decimal_places=0)
    cam = models.CharField(verbose_name='Cameras', max_length=30)
    gsm_ranges = models.CharField(verbose_name='GSM work ranges', max_length=30)
    internet = models.CharField(verbose_name='Mobile internet work range', max_length=30)
    pay = models.CharField(verbose_name='Pay system support', max_length=30)
    display_type = models.CharField(verbose_name='Display type', max_length=30)
    display_size = models.DecimalField(verbose_name='Display size (inch)', max_digits=5, decimal_places=2)
    nav = models.CharField(verbose_name='Navigation support', max_length=30)
    os = models.CharField(verbose_name='OS version', max_length=30)
    sim_type = models.CharField(verbose_name='SIM-card type', max_length=30)
    sim_cards = models.DecimalField(verbose_name='SIM-cards quantity ', max_digits=2, decimal_places=0)
    accum_capacity = models.DecimalField(verbose_name='Accumulator capacity', max_digits=10, decimal_places=0)
    body = models.CharField(verbose_name='Type of body', max_length=30)
    color = models.CharField(verbose_name='Color', max_length=30)
    dimensions = models.CharField(verbose_name='Dimensions', max_length=30)
    weight = models.DecimalField(verbose_name='Weight g', max_digits=10, decimal_places=0)
    description = models.TextField(verbose_name='Description text', max_length=255)

    def __str__(self):
        return str(self.product.name) + ' ' + str(self.model)


class Cultural(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    symbol = models.CharField(verbose_name='Symbol of...', max_length=30)
    rarity = models.CharField(verbose_name='Rarity or exclusive', max_length=30)
    description = models.TextField(verbose_name='Description text', max_length=255)

    def __str__(self):
        return str(self.product.name)


class Miscellaneous(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description text', max_length=255)

    def __str__(self):
        return str(self.product.name)


class ProductsInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.DecimalField(verbose_name='Количество', max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return '{0}_{1}'.format(self.cart, self.product)


