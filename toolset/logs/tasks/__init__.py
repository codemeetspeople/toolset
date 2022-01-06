"""Toolset logs tasks module."""

from invoke import Collection

from toolset.logs.tasks.merge import merge

ns = Collection('logs', merge)
