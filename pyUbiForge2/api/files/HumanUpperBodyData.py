from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanUpperBodyData(SubclassBaseFile):
    ResourceType = 0xFBCDE9D7
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

