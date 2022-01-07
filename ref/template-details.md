# Template Details

### Template Directory

- base
    - base.html
    - home.html
    - registration
        - login.html
        - signup.html
- profile
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


### Details

**`base.html`** : a base template for all the other pages to inherit from, with common styling and a navbar linking to the other pages
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

**`home.html`** : home page of the website
- extends 'base.html'
- home
    - image


**`profile.html`** : a base template for account related pages
- extends 'base.html'
- profile-navbar
    - my_profile
    - my_orders
    - my_cart
- content

**`my_profile.html`** : a view of the user's profile information
- extends 'profile.html'
- my_profile
    - username
    - edit my information

**`my_orders.html`** : a view of the list of user's orders
- extends 'profile.html'
- my_orders


**`my_cart.html`** : a view the list of products in the cart
- extends 'profile.html'


**`shop_cookies.html`** : a view list of cookie products to be shopped
extends 'base.html'


**`cookie_detail.html`** : a view of detail of a cookie


**`cookie_inventory.html`** : a view of admin to edit cookie stock inventory


**`report.html`** : a view of reports with revenue and profit


**`report_detail.html`** : a detailed view of report of a specific product


**`order_detail.html`** : 
