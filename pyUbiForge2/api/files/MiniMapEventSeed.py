from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class MiniMapEventSeed(SubclassBaseFile):
    ResourceType = 0x24D5DB07
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed

