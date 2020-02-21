#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings

from .avro_consumer import AvroConsumer
from .avro_producer import AvroProducer
from .cached_schema_registry_client import CachedSchemaRegistryClient
from .error import ClientError
from .load import load, loads

__all__ = ['AvroConsumer', 'AvroProducer',
           'load', 'loads',
           'ClientError', 'CachedSchemaRegistryClient']

# TODO: Add reference to avro example
warnings.warn(
    "Package confluent_kafka.avro has been deprecated."
    "This package will be removed in a future version",
    category=DeprecationWarning, stacklevel=2)
