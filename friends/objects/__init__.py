from typing import List


class Token:
    def __init__(self, tid: int = -1, text: str = ""):
        self.id = tid
        self.text = text


class CharacterEntity:
    def __init__(self, start: int = -1, end: int = -1, entity: str = ""):
        self.start = start
        self.end = end
        self.entity = entity


class Utterance:
    def __init__(
            self,
            uid: int = -1,
            speakers: List[str] = (),
            transcript: str = "",
            sentences: List[List[Token]] = (),
            transcript_with_note: str = "",
            tokens_with_note: str = (),
            character_entities: List[List[CharacterEntity]] = ()
    ):
        self.id = uid
        self.speakers = speakers
        self.transcript = transcript
        self.sentences = sentences
        self.transcript_with_note = transcript_with_note
        self.tokens_with_note = tokens_with_note
        self.character_entities = character_entities


class Scene:
    def __init__(self, cid: int = 0, utterances: List[Utterance] = ()):
        self.id = cid
        self.utterances = utterances


class Episode:
    def __init__(self, eid: int = 0, scenes: List[Scene] = ()):
        self.id = eid
        self.scenes = scenes


class Season:
    def __init__(self, sid: int = 0, episodes: List[Episode] = ()):
        self.id = sid
        self.episodes = episodes
