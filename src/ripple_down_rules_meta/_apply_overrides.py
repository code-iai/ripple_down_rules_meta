import ripple_down_rules
from . import overrides

# Apply all registered overrides
for name, obj in overrides._overrides:
    setattr(getattr(ripple_down_rules, name), '_overridden_by', obj)
    setattr(ripple_down_rules, name, obj)
