from coh.base import (
    Text,
    Category,
    Metric,
    MetricsSet,
    ResultSet,
    ResourcePool,
    DefaultResourcePool,
)

from coh.metrics import *
from coh.tools import *

all_metrics = MetricsSet([BasicCounts(), LogicOperators()])


rp = DefaultResourcePool()


__all__ = sorted([m for m in locals().keys()
                  if not m.startswith('_')])
