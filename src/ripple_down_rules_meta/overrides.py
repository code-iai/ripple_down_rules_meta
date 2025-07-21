from __future__ import annotations

import os
from dataclasses import dataclass
from os.path import dirname
from typing import Type, ClassVar

from ripple_down_rules import (DependsOn as OGDependsOn, RDRDecorator, TrackedObjectMixin,
                               has, isA)

_overrides = []


def override_ripple_down_rules(name):
    def decorator(obj):
        _overrides.append((name, obj))
        return obj

    return decorator


@override_ripple_down_rules("DependsOn")
@dataclass
class DependsOn(OGDependsOn):
    models_dir: ClassVar[str] = os.path.join(dirname(__file__), "predicates_models")
    rdr_decorator: RDRDecorator = RDRDecorator(models_dir, (bool,), True, package_name="ripple_down_rules_meta")
    """
    An rdr decorator used to fit rules for determining the dependencies.
    """
    @classmethod
    @rdr_decorator.decorator
    def evaluate(cls, dependent: Type[TrackedObjectMixin],
                 dependency: Type[TrackedObjectMixin], recursive: bool = False) -> bool:
        pass

dependsOn = DependsOn()
_overrides.append(("dependsOn", dependsOn))
