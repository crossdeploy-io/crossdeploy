'''
# `ibmcpd_monitor_instance`

Refer to the Terraform Registory for docs: [`ibmcpd_monitor_instance`](https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import crossdeploy.cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class MonitorInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance ibmcpd_monitor_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_mart_id: builtins.str,
        monitor_definition_id: builtins.str,
        subscription_id: builtins.str,
        drift_archive_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[typing.Union["MonitorInstanceParameters", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
        thresholds: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorInstanceThresholds", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance ibmcpd_monitor_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_mart_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#data_mart_id MonitorInstance#data_mart_id}.
        :param monitor_definition_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#monitor_definition_id MonitorInstance#monitor_definition_id}.
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#subscription_id MonitorInstance#subscription_id}.
        :param drift_archive_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#drift_archive_path MonitorInstance#drift_archive_path}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#parameters MonitorInstance#parameters}.
        :param thresholds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#thresholds MonitorInstance#thresholds}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6bf9d9962dff6d0af5dbcf58db0ecc514fb1fd6443b0d75eb437be9ecebc14f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MonitorInstanceConfig(
            data_mart_id=data_mart_id,
            monitor_definition_id=monitor_definition_id,
            subscription_id=subscription_id,
            drift_archive_path=drift_archive_path,
            parameters=parameters,
            thresholds=thresholds,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[typing.Union["MonitorInstanceParameters", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cbe6f7502e5ea21821d7239aa945e28837c7ea4bee1be65c236bd464783fbb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="putThresholds")
    def put_thresholds(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorInstanceThresholds", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fea65253cedf95da915fb413a58559f1d960a60eedfbcf17f22928062822e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThresholds", [value]))

    @jsii.member(jsii_name="resetDriftArchivePath")
    def reset_drift_archive_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriftArchivePath", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetThresholds")
    def reset_thresholds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "MonitorInstanceParametersOutputReference":
        return typing.cast("MonitorInstanceParametersOutputReference", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="thresholds")
    def thresholds(self) -> "MonitorInstanceThresholdsList":
        return typing.cast("MonitorInstanceThresholdsList", jsii.get(self, "thresholds"))

    @builtins.property
    @jsii.member(jsii_name="dataMartIdInput")
    def data_mart_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataMartIdInput"))

    @builtins.property
    @jsii.member(jsii_name="driftArchivePathInput")
    def drift_archive_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driftArchivePathInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorDefinitionIdInput")
    def monitor_definition_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorDefinitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorInstanceParameters", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorInstanceParameters", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdsInput")
    def thresholds_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceThresholds"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceThresholds"]]], jsii.get(self, "thresholdsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMartId")
    def data_mart_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataMartId"))

    @data_mart_id.setter
    def data_mart_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358cb3fd877ac70aceea55e892d312c6c77e6f0ddf815dda24934daffd91a30b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataMartId", value)

    @builtins.property
    @jsii.member(jsii_name="driftArchivePath")
    def drift_archive_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driftArchivePath"))

    @drift_archive_path.setter
    def drift_archive_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a827d1ef6cf84feae7ba3b0a3bb5c751cfff4a9b4f038f2cb00434bf4ce53eef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driftArchivePath", value)

    @builtins.property
    @jsii.member(jsii_name="monitorDefinitionId")
    def monitor_definition_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitorDefinitionId"))

    @monitor_definition_id.setter
    def monitor_definition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dad3b8a5882958e19789d699b22d95d7e66badf520bd933db3b7332196616d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorDefinitionId", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d0fd1a12bd547b0667459413b98f343180c917d3c94bea425ba44dec8b26c47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)


@jsii.data_type(
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_mart_id": "dataMartId",
        "monitor_definition_id": "monitorDefinitionId",
        "subscription_id": "subscriptionId",
        "drift_archive_path": "driftArchivePath",
        "parameters": "parameters",
        "thresholds": "thresholds",
    },
)
class MonitorInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        data_mart_id: builtins.str,
        monitor_definition_id: builtins.str,
        subscription_id: builtins.str,
        drift_archive_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[typing.Union["MonitorInstanceParameters", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
        thresholds: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorInstanceThresholds", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_mart_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#data_mart_id MonitorInstance#data_mart_id}.
        :param monitor_definition_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#monitor_definition_id MonitorInstance#monitor_definition_id}.
        :param subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#subscription_id MonitorInstance#subscription_id}.
        :param drift_archive_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#drift_archive_path MonitorInstance#drift_archive_path}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#parameters MonitorInstance#parameters}.
        :param thresholds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#thresholds MonitorInstance#thresholds}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2083408f71df58e9ae18117b76f8088c43655b318b79d5e90438117d20736dd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_mart_id", value=data_mart_id, expected_type=type_hints["data_mart_id"])
            check_type(argname="argument monitor_definition_id", value=monitor_definition_id, expected_type=type_hints["monitor_definition_id"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument drift_archive_path", value=drift_archive_path, expected_type=type_hints["drift_archive_path"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument thresholds", value=thresholds, expected_type=type_hints["thresholds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_mart_id": data_mart_id,
            "monitor_definition_id": monitor_definition_id,
            "subscription_id": subscription_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if drift_archive_path is not None:
            self._values["drift_archive_path"] = drift_archive_path
        if parameters is not None:
            self._values["parameters"] = parameters
        if thresholds is not None:
            self._values["thresholds"] = thresholds

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def data_mart_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#data_mart_id MonitorInstance#data_mart_id}.'''
        result = self._values.get("data_mart_id")
        assert result is not None, "Required property 'data_mart_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitor_definition_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#monitor_definition_id MonitorInstance#monitor_definition_id}.'''
        result = self._values.get("monitor_definition_id")
        assert result is not None, "Required property 'monitor_definition_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#subscription_id MonitorInstance#subscription_id}.'''
        result = self._values.get("subscription_id")
        assert result is not None, "Required property 'subscription_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def drift_archive_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#drift_archive_path MonitorInstance#drift_archive_path}.'''
        result = self._values.get("drift_archive_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union["MonitorInstanceParameters", _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#parameters MonitorInstance#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union["MonitorInstanceParameters", _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def thresholds(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceThresholds"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#thresholds MonitorInstance#thresholds}.'''
        result = self._values.get("thresholds")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceThresholds"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceParameters",
    jsii_struct_bases=[],
    name_mapping={
        "drift_threshold": "driftThreshold",
        "enabled": "enabled",
        "enable_data_drift": "enableDataDrift",
        "enable_model_drift": "enableModelDrift",
        "favourable_class": "favourableClass",
        "features": "features",
        "min_feedback_data_size": "minFeedbackDataSize",
        "min_records": "minRecords",
        "min_samples": "minSamples",
        "train_drift_model": "trainDriftModel",
        "unfavourable_class": "unfavourableClass",
    },
)
class MonitorInstanceParameters:
    def __init__(
        self,
        *,
        drift_threshold: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_data_drift: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_model_drift: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        favourable_class: typing.Optional[typing.Sequence[builtins.str]] = None,
        features: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MonitorInstanceParametersFeatures", typing.Dict[builtins.str, typing.Any]]]]] = None,
        min_feedback_data_size: typing.Optional[jsii.Number] = None,
        min_records: typing.Optional[jsii.Number] = None,
        min_samples: typing.Optional[jsii.Number] = None,
        train_drift_model: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        unfavourable_class: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param drift_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#drift_threshold MonitorInstance#drift_threshold}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enabled MonitorInstance#enabled}.
        :param enable_data_drift: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enable_data_drift MonitorInstance#enable_data_drift}.
        :param enable_model_drift: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enable_model_drift MonitorInstance#enable_model_drift}.
        :param favourable_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#favourable_class MonitorInstance#favourable_class}.
        :param features: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#features MonitorInstance#features}.
        :param min_feedback_data_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_feedback_data_size MonitorInstance#min_feedback_data_size}.
        :param min_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_records MonitorInstance#min_records}.
        :param min_samples: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_samples MonitorInstance#min_samples}.
        :param train_drift_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#train_drift_model MonitorInstance#train_drift_model}.
        :param unfavourable_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#unfavourable_class MonitorInstance#unfavourable_class}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__007c10cf65baf93124cde174397220ae67b1a0bca47f5d9494c3809d64f4f128)
            check_type(argname="argument drift_threshold", value=drift_threshold, expected_type=type_hints["drift_threshold"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_data_drift", value=enable_data_drift, expected_type=type_hints["enable_data_drift"])
            check_type(argname="argument enable_model_drift", value=enable_model_drift, expected_type=type_hints["enable_model_drift"])
            check_type(argname="argument favourable_class", value=favourable_class, expected_type=type_hints["favourable_class"])
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument min_feedback_data_size", value=min_feedback_data_size, expected_type=type_hints["min_feedback_data_size"])
            check_type(argname="argument min_records", value=min_records, expected_type=type_hints["min_records"])
            check_type(argname="argument min_samples", value=min_samples, expected_type=type_hints["min_samples"])
            check_type(argname="argument train_drift_model", value=train_drift_model, expected_type=type_hints["train_drift_model"])
            check_type(argname="argument unfavourable_class", value=unfavourable_class, expected_type=type_hints["unfavourable_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if drift_threshold is not None:
            self._values["drift_threshold"] = drift_threshold
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_data_drift is not None:
            self._values["enable_data_drift"] = enable_data_drift
        if enable_model_drift is not None:
            self._values["enable_model_drift"] = enable_model_drift
        if favourable_class is not None:
            self._values["favourable_class"] = favourable_class
        if features is not None:
            self._values["features"] = features
        if min_feedback_data_size is not None:
            self._values["min_feedback_data_size"] = min_feedback_data_size
        if min_records is not None:
            self._values["min_records"] = min_records
        if min_samples is not None:
            self._values["min_samples"] = min_samples
        if train_drift_model is not None:
            self._values["train_drift_model"] = train_drift_model
        if unfavourable_class is not None:
            self._values["unfavourable_class"] = unfavourable_class

    @builtins.property
    def drift_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#drift_threshold MonitorInstance#drift_threshold}.'''
        result = self._values.get("drift_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enabled MonitorInstance#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_data_drift(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enable_data_drift MonitorInstance#enable_data_drift}.'''
        result = self._values.get("enable_data_drift")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_model_drift(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#enable_model_drift MonitorInstance#enable_model_drift}.'''
        result = self._values.get("enable_model_drift")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def favourable_class(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#favourable_class MonitorInstance#favourable_class}.'''
        result = self._values.get("favourable_class")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def features(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceParametersFeatures"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#features MonitorInstance#features}.'''
        result = self._values.get("features")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MonitorInstanceParametersFeatures"]]], result)

    @builtins.property
    def min_feedback_data_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_feedback_data_size MonitorInstance#min_feedback_data_size}.'''
        result = self._values.get("min_feedback_data_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_records(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_records MonitorInstance#min_records}.'''
        result = self._values.get("min_records")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_samples(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#min_samples MonitorInstance#min_samples}.'''
        result = self._values.get("min_samples")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def train_drift_model(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#train_drift_model MonitorInstance#train_drift_model}.'''
        result = self._values.get("train_drift_model")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def unfavourable_class(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#unfavourable_class MonitorInstance#unfavourable_class}.'''
        result = self._values.get("unfavourable_class")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorInstanceParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceParametersFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "feature": "feature",
        "majority": "majority",
        "minority": "minority",
        "threshold": "threshold",
    },
)
class MonitorInstanceParametersFeatures:
    def __init__(
        self,
        *,
        feature: typing.Optional[builtins.str] = None,
        majority: typing.Optional[typing.Sequence[builtins.str]] = None,
        minority: typing.Optional[typing.Sequence[builtins.str]] = None,
        threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param feature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#feature MonitorInstance#feature}.
        :param majority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#majority MonitorInstance#majority}.
        :param minority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#minority MonitorInstance#minority}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#threshold MonitorInstance#threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c367738179f4a06bf4cdaef2a66ffc0666771ef78b1a0c6d517cc4cc71ecf637)
            check_type(argname="argument feature", value=feature, expected_type=type_hints["feature"])
            check_type(argname="argument majority", value=majority, expected_type=type_hints["majority"])
            check_type(argname="argument minority", value=minority, expected_type=type_hints["minority"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if feature is not None:
            self._values["feature"] = feature
        if majority is not None:
            self._values["majority"] = majority
        if minority is not None:
            self._values["minority"] = minority
        if threshold is not None:
            self._values["threshold"] = threshold

    @builtins.property
    def feature(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#feature MonitorInstance#feature}.'''
        result = self._values.get("feature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def majority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#majority MonitorInstance#majority}.'''
        result = self._values.get("majority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def minority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#minority MonitorInstance#minority}.'''
        result = self._values.get("minority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#threshold MonitorInstance#threshold}.'''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorInstanceParametersFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorInstanceParametersFeaturesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceParametersFeaturesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c8e0da6372818634b75a7b8d689c9e6588a04ebf3a65da4a271e986844fbd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorInstanceParametersFeaturesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde811fe749194a811b27949340385b8094595eda1972e71237aab57dd6302b4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorInstanceParametersFeaturesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__554601b8ac7caa9925a2e94027edf121c8db86c6dbd55285d5ae09078eea1d49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1573a7a145cb9fac4542c3833a52cd079ad7e6c9eb735645e31ccdccf5323317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69721cf2f8044528ba800adea36d8c3645422e0054e63df407019623a4269cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24b95a2b634a070a5a7b8ef78d882ff5451fac5c97a8df4e6bc915b1d40908b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorInstanceParametersFeaturesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceParametersFeaturesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50cdda9e018e358a81bd4977c0c8aa0c265e73b7febfa8ef434cb1a9ce7a6522)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFeature")
    def reset_feature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeature", []))

    @jsii.member(jsii_name="resetMajority")
    def reset_majority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMajority", []))

    @jsii.member(jsii_name="resetMinority")
    def reset_minority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinority", []))

    @jsii.member(jsii_name="resetThreshold")
    def reset_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="featureInput")
    def feature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureInput"))

    @builtins.property
    @jsii.member(jsii_name="majorityInput")
    def majority_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "majorityInput"))

    @builtins.property
    @jsii.member(jsii_name="minorityInput")
    def minority_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "minorityInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="feature")
    def feature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "feature"))

    @feature.setter
    def feature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cae7a052ade30eae866aae5a5c62e5f6e3e374ea1d7db67adf7046674a76c9b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feature", value)

    @builtins.property
    @jsii.member(jsii_name="majority")
    def majority(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "majority"))

    @majority.setter
    def majority(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b8fda1fbf0707af5026d122f29295b215b629cfedcd6cd95a2f289cb66381a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "majority", value)

    @builtins.property
    @jsii.member(jsii_name="minority")
    def minority(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "minority"))

    @minority.setter
    def minority(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__281cc67c09fe5f5fc318a365c4cd15687b3182ad453b992517b16aa9a72155ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minority", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e4b3fc802d66d71d033a21f554377eb0fecaa145f6851b372bd838883f06b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorInstanceParametersFeatures, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorInstanceParametersFeatures, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorInstanceParametersFeatures, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50b1a53c4b9178bf93ab314a6f1ff1a0358ce5f8b6def0e2dd67e724d9412b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorInstanceParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceParametersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4673ebefe89902d53b9db404cbd7bfeb67c64c84980a3a6bbdb7f8f9e99325)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFeatures")
    def put_features(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceParametersFeatures, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1a930ca6007e3c99fd0de19c73763865a5d96321d5b2305e8fc009379ac58d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFeatures", [value]))

    @jsii.member(jsii_name="resetDriftThreshold")
    def reset_drift_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriftThreshold", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEnableDataDrift")
    def reset_enable_data_drift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDataDrift", []))

    @jsii.member(jsii_name="resetEnableModelDrift")
    def reset_enable_model_drift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableModelDrift", []))

    @jsii.member(jsii_name="resetFavourableClass")
    def reset_favourable_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFavourableClass", []))

    @jsii.member(jsii_name="resetFeatures")
    def reset_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatures", []))

    @jsii.member(jsii_name="resetMinFeedbackDataSize")
    def reset_min_feedback_data_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinFeedbackDataSize", []))

    @jsii.member(jsii_name="resetMinRecords")
    def reset_min_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinRecords", []))

    @jsii.member(jsii_name="resetMinSamples")
    def reset_min_samples(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSamples", []))

    @jsii.member(jsii_name="resetTrainDriftModel")
    def reset_train_drift_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrainDriftModel", []))

    @jsii.member(jsii_name="resetUnfavourableClass")
    def reset_unfavourable_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnfavourableClass", []))

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(self) -> MonitorInstanceParametersFeaturesList:
        return typing.cast(MonitorInstanceParametersFeaturesList, jsii.get(self, "features"))

    @builtins.property
    @jsii.member(jsii_name="driftThresholdInput")
    def drift_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "driftThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDataDriftInput")
    def enable_data_drift_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDataDriftInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableModelDriftInput")
    def enable_model_drift_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableModelDriftInput"))

    @builtins.property
    @jsii.member(jsii_name="favourableClassInput")
    def favourable_class_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "favourableClassInput"))

    @builtins.property
    @jsii.member(jsii_name="featuresInput")
    def features_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]], jsii.get(self, "featuresInput"))

    @builtins.property
    @jsii.member(jsii_name="minFeedbackDataSizeInput")
    def min_feedback_data_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minFeedbackDataSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minRecordsInput")
    def min_records_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="minSamplesInput")
    def min_samples_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSamplesInput"))

    @builtins.property
    @jsii.member(jsii_name="trainDriftModelInput")
    def train_drift_model_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "trainDriftModelInput"))

    @builtins.property
    @jsii.member(jsii_name="unfavourableClassInput")
    def unfavourable_class_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "unfavourableClassInput"))

    @builtins.property
    @jsii.member(jsii_name="driftThreshold")
    def drift_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "driftThreshold"))

    @drift_threshold.setter
    def drift_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfef26c068f3d176eccc24f944b128e51eb00d968d63cd9d620c1817ab20ec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driftThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf96ca02dfe54ccaba58fe596f06b6c4cfb56f14a95baf6db6881f113e1fef7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableDataDrift")
    def enable_data_drift(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDataDrift"))

    @enable_data_drift.setter
    def enable_data_drift(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcdb49b73aa50e493959cee036c967a246403c008f61450f612a4835d9b5b7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDataDrift", value)

    @builtins.property
    @jsii.member(jsii_name="enableModelDrift")
    def enable_model_drift(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableModelDrift"))

    @enable_model_drift.setter
    def enable_model_drift(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc11507344a24c80ac6d1d416d2d91870476bd68aadfe2e30c24e7a01c92992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableModelDrift", value)

    @builtins.property
    @jsii.member(jsii_name="favourableClass")
    def favourable_class(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "favourableClass"))

    @favourable_class.setter
    def favourable_class(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b87228e3c029ca039045a691b8c580eb14fdd3db6247b8f64d575cb79381815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "favourableClass", value)

    @builtins.property
    @jsii.member(jsii_name="minFeedbackDataSize")
    def min_feedback_data_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minFeedbackDataSize"))

    @min_feedback_data_size.setter
    def min_feedback_data_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11398f4e7dc604647971deee03ee71651af31d07560fc145410f3414746a9fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minFeedbackDataSize", value)

    @builtins.property
    @jsii.member(jsii_name="minRecords")
    def min_records(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minRecords"))

    @min_records.setter
    def min_records(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899ba2fb50625ba75a9d6431a640d8a944cd29be0cb1eec55dbb17f7694f358f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minRecords", value)

    @builtins.property
    @jsii.member(jsii_name="minSamples")
    def min_samples(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSamples"))

    @min_samples.setter
    def min_samples(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c796f3829a77498e71fa112da6c726344b650d227ccf9677eb24f27c6340f977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSamples", value)

    @builtins.property
    @jsii.member(jsii_name="trainDriftModel")
    def train_drift_model(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "trainDriftModel"))

    @train_drift_model.setter
    def train_drift_model(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e8f55c19e81a36c8d8df7f3d34f1a57cb75f4c91bd0a26004e4cff4b48cb6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trainDriftModel", value)

    @builtins.property
    @jsii.member(jsii_name="unfavourableClass")
    def unfavourable_class(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "unfavourableClass"))

    @unfavourable_class.setter
    def unfavourable_class(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d39a6b3505fa2748d4e5fe5a5e0823887aedf41c45b353dc070c6bed5fdf812)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unfavourableClass", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorInstanceParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorInstanceParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorInstanceParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952055b3daff51b810ee3ff218646bddc53de4aaa217f29a8d11c52c3270dc9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceThresholds",
    jsii_struct_bases=[],
    name_mapping={"metric_id": "metricId", "type": "type", "value": "value"},
)
class MonitorInstanceThresholds:
    def __init__(
        self,
        *,
        metric_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metric_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#metric_id MonitorInstance#metric_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#type MonitorInstance#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#value MonitorInstance#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd28c683f97949ab2f715cf88095b15d969983b9457c2fa916fd1edd51590dd)
            check_type(argname="argument metric_id", value=metric_id, expected_type=type_hints["metric_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metric_id is not None:
            self._values["metric_id"] = metric_id
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def metric_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#metric_id MonitorInstance#metric_id}.'''
        result = self._values.get("metric_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#type MonitorInstance#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/monitor_instance#value MonitorInstance#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorInstanceThresholds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorInstanceThresholdsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceThresholdsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99391dc9eb3d082372ba7955886af79fe1601061df91f411636fd7941ba75a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorInstanceThresholdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366b026f9cb87155e7483f69bd9311ab168422e05aa30079c408f543e9032f9a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorInstanceThresholdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fcd52f84dfe8e744033cccd28700b42e3a80170a252c8df5c334e56c9220e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ebf1da5702205fcddcf7cb345c5b1f04a5ee3fe3c7cd41d5eb41a369d7d3ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3860bf3f5c2361c5d0e9c8f7120b4720b318f323569eabb17957ebb64db25b9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceThresholds]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceThresholds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceThresholds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6160372c0ad1f2007524adb65a844e25ec809ac2fa327d9d1ac5998eeef53a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorInstanceThresholdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.monitorInstance.MonitorInstanceThresholdsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0827952bb09db1715b207c6ad11bc65df8ea28965d3b003aaaf57ebd5cb23aeb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMetricId")
    def reset_metric_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricId", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="metricIdInput")
    def metric_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="metricId")
    def metric_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricId"))

    @metric_id.setter
    def metric_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee1dc4829df5b268689c53081092cf9307dcfcb4805a9388f17b4cb97ffe7600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f771d28433c9f299a0eb7a83332999ef8d3f5d2c9d80348d59dbd2b38d2fa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b7d695865d59aaf47bf13c675b38d7ca7e09497b8a73963771e19cec054d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorInstanceThresholds, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorInstanceThresholds, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorInstanceThresholds, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b046558cb727cc5d9a4f4e65c19b3436c5f1b83c90bb867a62f6f9edc012814f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorInstance",
    "MonitorInstanceConfig",
    "MonitorInstanceParameters",
    "MonitorInstanceParametersFeatures",
    "MonitorInstanceParametersFeaturesList",
    "MonitorInstanceParametersFeaturesOutputReference",
    "MonitorInstanceParametersOutputReference",
    "MonitorInstanceThresholds",
    "MonitorInstanceThresholdsList",
    "MonitorInstanceThresholdsOutputReference",
]

publication.publish()

def _typecheckingstub__c6bf9d9962dff6d0af5dbcf58db0ecc514fb1fd6443b0d75eb437be9ecebc14f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_mart_id: builtins.str,
    monitor_definition_id: builtins.str,
    subscription_id: builtins.str,
    drift_archive_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[typing.Union[MonitorInstanceParameters, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
    thresholds: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceThresholds, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cbe6f7502e5ea21821d7239aa945e28837c7ea4bee1be65c236bd464783fbb5(
    value: typing.Union[typing.Union[MonitorInstanceParameters, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fea65253cedf95da915fb413a58559f1d960a60eedfbcf17f22928062822e89(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceThresholds, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358cb3fd877ac70aceea55e892d312c6c77e6f0ddf815dda24934daffd91a30b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a827d1ef6cf84feae7ba3b0a3bb5c751cfff4a9b4f038f2cb00434bf4ce53eef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dad3b8a5882958e19789d699b22d95d7e66badf520bd933db3b7332196616d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d0fd1a12bd547b0667459413b98f343180c917d3c94bea425ba44dec8b26c47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2083408f71df58e9ae18117b76f8088c43655b318b79d5e90438117d20736dd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_mart_id: builtins.str,
    monitor_definition_id: builtins.str,
    subscription_id: builtins.str,
    drift_archive_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[typing.Union[MonitorInstanceParameters, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
    thresholds: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceThresholds, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007c10cf65baf93124cde174397220ae67b1a0bca47f5d9494c3809d64f4f128(
    *,
    drift_threshold: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_data_drift: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_model_drift: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    favourable_class: typing.Optional[typing.Sequence[builtins.str]] = None,
    features: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceParametersFeatures, typing.Dict[builtins.str, typing.Any]]]]] = None,
    min_feedback_data_size: typing.Optional[jsii.Number] = None,
    min_records: typing.Optional[jsii.Number] = None,
    min_samples: typing.Optional[jsii.Number] = None,
    train_drift_model: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    unfavourable_class: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c367738179f4a06bf4cdaef2a66ffc0666771ef78b1a0c6d517cc4cc71ecf637(
    *,
    feature: typing.Optional[builtins.str] = None,
    majority: typing.Optional[typing.Sequence[builtins.str]] = None,
    minority: typing.Optional[typing.Sequence[builtins.str]] = None,
    threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c8e0da6372818634b75a7b8d689c9e6588a04ebf3a65da4a271e986844fbd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde811fe749194a811b27949340385b8094595eda1972e71237aab57dd6302b4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554601b8ac7caa9925a2e94027edf121c8db86c6dbd55285d5ae09078eea1d49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1573a7a145cb9fac4542c3833a52cd079ad7e6c9eb735645e31ccdccf5323317(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69721cf2f8044528ba800adea36d8c3645422e0054e63df407019623a4269cd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b95a2b634a070a5a7b8ef78d882ff5451fac5c97a8df4e6bc915b1d40908b0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceParametersFeatures]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cdda9e018e358a81bd4977c0c8aa0c265e73b7febfa8ef434cb1a9ce7a6522(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cae7a052ade30eae866aae5a5c62e5f6e3e374ea1d7db67adf7046674a76c9b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b8fda1fbf0707af5026d122f29295b215b629cfedcd6cd95a2f289cb66381a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281cc67c09fe5f5fc318a365c4cd15687b3182ad453b992517b16aa9a72155ff(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e4b3fc802d66d71d033a21f554377eb0fecaa145f6851b372bd838883f06b7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b1a53c4b9178bf93ab314a6f1ff1a0358ce5f8b6def0e2dd67e724d9412b7a(
    value: typing.Optional[typing.Union[MonitorInstanceParametersFeatures, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4673ebefe89902d53b9db404cbd7bfeb67c64c84980a3a6bbdb7f8f9e99325(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1a930ca6007e3c99fd0de19c73763865a5d96321d5b2305e8fc009379ac58d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MonitorInstanceParametersFeatures, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfef26c068f3d176eccc24f944b128e51eb00d968d63cd9d620c1817ab20ec8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf96ca02dfe54ccaba58fe596f06b6c4cfb56f14a95baf6db6881f113e1fef7d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdb49b73aa50e493959cee036c967a246403c008f61450f612a4835d9b5b7f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc11507344a24c80ac6d1d416d2d91870476bd68aadfe2e30c24e7a01c92992(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b87228e3c029ca039045a691b8c580eb14fdd3db6247b8f64d575cb79381815(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11398f4e7dc604647971deee03ee71651af31d07560fc145410f3414746a9fb8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899ba2fb50625ba75a9d6431a640d8a944cd29be0cb1eec55dbb17f7694f358f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c796f3829a77498e71fa112da6c726344b650d227ccf9677eb24f27c6340f977(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e8f55c19e81a36c8d8df7f3d34f1a57cb75f4c91bd0a26004e4cff4b48cb6b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d39a6b3505fa2748d4e5fe5a5e0823887aedf41c45b353dc070c6bed5fdf812(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952055b3daff51b810ee3ff218646bddc53de4aaa217f29a8d11c52c3270dc9e(
    value: typing.Optional[typing.Union[MonitorInstanceParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd28c683f97949ab2f715cf88095b15d969983b9457c2fa916fd1edd51590dd(
    *,
    metric_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99391dc9eb3d082372ba7955886af79fe1601061df91f411636fd7941ba75a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366b026f9cb87155e7483f69bd9311ab168422e05aa30079c408f543e9032f9a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fcd52f84dfe8e744033cccd28700b42e3a80170a252c8df5c334e56c9220e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ebf1da5702205fcddcf7cb345c5b1f04a5ee3fe3c7cd41d5eb41a369d7d3ffd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3860bf3f5c2361c5d0e9c8f7120b4720b318f323569eabb17957ebb64db25b9c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6160372c0ad1f2007524adb65a844e25ec809ac2fa327d9d1ac5998eeef53a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MonitorInstanceThresholds]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0827952bb09db1715b207c6ad11bc65df8ea28965d3b003aaaf57ebd5cb23aeb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee1dc4829df5b268689c53081092cf9307dcfcb4805a9388f17b4cb97ffe7600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f771d28433c9f299a0eb7a83332999ef8d3f5d2c9d80348d59dbd2b38d2fa6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b7d695865d59aaf47bf13c675b38d7ca7e09497b8a73963771e19cec054d9c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b046558cb727cc5d9a4f4e65c19b3436c5f1b83c90bb867a62f6f9edc012814f(
    value: typing.Optional[typing.Union[MonitorInstanceThresholds, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
