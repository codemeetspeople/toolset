"""Toolset logs package constants."""

from dataclasses import dataclass

from toolset.core.constants import ConstantDataclass


@dataclass(frozen=True)
class LogSeverity(ConstantDataclass):
    """Class-wrapper for logs severity constants."""

    DEBUG: str = 'debug'
    INFO: str = 'info'
    WARNING: str = 'warning'
    ERROR: str = 'error'
    CRITICAL: str = 'critical'
