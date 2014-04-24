from coh.base import (
    Text,
    Category,
    Metric,
    MetricsSet,
    ResultSet,
)

from coh.resource_pool import (
    ResourcePool,
    DefaultResourcePool,
    rp,
)

from coh.metrics import *
from coh.tools import *

all_metrics = MetricsSet([BasicCounts(), LogicOperators()])


rp = DefaultResourcePool()


__all__ = sorted([m for m in locals().keys()
                  if not m.startswith('_')])
