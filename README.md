# Cookie Bean - Django Website

# Overview
This website is to help the cookie business customers and admins to keep track of products and sales.

The website provides secure login platform for both customer and admin.

If you are a customer you can view the website as a guest or registered customer.
    Anyone can:
    - browse website products
    Registered Customers can:
    - shop website products
    <!-- - leave review -->
    <!-- - build your own cookies -->

If you are an admin, you are able to add and edit product and ingredient information in the list, restock items, and view and manage orders.


# Technical Skills
- HTML
- CSS
- Python
- Django
- Git
- Command Line


# Apps and Database Models

<!-- ---------------------------- accounts ---------------------------- -->
### accounts

  
**`Profile`** : This model represents a profile of user's account
- Attributes:
    - `user` : the user of this shopping cart - OneToOneField(User)
- Methods:
    - `get_username()` : returns user's username
    - `get_userid()` : returns user's unique id 
    - `is_staff()` : true if user is a staff; otherwise, false
  

<!-- --------------------------- shoppingcart --------------------------- -->
### shoppingcart

  
**`Cart`** : This model represents a shopping cart
- Attributes:
    - `profile` : the associated profile of this shopping cart - OneToOneField(Profile)
    - `count` : the total number of the products in the cart
    - `total` : the total cost of the products in the cart(including sales tax)
- Methods:
    - `get_items()` : returns queryset of Products that are in this cart

  
**`Entry`** : This model represents an entry of products in shopping cart
- Attributes:
    - `cart` : the shopping cart of this entry - OneToOneField(Cart)
    - `order` : the order of this entry - ForeingKey(Order)
    - `product` : the product of this entry in the shopping cart - ForeignKey(Product)
    - `count` : the quantity of the product of this entry 
- Methods:

  
**`Order`** : This model represents an order of a customer
- Attributes:
    - `order_id` : an order unber generated uniquely for each order - AutoField(primary_key=True)
    - `owner_profile` : this order owner's profile - ForeignKey(Profile)
    - `total_count` : the total count of products in this order
    - `total_price` : the total price of this order
    - `timestamp` : the timestamp of when this order was made
    <!-- - `ready-to-ship` :  -->
    <!-- - `shipped` :  -->
- Methods:

  
<!-- ---------------------------- product ---------------------------- -->
### product
  

**`Product`** : This model represents a product of the company
- Attributes:
    - `name` : the name of this item
    - `product_id` : the unique id of this item - AutoField(primary_key=True)
    - `price` : the price of this product
- Methods:

  
<!--  Cookie(Product)  -->

**`Cookie`(`Product`)** : This model represents a cookie type of a product
- Attributes:

<!-- `Ingredient`
This model represents an ingredient that the company has in its inventory
Attributes:
- `name` : the name of the ingredient (i.e. `flour`)
- `ingredient_id` : the unique id of this product
    AutoField(primary_key=True)
- `price_per_ounce` : the price per unit of the ingredient

`RecipeRequirement`
This model represents a single ingredient and how much of it is required for an item
Attributes:
- `item` : 
    ForiegnKey
- `ingredient` : 
    OneToOneField
- `quantity_in_gram` : -->
  
<!-- ---------------------------- inventory ---------------------------- -->
### inventory

  
**`Inventory`** : This model represents a inventory of product
- Attributes:
    - `product` : the product of this inventory management system - OneToOneField(Product)
    - `quantity` : the quantity in the inventory
    - `low` : the quantity that indicates the inventory stock is in low
- Methods:
    - `is_low(): boolean` : returns true if stock quantity goes below a set amount; otherwise, false
    - `is_in_stock(): boolean` : returns true if in stock; otherwise, false


<!-- `IngredientInventory`(`Inventory`)
This model represents a stock management system for cookie ingredient 
Attributes:
- `ingredeint` : the ingredient to manage stock
- `quantity_in_gram` : the quantity of the ingredeint available in the inventory in unit of grams
Methods:
- `enough(): -> boolean` : returns true if there are enough amount left in the inventory -->

  
# Views and Templates Overview

- base.html
    - home.html
        - login.html
        - signup.html
        - profile.html
            - my_orders.html
            - my_cart.html
        - about_us.html
        - shop_cookies.html
            - cookie_detail.html
        - |admin.html
            - |cookie_inventory.html
                - |restock_cookie.html
                - |create_cookie.html
                - |edit_cookie.html
                - |delete_cookie.html
            - |order_list.html
            - |report.html



`base.html`
a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages

`home.html`
home page of the website
