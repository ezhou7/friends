import json
import os
from typing import Any

from friends.objects import *


def load():
    package_path = os.path.abspath(os.path.dirname(__file__))
    src_dir = os.path.join(package_path, "json")

    seasons = []
    for filename in os.listdir(src_dir):
        src_filepath = os.path.join(src_dir, filename)
        with open(src_filepath, "r") as fin:
            json_obj = json.load(fin)

        season = load_season(json_obj)
        seasons.append(season)

    return seasons


def load_season(json_obj: dict):
    season = Season()

    sid = json_obj.get("sid")
    set_attribute_if_not_null(season, "id", sid)

    json_episodes = json_obj.get("episodes")
    episodes = load_episodes(json_episodes)
    set_attribute_if_not_null(season, "episodes", episodes)

    return season


def load_episodes(json_episodes: List[dict]):
    return [load_episode(json_episode) for json_episode in json_episodes]


def load_episode(json_obj: dict):
    episode = Episode()

    eid = json_obj.get("eid")
    set_attribute_if_not_null(episode, "id", eid)

    json_scenes = json_obj.get("scenes")
    scenes = load_scenes(json_scenes)
    set_attribute_if_not_null(episode, "scenes", scenes)

    return episode


def load_scenes(json_scenes: List[dict]):
    return [load_scene(json_scene) for json_scene in json_scenes]


def load_scene(json_obj: dict):
    scene = Scene()

    cid = json_obj.get("cid")
    set_attribute_if_not_null(scene, "id", cid)

    json_utterances = json_obj.get("utterances")
    utterances = load_utterances(json_utterances)
    set_attribute_if_not_null(scene, "utterances", utterances)

    return scene


def load_utterances(json_utterances: List[dict]):
    return [load_utterance(json_utterance) for json_utterance in json_utterances]


def load_utterance(json_obj: dict):
    utterance = Utterance()

    uid = json_obj.get("uid")
    set_attribute_if_not_null(utterance, "id", uid)

    speakers = json_obj.get("speakers")
    set_attribute_if_not_null(utterance, "speakers", speakers)

    transcript = json_obj.get("transcript")
    set_attribute_if_not_null(utterance, "transcript", transcript)

    json_tokens = json_obj.get("tokens")
    tokens = load_tokens(json_tokens)
    set_attribute_if_not_null(utterance, "sentences", tokens)

    transcript_with_note = json_obj.get("transcript_with_note")
    set_attribute_if_not_null(utterance, "transcript_with_note", transcript_with_note)

    tokens_with_note = json_obj.get("tokens_with_note")
    set_attribute_if_not_null(utterance, "tokens_with_note", tokens_with_note)

    json_character_entities = json_obj.get("character_entities")
    character_entities = load_character_entities(json_character_entities)
    set_attribute_if_not_null(utterance, "character_entities", character_entities)

    return utterance


def load_tokens(json_tokens: List[List[str]]):
    return [
        [Token(tid, word) for tid, word in enumerate(sentence_json_tokens)]
        for sentence_json_tokens in json_tokens
    ]


def load_character_entities(json_character_entities: List[List[dict]]):
    return [
        [load_character_entity(json_character_entity) for json_character_entity in sentence_json_character_entities]
        for sentence_json_character_entities in json_character_entities
    ]


def load_character_entity(json_obj: dict):
    character_entity = CharacterEntity()

    start = json_obj.get("start")
    set_attribute_if_not_null(character_entity, "start", start)

    end = json_obj.get("end")
    set_attribute_if_not_null(character_entity, "end", end)

    entity = json_obj.get("entity")
    set_attribute_if_not_null(character_entity, "entity", entity)

    return character_entity


def set_attribute_if_not_null(obj: object, attr: str, value: Any):
    if value:
        setattr(obj, attr, value)


if __name__ == "__main__":
    friends_seasons = load()
