# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vmware script-execution list",
)
class List(AAZCommand):
    """List script executions in a private cloud

    :example: List script executions.
        az vmware script-execution list --resource-group group1 --private-cloud cloud1
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}/scriptexecutions", "2024-09-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.private_cloud = AAZStrArg(
            options=["-c", "--private-cloud"],
            help="Name of the private cloud",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[-\\w\\._]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ScriptExecutionsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ScriptExecutionsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/scriptExecutions",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.errors = AAZListType(
                flags={"read_only": True},
            )
            properties.failure_reason = AAZStrType(
                serialized_name="failureReason",
            )
            properties.finished_at = AAZStrType(
                serialized_name="finishedAt",
                flags={"read_only": True},
            )
            properties.hidden_parameters = AAZListType(
                serialized_name="hiddenParameters",
            )
            properties.information = AAZListType(
                flags={"read_only": True},
            )
            properties.named_outputs = AAZDictType(
                serialized_name="namedOutputs",
            )
            properties.output = AAZListType()
            properties.parameters = AAZListType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.retention = AAZStrType()
            properties.script_cmdlet_id = AAZStrType(
                serialized_name="scriptCmdletId",
            )
            properties.started_at = AAZStrType(
                serialized_name="startedAt",
                flags={"read_only": True},
            )
            properties.submitted_at = AAZStrType(
                serialized_name="submittedAt",
                flags={"read_only": True},
            )
            properties.timeout = AAZStrType(
                flags={"required": True},
            )
            properties.warnings = AAZListType(
                flags={"read_only": True},
            )

            errors = cls._schema_on_200.value.Element.properties.errors
            errors.Element = AAZStrType()

            hidden_parameters = cls._schema_on_200.value.Element.properties.hidden_parameters
            hidden_parameters.Element = AAZObjectType()
            _ListHelper._build_schema_script_execution_parameter_read(hidden_parameters.Element)

            information = cls._schema_on_200.value.Element.properties.information
            information.Element = AAZStrType()

            named_outputs = cls._schema_on_200.value.Element.properties.named_outputs
            named_outputs.Element = AAZDictType()

            _element = cls._schema_on_200.value.Element.properties.named_outputs.Element
            _element.Element = AAZAnyType()

            output = cls._schema_on_200.value.Element.properties.output
            output.Element = AAZStrType()

            parameters = cls._schema_on_200.value.Element.properties.parameters
            parameters.Element = AAZObjectType()
            _ListHelper._build_schema_script_execution_parameter_read(parameters.Element)

            warnings = cls._schema_on_200.value.Element.properties.warnings
            warnings.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_script_execution_parameter_read = None

    @classmethod
    def _build_schema_script_execution_parameter_read(cls, _schema):
        if cls._schema_script_execution_parameter_read is not None:
            _schema.name = cls._schema_script_execution_parameter_read.name
            _schema.type = cls._schema_script_execution_parameter_read.type
            _schema.discriminate_by(
                "type",
                "Credential",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "Credential",
                )
            )
            _schema.discriminate_by(
                "type",
                "SecureValue",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "SecureValue",
                )
            )
            _schema.discriminate_by(
                "type",
                "Value",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "Value",
                )
            )
            return

        cls._schema_script_execution_parameter_read = _schema_script_execution_parameter_read = AAZObjectType()

        script_execution_parameter_read = _schema_script_execution_parameter_read
        script_execution_parameter_read.name = AAZStrType(
            flags={"required": True},
        )
        script_execution_parameter_read.type = AAZStrType(
            flags={"required": True},
        )

        disc_credential = _schema_script_execution_parameter_read.discriminate_by("type", "Credential")
        disc_credential.password = AAZStrType(
            flags={"secret": True},
        )
        disc_credential.username = AAZStrType()

        disc_secure_value = _schema_script_execution_parameter_read.discriminate_by("type", "SecureValue")
        disc_secure_value.secure_value = AAZStrType(
            serialized_name="secureValue",
            flags={"secret": True},
        )

        disc_value = _schema_script_execution_parameter_read.discriminate_by("type", "Value")
        disc_value.value = AAZStrType()

        _schema.name = cls._schema_script_execution_parameter_read.name
        _schema.type = cls._schema_script_execution_parameter_read.type
        _schema.discriminate_by(
                "type",
                "Credential",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "Credential",
                )
            )
        _schema.discriminate_by(
                "type",
                "SecureValue",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "SecureValue",
                )
            )
        _schema.discriminate_by(
                "type",
                "Value",
                cls._schema_script_execution_parameter_read.discriminate_by(
                    "type",
                    "Value",
                )
            )


__all__ = ["List"]
