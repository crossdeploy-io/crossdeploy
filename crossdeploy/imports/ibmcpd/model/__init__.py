'''
# `ibmcpd_model`

Refer to the Terraform Registory for docs: [`ibmcpd_model`](https://www.terraform.io/docs/providers/ibmcpd/r/model).
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


class Model(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.model.Model",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ibmcpd/r/model ibmcpd_model}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        model_path: builtins.str,
        name: builtins.str,
        software_spec: builtins.str,
        type: builtins.str,
        asset_id: typing.Optional[builtins.str] = None,
        checksum: typing.Optional[builtins.str] = None,
        input_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelInputSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        label_column: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        space_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ibmcpd/r/model ibmcpd_model} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param model_path: tar.gz file of model from joblib. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#model_path Model#model_path}
        :param name: Name of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#name Model#name}
        :param software_spec: Software spec of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#software_spec Model#software_spec}
        :param type: Type of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#type Model#type}
        :param asset_id: Asset ID of model in project. Used when promoting model in project to deployment space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#asset_id Model#asset_id}
        :param checksum: Checksum of Python object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#checksum Model#checksum}
        :param input_schema: Training input schema of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#input_schema Model#input_schema}
        :param label_column: Label column of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#label_column Model#label_column}
        :param project_id: Project ID of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#project_id Model#project_id}
        :param space_id: Space ID of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#space_id Model#space_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd02fecf578b76356e53c1100510c7bbc47de4626d5a50d9d91974420264376)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ModelConfig(
            model_path=model_path,
            name=name,
            software_spec=software_spec,
            type=type,
            asset_id=asset_id,
            checksum=checksum,
            input_schema=input_schema,
            label_column=label_column,
            project_id=project_id,
            space_id=space_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putInputSchema")
    def put_input_schema(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelInputSchema", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd613daecc771e7bca22bb9ce5f7f781a4c17f4a6436d0cb3072e22416f23f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInputSchema", [value]))

    @jsii.member(jsii_name="resetAssetId")
    def reset_asset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssetId", []))

    @jsii.member(jsii_name="resetChecksum")
    def reset_checksum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChecksum", []))

    @jsii.member(jsii_name="resetInputSchema")
    def reset_input_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputSchema", []))

    @jsii.member(jsii_name="resetLabelColumn")
    def reset_label_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelColumn", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetSpaceId")
    def reset_space_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpaceId", []))

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
    @jsii.member(jsii_name="inputSchema")
    def input_schema(self) -> "ModelInputSchemaList":
        return typing.cast("ModelInputSchemaList", jsii.get(self, "inputSchema"))

    @builtins.property
    @jsii.member(jsii_name="assetIdInput")
    def asset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="checksumInput")
    def checksum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checksumInput"))

    @builtins.property
    @jsii.member(jsii_name="inputSchemaInput")
    def input_schema_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelInputSchema"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelInputSchema"]]], jsii.get(self, "inputSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="labelColumnInput")
    def label_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="modelPathInput")
    def model_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareSpecInput")
    def software_spec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "softwareSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="spaceIdInput")
    def space_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="assetId")
    def asset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assetId"))

    @asset_id.setter
    def asset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4220b7fcfb9cff145d6d12aadd414f5f9f6fbea91b7c293abcc09b4547ccfce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetId", value)

    @builtins.property
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @checksum.setter
    def checksum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad08eda7a65884f6ac1a4546abcfd84ee257a45a246d79705c2f99a0ae5de531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checksum", value)

    @builtins.property
    @jsii.member(jsii_name="labelColumn")
    def label_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelColumn"))

    @label_column.setter
    def label_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10378694c642b28085cad217deebeceff0f3b7dafd5767f7a495542a57a70589)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelColumn", value)

    @builtins.property
    @jsii.member(jsii_name="modelPath")
    def model_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelPath"))

    @model_path.setter
    def model_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785b707e1d1f5d2bb16907249b25b19b2af07f3a73bfb61af9e352f8795b0f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14caa9557078b299225a264c1975c74d30f24e129887db5b87c8ea5afc361835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__616ebc03e193ee05045d63af91599c309887737e40d8a80e637f72f12f454e83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="softwareSpec")
    def software_spec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "softwareSpec"))

    @software_spec.setter
    def software_spec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf4fbb6ec5931d7af0dc2ce4e272254e34060fb57dabfef43fb927aefa04679)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softwareSpec", value)

    @builtins.property
    @jsii.member(jsii_name="spaceId")
    def space_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spaceId"))

    @space_id.setter
    def space_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc9892f80fe7f93508fea2f5368621d1f7795e4d55abe4c1f583747284757128)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spaceId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66bd37345cc1ca6b3a220f39bf4eeb81f6c817619bf7261ea42f3cfc05a940a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="ibmcpd.model.ModelConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "model_path": "modelPath",
        "name": "name",
        "software_spec": "softwareSpec",
        "type": "type",
        "asset_id": "assetId",
        "checksum": "checksum",
        "input_schema": "inputSchema",
        "label_column": "labelColumn",
        "project_id": "projectId",
        "space_id": "spaceId",
    },
)
class ModelConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        model_path: builtins.str,
        name: builtins.str,
        software_spec: builtins.str,
        type: builtins.str,
        asset_id: typing.Optional[builtins.str] = None,
        checksum: typing.Optional[builtins.str] = None,
        input_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelInputSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        label_column: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        space_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param model_path: tar.gz file of model from joblib. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#model_path Model#model_path}
        :param name: Name of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#name Model#name}
        :param software_spec: Software spec of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#software_spec Model#software_spec}
        :param type: Type of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#type Model#type}
        :param asset_id: Asset ID of model in project. Used when promoting model in project to deployment space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#asset_id Model#asset_id}
        :param checksum: Checksum of Python object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#checksum Model#checksum}
        :param input_schema: Training input schema of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#input_schema Model#input_schema}
        :param label_column: Label column of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#label_column Model#label_column}
        :param project_id: Project ID of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#project_id Model#project_id}
        :param space_id: Space ID of model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#space_id Model#space_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b09322d0f9114d2a2c048310bde83d9bc77093246e782983ffadf28bc6d905)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument model_path", value=model_path, expected_type=type_hints["model_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument software_spec", value=software_spec, expected_type=type_hints["software_spec"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
            check_type(argname="argument checksum", value=checksum, expected_type=type_hints["checksum"])
            check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
            check_type(argname="argument label_column", value=label_column, expected_type=type_hints["label_column"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument space_id", value=space_id, expected_type=type_hints["space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_path": model_path,
            "name": name,
            "software_spec": software_spec,
            "type": type,
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
        if asset_id is not None:
            self._values["asset_id"] = asset_id
        if checksum is not None:
            self._values["checksum"] = checksum
        if input_schema is not None:
            self._values["input_schema"] = input_schema
        if label_column is not None:
            self._values["label_column"] = label_column
        if project_id is not None:
            self._values["project_id"] = project_id
        if space_id is not None:
            self._values["space_id"] = space_id

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
    def model_path(self) -> builtins.str:
        '''tar.gz file of model from joblib.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#model_path Model#model_path}
        '''
        result = self._values.get("model_path")
        assert result is not None, "Required property 'model_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#name Model#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def software_spec(self) -> builtins.str:
        '''Software spec of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#software_spec Model#software_spec}
        '''
        result = self._values.get("software_spec")
        assert result is not None, "Required property 'software_spec' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#type Model#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_id(self) -> typing.Optional[builtins.str]:
        '''Asset ID of model in project. Used when promoting model in project to deployment space.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#asset_id Model#asset_id}
        '''
        result = self._values.get("asset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def checksum(self) -> typing.Optional[builtins.str]:
        '''Checksum of Python object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#checksum Model#checksum}
        '''
        result = self._values.get("checksum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_schema(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelInputSchema"]]]:
        '''Training input schema of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#input_schema Model#input_schema}
        '''
        result = self._values.get("input_schema")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelInputSchema"]]], result)

    @builtins.property
    def label_column(self) -> typing.Optional[builtins.str]:
        '''Label column of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#label_column Model#label_column}
        '''
        result = self._values.get("label_column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Project ID of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#project_id Model#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def space_id(self) -> typing.Optional[builtins.str]:
        '''Space ID of model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#space_id Model#space_id}
        '''
        result = self._values.get("space_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ibmcpd.model.ModelInputSchema",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ModelInputSchema:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#name Model#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#type Model#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e376310407379cc124d2f7294c49006c95d5fbb54882cbc027555ff82ca76379)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#name Model#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/model#type Model#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelInputSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelInputSchemaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.model.ModelInputSchemaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f20fed58816fc1551ba0334266a51befbf15723e453604c3faf4846c94cb4d02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ModelInputSchemaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4081259a0ee04037972c3783b375dbd9adb319071a4408ca508ea2014860bc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ModelInputSchemaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e97ff9cd6029869c5c98409a9dce19e70f79d1dbcbec59ccef96c7a820f955)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60f2acd4ddf4173b5db1df9c24899fabe5c216800f3afeed333c88ef987775b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7845f4ac1dd92f70592b0897386d0a69f8438137afb333b63a199b3d19330769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelInputSchema]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelInputSchema]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelInputSchema]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e98adf7fbf94ef0b83c675ad74f364455f2ce6fc448531740f62c73023715b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ModelInputSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.model.ModelInputSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e4a86c10445f97503c5f979b996bee626426249531032242bbaa08a755b8a6c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28b7aafc8fa3c4078335a32e7b0ed573106755be383237c26aeaa0f2f2dcd059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7506b1323cb518456cde9c17877a5da0bceac6db7d993a54e58acb8eebbbaac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ModelInputSchema, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ModelInputSchema, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ModelInputSchema, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8f8d300655abc6d778c68c7465645d6b4b29731c5affeb2b9d1f2cdd49ee35a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Model",
    "ModelConfig",
    "ModelInputSchema",
    "ModelInputSchemaList",
    "ModelInputSchemaOutputReference",
]

publication.publish()

def _typecheckingstub__7fd02fecf578b76356e53c1100510c7bbc47de4626d5a50d9d91974420264376(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    model_path: builtins.str,
    name: builtins.str,
    software_spec: builtins.str,
    type: builtins.str,
    asset_id: typing.Optional[builtins.str] = None,
    checksum: typing.Optional[builtins.str] = None,
    input_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelInputSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    label_column: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    space_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__afd613daecc771e7bca22bb9ce5f7f781a4c17f4a6436d0cb3072e22416f23f0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelInputSchema, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4220b7fcfb9cff145d6d12aadd414f5f9f6fbea91b7c293abcc09b4547ccfce9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad08eda7a65884f6ac1a4546abcfd84ee257a45a246d79705c2f99a0ae5de531(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10378694c642b28085cad217deebeceff0f3b7dafd5767f7a495542a57a70589(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785b707e1d1f5d2bb16907249b25b19b2af07f3a73bfb61af9e352f8795b0f69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14caa9557078b299225a264c1975c74d30f24e129887db5b87c8ea5afc361835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__616ebc03e193ee05045d63af91599c309887737e40d8a80e637f72f12f454e83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf4fbb6ec5931d7af0dc2ce4e272254e34060fb57dabfef43fb927aefa04679(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9892f80fe7f93508fea2f5368621d1f7795e4d55abe4c1f583747284757128(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66bd37345cc1ca6b3a220f39bf4eeb81f6c817619bf7261ea42f3cfc05a940a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b09322d0f9114d2a2c048310bde83d9bc77093246e782983ffadf28bc6d905(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    model_path: builtins.str,
    name: builtins.str,
    software_spec: builtins.str,
    type: builtins.str,
    asset_id: typing.Optional[builtins.str] = None,
    checksum: typing.Optional[builtins.str] = None,
    input_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelInputSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    label_column: typing.Optional[builtins.str] = None,
    project_id: typing.Optional[builtins.str] = None,
    space_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e376310407379cc124d2f7294c49006c95d5fbb54882cbc027555ff82ca76379(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20fed58816fc1551ba0334266a51befbf15723e453604c3faf4846c94cb4d02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4081259a0ee04037972c3783b375dbd9adb319071a4408ca508ea2014860bc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e97ff9cd6029869c5c98409a9dce19e70f79d1dbcbec59ccef96c7a820f955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f2acd4ddf4173b5db1df9c24899fabe5c216800f3afeed333c88ef987775b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7845f4ac1dd92f70592b0897386d0a69f8438137afb333b63a199b3d19330769(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e98adf7fbf94ef0b83c675ad74f364455f2ce6fc448531740f62c73023715b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelInputSchema]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4a86c10445f97503c5f979b996bee626426249531032242bbaa08a755b8a6c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b7aafc8fa3c4078335a32e7b0ed573106755be383237c26aeaa0f2f2dcd059(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7506b1323cb518456cde9c17877a5da0bceac6db7d993a54e58acb8eebbbaac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f8d300655abc6d778c68c7465645d6b4b29731c5affeb2b9d1f2cdd49ee35a(
    value: typing.Optional[typing.Union[ModelInputSchema, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
