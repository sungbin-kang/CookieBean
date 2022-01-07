# View Details

<!-- ---------------------------- base ---------------------------- -->
url-prefix : ""

signup(request)
    creates new user
url : "signup/"

logout_request(request)
    returns the view to logout
url : "logout/"
url-name : logout

<!-- ---------------------------- profile ---------------------------- -->

url-prefix : "profile/"

view_profile(request)
    returns the view user's profile
url : ""
url-name : my_profile

view_order(request)
    returns the list of user's orders
url : "my-orders/"
url-name : my_orders


<!-- --------------------------- shoppingcart --------------------------- -->

url-prefix : "my-cart/"

view_shopping_cart(request)
    returns user's shopping cart view
url : ""
url-name : my_cart

add_quantity(request, product_id)
    adds quantity of the product by 1 from user's shopping cart
url : "add-quantity/<product_id>>"
url-name : add_quantity

subtract_quantity(request, product_id)
    subtracts quantity of the product by 1 from user's shopping cart
url : "subtract-quantity/<product_id>>"
url-name : subtract_quantity

delete_from_cart(request, product_id)
    deletes the product entry from the user's shopping cart
url : "delete-product/<product_id>"
url-name : delete_product

checkout_order(request)
    puts order to the report
url : "checkout-order/"
url-name : checkout_order



<!-- --------------------------- products --------------------------- -->

url-prefix : "products/"

shop_cookie(request)
    returns list of cookies
url : "shop-cookies/"
url-name : shop_cookies

cookie_detail(request, product_id)
    returns the detail of the cookie
url : "cookie-detail/<product_id>"
url-name : cookie_detail 

add_to_cart(request, product_id)
    add the product into user's shopping cart
url : "add-to-cart/<product_id>"
url-name : add_to_cart


<!-- ---------------------------- admin ---------------------------- -->

url-prefix : "admin/"

<!-- product_inventory_list(request)
    return the list of inventory for company products
url : "product-inventory"
url-name : product_inventory -->


<!-- cookie -->

cookie_inventory_list(request)
    return the list of inventory for cookie ingredient
url : "cookie-inventory"
url-name : cookie_inventory

restock_cookie(request)
    restocks the number of cookie in the inventory
url : "restock-cookie/<product_id>"
url-name : restock_cookie

create_cookie(request):
    creates a cookie object into the product list and productinventory object to track inventory
url : "create-cookie"
url-name : create_cookie

edit_cookie(request):
    edits cookie object
url : "edit-cookie/<product_id>"
url-name : edit_cookie

delete_cookie(request):
    deletes cookie object 
url : "delete-cookie/<product_id>"
url-name : delete_cookie


<!-- report -->

view_report(request):
    returns revenue and profit with the list of product sales
url : "report/"
url-name : report

view_report(request, date):
    returns revenue and profit with the list of product sales during the selected period of time
url : "report/<dateandtime>"
url-name : report

report_detail(request, product_id):
    returns the revenue and profit of the specific product
url : "report-detail/<product_id>"
url-name : report_detail

order_detail(request, username):
    returns detail of the specific user's order
url : "order-detail/<username>"
url-name : order_detail


<!-- ingredient -->

<!-- create_ingredient(request):
    creates an ingredient object into the ingredeint list
url: "create-ingredient"
url-name : create_ingredient

edit_ingredient(request):
    edits ingredient object
url : "edit-ingredient/<ingredeint_id>"
url-name : edit_ingredient

delete_ingredient(request):
    deletes ingredient object 
url : "delete-ingredient/<ingredient_id>"
url-name : delete_ingredient -->


<!-- recipe requirement -->

<!-- create_recipe(request):
    creates an recipe object into the recipe list
url: "create-recipe"
url-name : create_recipe

edit_recipe(request):
    edits recipe object
url : "edit-recipe/<recipe_id>"
url-name : edit_recipe

delete_recipe(request):
    deletes recipe object 
url : "delete-recipe/<recipe_id>"
url-name : delete_recipe -->