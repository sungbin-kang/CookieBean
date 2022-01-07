# Template Details


- base
    - base.html
    - home.html
- accounts
    - my_profile.html
    - my_orders.html
- shoppingcart
    - my_cart.html
- product
    - shop_cookies.html
    - cookie_detail.html
- admin
    - cookie_inventory.html
    - report.html
    - report_detail.html
    - order_detail.html






### `base.html`
a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages
- stylesheet
- base
    - header
        - signboard
            - logo
            - business-name
        - reginstration
            - login
            - signup
        - shoppingcart
        - navbar
            - about_us
            - shop_cookies
            - admin
                - report
                - order
                - inventory
    - content
    - footer
        - contact
        - location

### `home.html`
home page of the website
extends 'base.html'
- home
    - image


### `accounts.html`
a base template for account related pages
extends 'base.html'
- accounts-navbar
    - my_profile
    - my_orders
    - my_cart
- content

### `my_profile.html`
a view of the user's profile information
extends 'accounts.html'
- my_profile
    - username
    - edit my information

### `my_orders.html`
a view of the list of user's orders
extends 'accounts.html'
- my_orders


### `my_cart.html`
a view the list of products in the cart
extends 'accounts.html'


### `shop_cookies.html`
a view list of cookie products to be shopped
extends 'base.html'


### `cookie_detail.html`
a view of detail of a cookie


### `cookie_inventory.html`
a view of admin to edit cookie stock inventory


### `report.html`
a view of reports with revenue and profit


### `report_detail.html`
a detailed view of report of a specific product


### `order_detail.html`








### `login.html`
### `singup.html`
success_url = to the previous page 
HTTP_REFERER
ref: https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request/35796330



# View Details

<!-- ---------------------------- accounts ---------------------------- -->

https://github.com/justdjango/Shopping_cart/blob/master/accounts/views.py

@login_requried
def profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(owner=my_user_profile)
	context = {
		'my_orders' : my_orders,
	}

	return render(request, "profile.html", context)

| url      | "profile/"                           |
| -------- | ------------------------------------ |
| url-name | profile                              |




<!-- --------------------------- shoppingcart --------------------------- -->


https://github.com/justdjango/Shopping_cart/blob/master/accounts/views.py

shoppingcart/urls.py

app_name = "shopping_cart"



| url      | r'^shopping-cart/$'                           |
| -------- | ------------------------------------ |
| url-name | shopping_cart                              |


views.py

@login_requried
def shopping_cart(request):
    """
    returns the shopping cart view
    """
	my_profile = Profile.objects.filter(user=request.user).first()
	my_cart = Cart.objects.filter(profile=my_profile)
	context = {
		'my_cart' : my_cart,
	}

	return render(request, "shopping_cart.html", context) 




@login_requried
def add_quantity(request, product_id):
    """
    adds the product quantity by 1 in the logged in user's shoppin cart
    """
    my_profile = Profile.objects.filter(user=request.user).first()
    my_cart = Cart.objects.filter(profile=my_profile)
    product = Product.objects.get(product_id=product_id)

    entry, created = Entry.objects.get_or_create(cart=my_cart, product=product, defaults={"count": "0"})
    entry.count += 1
    entry.save()

    return redirect reverse("shopping_cart:shopping_cart")

| url      | r'^add-quantity/(?P<item_id>[-\w]+)/$'                           |
| -------- | ------------------------------------ |
| url-name | add_quantity                              |


@login_requried
def subtract_quantity(request, product_id):
    """
    adds the product quantity by 1 in the logged in user's shoppin cart
    """
    my_profile = Profile.objects.filter(user=request.user).first()
    my_cart = Cart.objects.filter(profile=my_profile)
    product = Product.objects.get(product_id=product_id)

    entry = Entry.obejcts.filter(cart=my_cart, product=produc_id)
    if entry.exists():
        if entry[0].count == 1:
            entry[0].delete()
        else:
            entry[0].count -= 1
            entry[0].save()

    return redirect reverse("shopping_cart:shopping_cart")

| url      | r'^subtract_quantity/(?P<item_id>[-\w]+)/$'                           |
| -------- | ------------------------------------ |
| url-name | add_to_cart                              |


@login_requried
def delete_from_cart(request, product_id):
    """
    deletes the product entry from the user's shopping cart
    """
    my_profile = Profile.objects.filter(user=request.user).first()
    my_cart = Cart.objects.filter(profile=my_profile)
    product = Product.objects.get(product_id=product_id)

    entry = Entry.obejcts.filter(cart=my_cart, product=produc_id)
    if entry.exists():
        entry[0].delete()
    
    return redirect(reverse("shopping_cart"))

| url      | r'^add-to-cart/(?P<item_id>[-\w]+)/$'                           |
| -------- | ------------------------------------ |
| url-name | add_to_cart                              |





<!-- --------------------------- products --------------------------- -->

app_name = "products"

def product_list(request):
    object_list = Product.objects.all()
    context = {
        "object_list" = object_list,
    }
    
    return render(request, "product_list.html", context)



def cookie_list(request):
    object_list = Cookie.objects.all()
    context = {
        "object_list" : object_list
    }

    return render(request, "shop_cookie.html", context)

| url      | "shop-cookies/"                           |
| -------- | ------------------------------------ |
| url-name | shop_cookies                              |













| url      | ""                 |
| -------- | ------------------ |
| url-name |                    |