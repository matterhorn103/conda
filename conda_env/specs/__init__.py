# -*- coding: utf-8 -*-
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from .binstar import BinstarSpec
from .yaml_file import YamlFileSpec
from .notebook import NotebookSpec
from .requirements import RequirementsSpec
from ..exceptions import SpecNotFound

all_specs = [
    BinstarSpec,
    NotebookSpec,
    YamlFileSpec,
    RequirementsSpec
]


def detect(**kwargs):
    specs = []
    for SpecClass in all_specs:
        spec = SpecClass(**kwargs)
        specs.append(spec)
        if spec.can_handle():
            return spec

    raise SpecNotFound(build_message(specs))


def build_message(specs):
    binstar_spec = next((spec for spec in specs if isinstance(spec, BinstarSpec)), None)
    if binstar_spec:
        return binstar_spec.msg
    else:
        return "\n".join([s.msg for s in specs if s.msg is not None])
