import factory

from src.utils.models import NoteValid, NoteInvalid


class BaseNoteFactory(factory.Factory):
    class Meta:
        abstract = True

    content = factory.Faker("text")


class NoteFactory(BaseNoteFactory):
    class Meta:
        model = NoteValid

    title = factory.Faker("name")


class NoteFactoryInvalid(BaseNoteFactory):
    class Meta:
        model = NoteInvalid

    title = factory.Faker("pyint")
