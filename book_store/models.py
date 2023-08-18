from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    #blank=True: frontend (form), this field may be blank
    #null=True: when a value isn't received, a NULL value is stored in the database. If False, a default needs to be given.

    #this method exists on every python class. In this case we are overriding it. This method changes how instances of the class should be output in the terminal. Right now, if we query the db using Book.objects.all(), we are returned: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]> , which is not very helpful.

    #"Self" is used to access the variable associated with the current instance. With the self keyword, you can access the attributes and methods of the class. (It is the same thing as "this").

    #You don't need to run migrations when you add methods to your classes, only when you change the structure of the class.
    def __str__(self):
        return f"{self.title} ({self.rating})"