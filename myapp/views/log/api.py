# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface

from myapp import app, appbuilder
from myapp.models.log import Log
from . import LogMixin


class LogRestApi(LogMixin, ModelRestApi):
    datamodel = SQLAInterface(Log)

    class_permission_name = "LogModelView"
    method_permission_name = {
        "get_list": "list",
        "get": "show",
        "post": "add",
        "put": "edit",
        "delete": "delete",
        "info": "list",
    }
    resource_name = "log"
    allow_browser_login = True
    list_columns = ("user.username", "action", "dttm")


if (
    not app.config.get("FAB_ADD_SECURITY_VIEWS") is False
    or app.config.get("MYAPP_LOG_VIEW") is False
):
    appbuilder.add_api(LogRestApi)
