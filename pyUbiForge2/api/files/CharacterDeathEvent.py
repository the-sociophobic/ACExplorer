from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CharacterDeathEvent(SubclassBaseFile):
    ResourceType = 0x976188FA
    ParentResourceType = _Event.ResourceType
    parent: _Event

