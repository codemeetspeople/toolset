"""Toolset common constants utils."""

from __future__ import annotations

from typing import Any
from dataclasses import dataclass, astuple


@dataclass(frozen=True)
class ConstantDataclass:
    """Class-wrapper for constants."""

    @classmethod
    def all(cls: ConstantDataclass) -> tuple[Any, ...]:
        """Return the fields of a ConstantDataclass instance as a new tuple of field values.

        Example usage::

          @dataclass
          class Foo:
              bar: int
              baz: int

        foo = Foo(1, 2)
        assert Foo.all() == (1, 2)
        """
        return astuple(cls())
