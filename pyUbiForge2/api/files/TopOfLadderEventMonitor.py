from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class TopOfLadderEventMonitor(SubclassBaseFile):
    ResourceType = 0x5CC0F941
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

