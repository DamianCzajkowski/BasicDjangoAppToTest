import factory
from factory.fuzzy import FuzzyText, FuzzyDate
from . import models
import datetime


class BlogFactory(factory.Factory):
    class Meta:
        model = models.Blog

    name = FuzzyText(length=10, prefix='name_')
    tagline = FuzzyText(length=120)


class AuthorFactory(factory.Factory):
    class Meta:
        model = models.Author

    name = FuzzyText(max_length=200)
    email = factory.Sequence(lambda n: 'person{}@example.com'.format(n))


class EntryFactory(factory.Factory):
    class Meta:
        model = models.Entry

    blog = BlogFactory
    headline = FuzzyText(length=120)
    body_text = factory.Faker('random_text')
    pub_date = FuzzyDate(datetime.date(2008, 1, 1))
    mod_date = FuzzyDate(datetime.date(2008, 1, 1))
    authors = AuthorFactory
    number_of_comments = factory.Faker('random_int')
    number_of_pingbacks = factory.Faker('random_int')
    rating = factory.Faker('random_int')
