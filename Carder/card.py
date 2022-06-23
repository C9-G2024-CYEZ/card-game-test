import enum
import pygame
import json


class Element(enum.Enum):
    wind = 0
    lumi = 1
    dark = 2  # light
    fire = 3
    aqua = 4  # water


class Card(object):
    def __init__(self, name, element, level, attack, defense, description, image_path, skill1, skill2, spirit, spirit_rate):
        self.name = name
        self.element = element
        self.level = level
        self.attack = attack
        self.defense = defense
        self.description = description
        self.image_path = image_path
        self.skill1 = skill1
        self.skill2 = skill2
        self.spirit = spirit
        self.spirit_rate = spirit_rate
        self.image=pygame.image.load(image_path)
    def toJSON(self):
        return json.dumps(self.__dict__(), indent=4, ensure_ascii=False)

    @classmethod
    def fromJSON(cls, json_data):
        return json.loads(json_data, object_hook=lambda d: cls(**d))

    def __dict__(self):
        return {
            'name': self.name,
            'element': str(self.element),
            'level': self.level,
            'attack': self.attack,
            'defense': self.defense,
            'description': self.description,
            'image_path': self.image_path,
            'skill1': self.skill1,
            'skill2': self.skill2,
            'spirit': self.spirit,
            'spirit_rate': self.spirit_rate
        }

    def __str__(self):
        return "CARD: {0}".format(self.name)
