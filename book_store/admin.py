from django.contrib import admin

from .models import Book

# Register your models here.

# set options through properties and fields for this class which is then reflected in the admin page
class BookAdmin(admin.ModelAdmin):
    #this shows the field in the admin side but you can't edit it. So we can either do this, or in the model.py add editable=False, both work.

    readonly_fields = ("slug",)

    #this makes it so that when filling out the book form, the slug will prepopulate before you hit save, so that you can see what the slug will be. Otherwise, the slug field is filled after hitting save (based on our Book.save() method).

    #for prepopulated_fields to work, I have to remove "slug" from readonly as it throws an error that it doesn't exist (can't be prepopulated, or modified)
    #prepopulated_fields = {"slug": ("title",)}

    #with the prepopulated_fields and allowing the user to edit the fields, we can remove the Book.save() method as we don't need it anymore. I'm going to leave it just to show it.

    #add a filtering system into the django admin for Books. 
    list_filter = ("author", "rating",)

    #add column titles for the list display of books 
    list_display = ("title", "author",)

#admin.site.register(Book)
admin.site.register(Book, BookAdmin)