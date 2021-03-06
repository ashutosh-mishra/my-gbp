# Copyright (c) 2016 Cisco Systems Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron._i18n import _LI
from neutron.tests.unit.plugins.ml2.drivers import (
    mechanism_logger as ml2_logger)
from oslo_log import log

from gbpservice.neutron.plugins.ml2plus import driver_api

LOG = log.getLogger(__name__)


class LoggerPlusMechanismDriver(driver_api.MechanismDriver,
                                ml2_logger.LoggerMechanismDriver):
    """Mechanism driver that logs all calls and parameters made.

    Generally used for testing and debugging.
    """

    def initialize(self):
        LOG.info(_LI("initialize called"))

    def ensure_tenant(self, plugin_context, tenant_id):
        LOG.info(_LI("ensure_tenant called with tenant_id %s"), tenant_id)
