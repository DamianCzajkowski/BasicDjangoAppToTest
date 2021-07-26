import pytest

from apps.library.models import *
from apps.library.factories import *
import datetime


# pytestmark = pytest.mark.django_db

"""
    If you want to run this file type: pytest -s apps/library/tests/test_queries.py

"""


class TestCreatingObject:

    @pytest.mark.order(1)
    def test_initial(self):
        print("-"*50)
        print("TEST CREATING OBJECTS")

    @pytest.mark.order(2)
    @pytest.mark.django_db
    def test_create(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()

        result = Blog.objects.all()
        # import pdb; pdb.set_trace()
        print("TEST CREATING OBJECT RESULT: ", result)

    @pytest.mark.order(3)
    @pytest.mark.django_db
    def test_update(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()

        blog = Blog.objects.get(pk=blog.pk)
        blog.name = "Another test name"
        blog.tagline = "AAAAAa"
        blog.save(update_fields=["name"])  # It saves only field in list

        # import pdb; pdb.set_trace()
        result = Blog.objects.get(pk=blog.pk)
        print("TEST UPDATING OBJECT RESULT: ", result.name, result.tagline)

    @pytest.mark.order(4)
    @pytest.mark.django_db
    def test_saving_foreign_key(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()
        entry = EntryFactory.create()
        entry.name = "Test name of Entry"
        entry.blog = blog
        entry.save()
        # import pdb; pdb.set_trace()
        result = Entry.objects.get(pk=entry.pk)
        print("TEST SAVING FOREIGN KEY: ", result.headline, result.blog)

    @pytest.mark.order(5)
    @pytest.mark.django_db
    def test_saving_many_to_many(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()
        entry = EntryFactory.create()
        entry.name = "Test name of Entry"
        entry.blog = blog
        entry.save()

        author = AuthorFactory.create()
        author.save()
        entry.authors.add(author)

        john = Author.objects.create(name="John")
        paul = Author.objects.create(name="Paul")
        george = Author.objects.create(name="George")
        entry.authors.add(john, paul, george)

        # import pdb; pdb.set_trace()
        result = Entry.objects.get(pk=entry.pk)
        print("TEST SAVING MANY TO MANY: ",
              result.headline, result.authors.all())

    @pytest.mark.order(6)
    @pytest.mark.django_db
    def test_saving_one_to_one(self):
        pass  # to create


class TestRetrievingObject:

    @pytest.mark.order(7)
    def test_initial(self):
        print("-"*50)
        print("TEST RETRIEVING OBJECTS")

    @pytest.mark.order(8)
    @pytest.mark.django_db
    def test_objects(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()
        result = Blog.objects
        print("TEST OBJECTS: ", result)

    @pytest.mark.order(9)
    @pytest.mark.django_db
    def test_objects_all(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()
        result = Blog.objects.all()
        print("TEST OBJECTS ALL: ", result)

    @pytest.mark.order(10)
    @pytest.mark.django_db
    def test_filter(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()

        # INSTED OF YOU CAN USE Blog.objects.all().filter(name__exact="Test_name")
        result = Blog.objects.filter(name__exact="Test_name")
        print("TEST OBJECTS FILTER: ", result)
    
    @pytest.mark.order(11)
    @pytest.mark.django_db
    def test_filter(self):
        blog = Blog(name="Test_name", tagline="Test tagline")
        blog.save()
        entry = EntryFactory.create(headline="What a mess", pub_date=datetime.date.today())
        entry.name = "Test name of Entry"
        entry.blog = blog
        entry.save()

        author = AuthorFactory.create()
        author.save()
        entry.authors.add(author)


        result = Entry.objects.filter(headline__startswith="What").exclude()
        print("TEST OBJECTS FILTER: ", result)


# class TestQueringJSONField:
#     @pytest.mark.order(1)
#     def test(self):
#         pass
