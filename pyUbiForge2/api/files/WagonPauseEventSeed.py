from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WagonPauseEventSeed(SubclassBaseFile):
    ResourceType = 0x4914B4A1
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

