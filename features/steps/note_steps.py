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

@given("Я имею две созданные заметки заметки note_1 и note_2")
def step_have_valid_data(context):
    context.note_1, context.note_2 = get_note_data(2, True)
    context.note_api = NoteServiceApi()
    context.note_api.delete_note_all()
    context.note_api.create_note(context.note_1)
    context.created_note = context.note_api.create_note(context.note_2).json()

@when('Я удаляю заметку note_2 по ее id')
def step_delete_note_by_valid_id(context):
    context.response = context.note_api.delete_note_by_id(context.created_note["id"])

@then('текст в теле ответа "{body_response_text}"')
def step_check_response(context, body_response_text):
    expected_data = {"detail": body_response_text}
    check_json_data(context.response, expected_data, "detail")
