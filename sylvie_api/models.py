from django.db import models

# Create your models here.

class Employee(models.Model):
    jobs = {
        'WT' : 'Mesero',
        'CK' : 'Cocinero',
        'CS' : 'Cajero'
    }
    
    employeeNumber = models.IntegerField('Numero de empleado', primary_key=True)
    name = models.TextField('Nombre', max_length=30, unique=True)
    job = models.CharField('Puesto', choices=jobs)

#Check if I need to rewrite save method to ensure name is unique
class Category(models.Model):
    categoryName = models.TextField('Categoría', max_length=30, unique=True)

#Check if I need to rewrite save method to ensure name is unique
class Product(models.Model):
    productName = models.TextField('Nombre del producto', max_length=30, unique=True)
    price = models.PositiveSmallIntegerField('Precio del producto')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
class Order(models.Model):
    tableNumber = models.PositiveSmallIntegerField('Numero de mesa')
    total = models.PositiveIntegerField('Total de la orden')
    waiter = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_product = models.ManyToManyRel(Product)