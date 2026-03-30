import random

from src.api.note_api import NoteServiceApi
from src.utils.models import NoteInvalid, Note
from src.utils.note_factory import NoteFactory, NoteFactoryInvalid


def check_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code


def check_json_data(response, expected, args=None):
    assert response.json()[args] == expected[args], "Значения ключа в response и expected разные"


def check_json_data_all(response, expected: list):
    cnt = 0
    for item_e in expected:
        for item_r in response.json():
            tmp = {
                "title": item_r["title"],
                "content": item_r["content"]
            }
            if tmp["title"] == item_e["title"] and tmp["content"] == item_e["content"]:
                cnt += 1
    assert True if cnt == len(expected) else False


def get_note_data(count: int, isvalid: bool):
    result = []
    for i in range(count):
        tmp = {}
        note = NoteFactory() if isvalid else NoteFactoryInvalid()
        tmp["title"] = note.title
        tmp["content"] = note.content
        result.append(tmp)
    if count == 1:
        return result[0]

    return result


def get_id(is_valid=True):
    note_api = NoteServiceApi()
    note_list = note_api.get_note_all().json()
    id_list = []
    if note_list:
        for note in note_list:
            id_list.append(note["id"])
        id_list.sort()
        if is_valid:
            return random.choice(id_list)
        else:
            return id_list[-1] + 1
    else:
        return 1
