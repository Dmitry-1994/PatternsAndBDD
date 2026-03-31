from behave import given, when, then

from src.api.note_api import NoteServiceApi
from src.utils.helpers import get_note_data, check_status_code, check_json_data, check_json_data_all, get_id


@given("I have random valid data to create a note.")
def step_have_valid_data(context):
    context.data = get_note_data(1, True)
    context.note_api = NoteServiceApi()


@when("I'm creating a note with random valid data.")
def step_create_note(context):
    context.response = context.note_api.create_note(context.data)


@then('the response status should be "{status_code}"')
def check_code(context, status_code):
    check_status_code(context.response, int(status_code))


@then('the created note has the correct "{field}"')
def check_field(context, field):
    check_json_data(context.response, context.data, field)


@given("I have random invalid data to create a note.")
def step_have_invalid_data(context):
    context.data = get_note_data(1, False)
    context.note_api = NoteServiceApi()


@when("I'm creating a note with a random invalid title.")
def step_create_note(context):
    context.response = context.note_api.create_note(context.data)


@given("I have two created notes notes note_1 and note_2")
def step_have_valid_data(context):
    context.note_1, context.note_2 = get_note_data(2, True)
    context.note_api = NoteServiceApi()
    context.note_api.delete_note_all()
    context.note_api.create_note(context.note_1)
    context.created_note = context.note_api.create_note(context.note_2).json()


@when('I am deleting a note_2 by its id')
def step_delete_note_by_valid_id(context):
    context.response = context.note_api.delete_note_by_id(context.created_note["id"])


@then('the text in the body of the "{body_response_text}" response')
def step_check_response(context, body_response_text):
    expected_data = {"detail": body_response_text}
    check_json_data(context.response, expected_data, "detail")


@then('the list of received notes consists of note_1')
def step_check_note_after_delete(context):
    get_note_after_delete = context.note_api.get_note_all()
    check_json_data_all(get_note_after_delete, [context.note_1])

@given("I have a random invalid note id.")
def step_have_invalid_id(context):
    context.note_api = NoteServiceApi()
    context.invalid_id = get_id(False)

@when("I am deleting a note with an invalid id.")
def step_delete_note_by_invalid_id(context):
    context.response = context.note_api.delete_note_by_id(context.invalid_id)
