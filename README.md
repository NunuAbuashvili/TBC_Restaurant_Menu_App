# Restaurant Catalog API #

A Django REST Framework-based API for managing restaurant catalogs, menus, and food items.


## Features ##

- User registration system with custom user model.
- User authentication system with JWT authentication.
- Restaurant management.
- Hierarchical menu system:
  - Main categories (e.g., Food, Drinks)
  - Subcategories (e.g., Traditional Hot Dishes, Non-alcoholic Beverages)
  - Menu items.
  - Ingredients.
- Image handling for restaurants, subcategories, and menu items.
- Filtering capabilities for menu items and subcategories.
- Permission-based access control.


## Technical Stack ##

- Python 3.8+
- Django 3.2+
- Django REST Framework
- JWT (for authentication)
- Django Filter
- Pillow (for image handling)

## Installation ##

1. Clone the repository:
```
clone https://github.com/NunuAbuashvili/TBC_Restaurant_Menu_App.git
cd restaurant_menu
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Run migrations:
```
python manage.py migrate
```
4. Create a superuser:
```
python manage.py createsuperuser
```
5. Run the development server:
```
python manage.py runserver
```

## API Endpoints ## 

### Authentication ###
- `/account/signup`: User registration
- `/account/token/`: Obtain JWT token
- `/account/token/refresh/`: Refresh JWT token

### Restaurants ###
- `GET /restaurant/catalog`: List of all restaurants
- `POST /restaurant/catalog`: Create a new restaurant (authenticated users only)

### Menu ###
- `GET /menu/main-category-viewset`: List main categories
- `POST /menu/main-category-viewset`: Create new main category (authenticated users only)
- `GET /menu/subcategory-viewset`: List subcategories with filtering options
- `POST /menu/subcategory-viewset`: Create new subcategory (authenticated users only)
- `GET /menu/subcategory-viewset/<int:pk>`: Retrieve detailed view of a subcategory.
- `PUT /menu/subcategory-viewset/<int:pk>`: Update subcategory (authenticated users only)
- `GET /menu/menu-item-viewset`: List menu items with filtering options
- `PUT /menu/menu-item-viewset`: Create menu item (authenticated users only)
- `GET /menu/menu-item-viewset/<int:pk>`: Retrieve detailed view of a menu item
- `PUT /menu/menu-item-viewset/<int:pk>`: Update menu item (authenticated users only)


## Authentication ##
The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:
```
Bearer <your_token_here>
```
 

## Permissions ##
- Unauthenticated users can view all data.
- Only authenticated users can create/modify restaurants and menu items.


## Data Models ##
- `CustomUser`: Extended user model for authentication
- `Restaurant`: Basic restaurant information
- `MainCategory`: Top-level menu categories
- `SubCategory`: Second-level menu categories
- `MenuItem`: Individual menu items
- `Ingredient`: Ingredients of menu items


## Contributing ##
This project is part of a learning process. While contributions are welcome, please note that major changes may be implemented as part of the learning journey.
