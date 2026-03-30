from behave import given, when, then

from src.api.note_api import NoteServiceApi
from src.utils.helpers import get_note_data, check_status_code, check_json_data


@given("Я имею случайные валидные данные для создания заметки")
def step_have_valid_data(context):
    context.data = get_note_data(1, True)
    context.note = NoteServiceApi()


@when("Я создаю заметку со случайными валидными данными")
def step_create_note(context):
    context.response = context.note.create_note(context.data)


@then('статус ответа должен быть "{status_code}"')
def check_code(context, status_code):
    check_status_code(context.response, int(status_code))


@then('созданная заметка имеет корректный "{field}"')
def check_field(context, field):
    check_json_data(context.response, context.data, field)


@given("Я имею случайные не валидные данные для создания заметки")
def step_have_invalid_data(context):
    context.data = get_note_data(1, False)
    context.note = NoteServiceApi()


@when("Я создаю заметку со случайным не валидным title")
def step_create_note(context):
    context.response = context.note.create_note(context.data)
