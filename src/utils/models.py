from dataclasses import dataclass


@dataclass
class Note:
    content: str


@dataclass
class NoteValid(Note):
    title: str


@dataclass
class NoteInvalid(Note):
    title: int
