from django.db import models

# Create your models here.


class Publishing(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    headquarter = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    image = models.ImageField(upload_to="author_img/",
                              default="author_img/person.jpg")

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category


class Book(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    publishing = models.ForeignKey(
        Publishing, on_delete=models.CASCADE, related_name="publishing", blank=True, null=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="author")
    isbn = models.SlugField(max_length=10)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to="book_img/", default="book_img/book.jpg")
    pdf = models.FileField(upload_to='book_pdf', blank=True, null=True)

    def __str__(self):
        return self.name
