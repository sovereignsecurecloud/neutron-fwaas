# Copyright 2016 <PUT YOUR NAME/COMPANY HERE>
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
#

"""rename tenant to project

Revision ID: f83a0b2964d0
Revises: 458aa42b14b
Create Date: 2016-07-14 13:11:53.112622

"""

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'f83a0b2964d0'
down_revision = '458aa42b14b'

# milestone identifier, used by neutron-db-manage
neutron_milestone = [migration.NEWTON]


# NOTE(ralonsoh): this migration operated on the FWaaS v1 tables that are no
# longer created. The v1 tables were removed from the Neutron initial migration
# and dropped by the 2025.1 contract migration 1007f519ea46. This script is
# kept as a no-op because it is a milestone marker in the contract branch.
def upgrade():
    pass
