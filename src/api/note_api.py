import requests

from src.utils.config_loader import Config


class NoteServiceApi:
    def __init__(self):
        config = Config()
        self.base_url = config.get("API", "base_url")
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_note_all(self):
        response = requests.get(f'{self.base_url}/notes')
        return response

    def get_note_by_id(self, note_id):
        response = requests.get(f'{self.base_url}/notes/{note_id}')
        return response

    def create_note(self, note):
        response = requests.post(f'{self.base_url}/notes', json=note, headers=self.headers)
        return response

    def update_note(self, note_id, note):
        response = requests.put(f'{self.base_url}/notes/{note_id}', json=note, headers=self.headers)
        return response

    def delete_note_by_id(self, note_id):
        response = requests.delete(f'{self.base_url}/notes/{note_id}')
        return response

    def delete_note_all(self):
        all_notes = self.get_note_all().json()
        for note in all_notes:
            self.delete_note_by_id(note["id"])
