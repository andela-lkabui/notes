import factory
from api import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NotesUser

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda a: '{0}.{1}'.format(a.first_name, a.last_name).lower())
    password = factory.Faker('password')
    email = factory.LazyAttribute(lambda a: '{0}.{1}@notesapi.com'.format(a.first_name, a.last_name).lower())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        return model_class.objects.create_user(**kwargs)

class NoteFactory(factory.Factory):
    class Meta:
        model = models.Notes

    title = factory.Faker('sentence')
    note = factory.Faker('paragraph')
    owner = factory.SubFactory(UserFactory)