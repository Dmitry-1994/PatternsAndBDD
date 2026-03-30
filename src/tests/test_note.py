# Создание заметок. Успешное создание заметки с валидными данными
from src.api.note_api import NoteServiceApi
from src.utils.helpers import get_note_data, check_status_code, check_json_data, check_json_data_all, get_id


def test_success_create_note_with_valid_data():
    data1 = get_note_data(1, True)
    note_api = NoteServiceApi()
    response = note_api.create_note(data1)
    check_status_code(response, 200)
    check_json_data(response, data1, "title")
    check_json_data(response, data1, "content")


# Создание заметок. Неуспешное создание заметки с не валидными данными
def test_unsuccess_create_note_with_invalid_data():
    data1 = get_note_data(1, False)
    note_api = NoteServiceApi()
    response = note_api.create_note(data1)
    check_status_code(response, 422)


# Получение списка заметок. Когда заметок нет
def test_success_get_all_without_note():
    note_api = NoteServiceApi()
    note_api.delete_note_all()
    response = note_api.get_note_all()
    check_status_code(response, 200)
    assert response.json() == []


# Получение списка заметок. Когда заметки есть
def test_success_get_all_with_note():
    data1, data2 = get_note_data(2, True)
    note_api = NoteServiceApi()
    note_api.create_note(data1)
    note_api.create_note(data2)
    response = note_api.get_note_all()
    check_status_code(response, 200)
    check_json_data_all(response, [data1, data2])


# Получение заметки по id. По валидному id
def test_get_note_by_valid_id():
    data1 = get_note_data(1, True)
    note_api = NoteServiceApi()
    note_api.delete_note_all()
    expected = note_api.create_note(data1).json()
    valid_id = get_id(True)
    response = note_api.get_note_by_id(valid_id)
    check_status_code(response, 200)
    assert response.json() == expected


# Получение заметки по id. По не валидному id
def test_get_note_by_invalid_id():
    note_api = NoteServiceApi()
    invalid_id = get_id(False)
    response = note_api.get_note_by_id(invalid_id)
    expected_data = {"detail": "Note not found"}
    check_status_code(response, 404)
    check_json_data(response, expected_data, "detail")


# Редактирование заметки по id. По валидному id
def test_update_note_by_valid_id():
    data1, data2 = get_note_data(2, True)
    note_api = NoteServiceApi()
    note_api.create_note(data1).json()
    valid_id = get_id(True)
    note_api.update_note(valid_id, data2)
    response = note_api.get_note_by_id(valid_id)
    check_status_code(response, 200)
    check_json_data(response, data2, "title")
    check_json_data(response, data2, "content")


# Редактирование заметки по id. По не валидному id
def test_update_note_by_invalid_id():
    data1 = get_note_data(1, True)
    invalid_id = get_id(False)
    note_api = NoteServiceApi()
    response = note_api.update_note(invalid_id, data1)
    expected_data = {"detail": "Note not found"}
    check_status_code(response, 404)
    check_json_data(response, expected_data, "detail")


# Удаление заметки по id. По валидному id
def test_delete_note_by_valid_id():
    data1, data2 = get_note_data(2, True)
    note_api = NoteServiceApi()
    note_api.delete_note_all()
    note_api.create_note(data1)
    create_note = note_api.create_note(data2).json()
    response = note_api.delete_note_by_id(create_note["id"])
    expected_data = {"detail": "Note deleted"}
    check_status_code(response, 200)
    check_json_data(response, expected_data, "detail")
    get_note_after_delete = note_api.get_note_all()
    check_json_data_all(get_note_after_delete, [data1])


# Удаление заметки по id. По не валидному id
def test_delete_note_by_invalid_id():
    note_api = NoteServiceApi()
    invalid_id = get_id(False)
    response = note_api.delete_note_by_id(invalid_id)
    expected_data = {"detail": "Note not found"}
    check_status_code(response, 404)
    check_json_data(response, expected_data, "detail")
