#  Django Inventory & Stock Management System

This project is a **Django-based Inventory and Stock Management System** designed to simplify the process of managing **stores, products, suppliers, customers, purchases, and sales**.  

It provides a **dashboard with key business metrics**, CRUD functionality for resources, and automatic stock updates when purchases or sales are made.  

Built as my **Capstone Project**, this system demonstrates practical backend development skills in **Python, Django, and databases**.  

---

##  Core Features

### Inventory Management
- Add, update, and delete **stores** and **categories**.  
- Manage **products** with supplier and category assignments.  
- Track stock quantity in real time.  

###  Purchases
- Create purchase orders from suppliers.  
- Automatically **increase product stock** when purchases are recorded.  
- View a list of all purchases in reverse chronological order.  

### Sales
- Create sales orders for customers.  
- System validates stock availability before confirming sale.  
- Automatically **decrease product stock** when sales are completed.  
- Error messages displayed if stock is insufficient.  

### Dashboard & Reporting
- Overview of **total stores, categories, products, customers, purchases, and sales**.  
- Aggregated statistics:
  - Total purchased & sold quantities  
  - Total purchase value  
  - Total sales value  
- Clean dashboard UI for quick insights.  

### Customers & Suppliers
- Manage **customer records** with full CRUD functionality.  
- Manage **supplier records** linked to products.  

---

## Tech Stack

- **Backend**: Django (Python)  
- **Database**: SQLite (default) – compatible with PostgreSQL/MySQL  
- **Frontend**: Django Templates (HTML, CSS, Bootstrap/Tailwind)  
- **ORM**: Django ORM (queries, aggregation, expressions)  
- **Authentication**: Django built-in user model  

---

##  Project Structure







---

##  Main Endpoints (Views)

###  Authentication
- `/` → Welcome page for unauthenticated users  
- `/dashboard/` → Main dashboard (authenticated users only)  

###  Inventory
- `/stores/` → List & add stores  
- `/stores/<id>/` → View/update/delete a store  
- `/categories/` → List & add categories  
- `/categories/<id>/` → View/update/delete a category  
- `/products/` → List & add products  
- `/products/<id>/` → View/update/delete a product  

###  Purchases
- `/purchases/` → List all purchases  
ad- `/purchases/new/` → Create new purchase order  

###  Sales
- `/sales/` → List all sales  
- `/sales/new/` → Create new sales order  

###  People
- `/customers/` → List & add customers  
- `/customers/<id>/` → View/update/delete customer  
- `/suppliers/` → List & add suppliers  
- `/suppliers/<id>/` → View/update/delete supplier  

---
