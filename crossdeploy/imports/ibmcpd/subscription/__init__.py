'''
# `ibmcpd_subscription`

Refer to the Terraform Registory for docs: [`ibmcpd_subscription`](https://www.terraform.io/docs/providers/ibmcpd/r/subscription).
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


class Subscription(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.Subscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription ibmcpd_subscription}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        asset: typing.Union[typing.Union["SubscriptionAsset", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        asset_properties: typing.Union[typing.Union["SubscriptionAssetProperties", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        data_mart_id: builtins.str,
        deployment: typing.Union[typing.Union["SubscriptionDeployment", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        service_provider_id: builtins.str,
        aws_access_key_id: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_secret_access_key: typing.Optional[builtins.str] = None,
        payload_file: typing.Optional[builtins.str] = None,
        training_data_reference: typing.Optional[typing.Union[typing.Union["SubscriptionTrainingDataReference", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
        training_data_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SubscriptionTrainingDataSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription ibmcpd_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param asset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset Subscription#asset}.
        :param asset_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_properties Subscription#asset_properties}.
        :param data_mart_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#data_mart_id Subscription#data_mart_id}.
        :param deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment Subscription#deployment}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.
        :param service_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#service_provider_id Subscription#service_provider_id}.
        :param aws_access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_access_key_id Subscription#aws_access_key_id}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_region Subscription#aws_region}.
        :param aws_secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_secret_access_key Subscription#aws_secret_access_key}.
        :param payload_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#payload_file Subscription#payload_file}.
        :param training_data_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_reference Subscription#training_data_reference}.
        :param training_data_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_schema Subscription#training_data_schema}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80791c4e231a945761a710c4fe38aa69738133dfec8fc98fc03f8639f74d408)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SubscriptionConfig(
            asset=asset,
            asset_properties=asset_properties,
            data_mart_id=data_mart_id,
            deployment=deployment,
            name=name,
            service_provider_id=service_provider_id,
            aws_access_key_id=aws_access_key_id,
            aws_region=aws_region,
            aws_secret_access_key=aws_secret_access_key,
            payload_file=payload_file,
            training_data_reference=training_data_reference,
            training_data_schema=training_data_schema,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putAsset")
    def put_asset(
        self,
        value: typing.Union[typing.Union["SubscriptionAsset", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac026a9c770f6b70205669a4a061bd83e0d681101a412d8f17a8a372f09a66d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAsset", [value]))

    @jsii.member(jsii_name="putAssetProperties")
    def put_asset_properties(
        self,
        value: typing.Union[typing.Union["SubscriptionAssetProperties", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5aab6e8b6321e482e293c0402eb8782cd1421b73e6aeb6262fdfcc058196afd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssetProperties", [value]))

    @jsii.member(jsii_name="putDeployment")
    def put_deployment(
        self,
        value: typing.Union[typing.Union["SubscriptionDeployment", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d1cd38af202b5bc6158ca770773aa96eccde5dbe8f2129927a47d2bf6a744a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployment", [value]))

    @jsii.member(jsii_name="putTrainingDataReference")
    def put_training_data_reference(
        self,
        value: typing.Union[typing.Union["SubscriptionTrainingDataReference", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81ef500f3427c920dd242217dcc6eb6f4fd3b8051502f3b3ffe91d1e37dc1be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrainingDataReference", [value]))

    @jsii.member(jsii_name="putTrainingDataSchema")
    def put_training_data_schema(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SubscriptionTrainingDataSchema", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb185344cd5b817d9b637d41b65036b0a558c474852aaed198317425bda47f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrainingDataSchema", [value]))

    @jsii.member(jsii_name="resetAwsAccessKeyId")
    def reset_aws_access_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAccessKeyId", []))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @jsii.member(jsii_name="resetAwsSecretAccessKey")
    def reset_aws_secret_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSecretAccessKey", []))

    @jsii.member(jsii_name="resetPayloadFile")
    def reset_payload_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadFile", []))

    @jsii.member(jsii_name="resetTrainingDataReference")
    def reset_training_data_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrainingDataReference", []))

    @jsii.member(jsii_name="resetTrainingDataSchema")
    def reset_training_data_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrainingDataSchema", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="asset")
    def asset(self) -> "SubscriptionAssetOutputReference":
        return typing.cast("SubscriptionAssetOutputReference", jsii.get(self, "asset"))

    @builtins.property
    @jsii.member(jsii_name="assetProperties")
    def asset_properties(self) -> "SubscriptionAssetPropertiesOutputReference":
        return typing.cast("SubscriptionAssetPropertiesOutputReference", jsii.get(self, "assetProperties"))

    @builtins.property
    @jsii.member(jsii_name="deployment")
    def deployment(self) -> "SubscriptionDeploymentOutputReference":
        return typing.cast("SubscriptionDeploymentOutputReference", jsii.get(self, "deployment"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="trainingDataReference")
    def training_data_reference(
        self,
    ) -> "SubscriptionTrainingDataReferenceOutputReference":
        return typing.cast("SubscriptionTrainingDataReferenceOutputReference", jsii.get(self, "trainingDataReference"))

    @builtins.property
    @jsii.member(jsii_name="trainingDataSchema")
    def training_data_schema(self) -> "SubscriptionTrainingDataSchemaList":
        return typing.cast("SubscriptionTrainingDataSchemaList", jsii.get(self, "trainingDataSchema"))

    @builtins.property
    @jsii.member(jsii_name="assetInput")
    def asset_input(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionAsset", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubscriptionAsset", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assetInput"))

    @builtins.property
    @jsii.member(jsii_name="assetPropertiesInput")
    def asset_properties_input(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionAssetProperties", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubscriptionAssetProperties", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assetPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKeyIdInput")
    def aws_access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSecretAccessKeyInput")
    def aws_secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSecretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMartIdInput")
    def data_mart_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataMartIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentInput")
    def deployment_input(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionDeployment", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubscriptionDeployment", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadFileInput")
    def payload_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadFileInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceProviderIdInput")
    def service_provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceProviderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="trainingDataReferenceInput")
    def training_data_reference_input(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionTrainingDataReference", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SubscriptionTrainingDataReference", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "trainingDataReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="trainingDataSchemaInput")
    def training_data_schema_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SubscriptionTrainingDataSchema"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SubscriptionTrainingDataSchema"]]], jsii.get(self, "trainingDataSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAccessKeyId")
    def aws_access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccessKeyId"))

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9eddafe0509b7f62b4b93f828eaf0907ef90b6e3026ae867a882b856dea0a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1228728386cebb40d46b684a65546a938eabea398f5f69316bb218e6229dff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSecretAccessKey"))

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56f08692a33898e12ec5dcf7ba3551a252b3111e702dc82fa03cb78f5ca643e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSecretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="dataMartId")
    def data_mart_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataMartId"))

    @data_mart_id.setter
    def data_mart_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f63ef5fbeceb1da46e5c25bfbdfe7f27e61985ca829cb4e82e2f119fb8bc0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataMartId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6729ea19d9229e77221d81260d089bfaa79e0639b1ba6b2bb2da3c0608f0eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFile")
    def payload_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadFile"))

    @payload_file.setter
    def payload_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a816c4f1bb7d593c3ccda6ced331032dbc164513bbf96597f5cfb88c4901f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFile", value)

    @builtins.property
    @jsii.member(jsii_name="serviceProviderId")
    def service_provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceProviderId"))

    @service_provider_id.setter
    def service_provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d10926e840f4d4b30feb0ba3f7210b7f3509edc234680b21d7b21d69b9a33fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceProviderId", value)


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionAsset",
    jsii_struct_bases=[],
    name_mapping={
        "asset_id": "assetId",
        "asset_type": "assetType",
        "input_data_type": "inputDataType",
        "problem_type": "problemType",
        "url": "url",
    },
)
class SubscriptionAsset:
    def __init__(
        self,
        *,
        asset_id: builtins.str,
        asset_type: builtins.str,
        input_data_type: builtins.str,
        problem_type: builtins.str,
        url: builtins.str,
    ) -> None:
        '''
        :param asset_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_id Subscription#asset_id}.
        :param asset_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_type Subscription#asset_type}.
        :param input_data_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#input_data_type Subscription#input_data_type}.
        :param problem_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#problem_type Subscription#problem_type}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#url Subscription#url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff16a38431ce6d8d948bd15d3aa1a650df563f1dae315a56fc0d0f819bdf403b)
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
            check_type(argname="argument asset_type", value=asset_type, expected_type=type_hints["asset_type"])
            check_type(argname="argument input_data_type", value=input_data_type, expected_type=type_hints["input_data_type"])
            check_type(argname="argument problem_type", value=problem_type, expected_type=type_hints["problem_type"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_id": asset_id,
            "asset_type": asset_type,
            "input_data_type": input_data_type,
            "problem_type": problem_type,
            "url": url,
        }

    @builtins.property
    def asset_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_id Subscription#asset_id}.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_type Subscription#asset_type}.'''
        result = self._values.get("asset_type")
        assert result is not None, "Required property 'asset_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_data_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#input_data_type Subscription#input_data_type}.'''
        result = self._values.get("input_data_type")
        assert result is not None, "Required property 'input_data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def problem_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#problem_type Subscription#problem_type}.'''
        result = self._values.get("problem_type")
        assert result is not None, "Required property 'problem_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#url Subscription#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionAssetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionAssetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e4c796700597e29bfa16f171251b5cee100719d148e90c3ee02438d01a028b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="assetIdInput")
    def asset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="assetTypeInput")
    def asset_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="inputDataTypeInput")
    def input_data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputDataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="problemTypeInput")
    def problem_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "problemTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="assetId")
    def asset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assetId"))

    @asset_id.setter
    def asset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53546f618226ae6324059c8a42a8fc8f52fa170413d21a76d3b3e9db0d8eef52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetId", value)

    @builtins.property
    @jsii.member(jsii_name="assetType")
    def asset_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assetType"))

    @asset_type.setter
    def asset_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c1fcb53824257959a7bea6e6d05d1c988691a32d79f6b69c9fd49efedd1953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetType", value)

    @builtins.property
    @jsii.member(jsii_name="inputDataType")
    def input_data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputDataType"))

    @input_data_type.setter
    def input_data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05749eea22f75b351a8c19c705ae87bf981768f9ba96197424ae97b3aa836875)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputDataType", value)

    @builtins.property
    @jsii.member(jsii_name="problemType")
    def problem_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "problemType"))

    @problem_type.setter
    def problem_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8b689eedd41e1414cffa3194b1f69142a6baaf72c7d2a7064fab8833179ff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "problemType", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f4e33a2710471f996401a96be4b1613e5198cf3176aa913407fd64b194c8a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233906f8eabf6a6d9d83b4a3915d17b0f229dd559937ac60fc81338fb4aba031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionAssetProperties",
    jsii_struct_bases=[],
    name_mapping={
        "categorical_fields": "categoricalFields",
        "feature_fields": "featureFields",
        "label_column": "labelColumn",
        "prediction_field": "predictionField",
        "probability_fields": "probabilityFields",
    },
)
class SubscriptionAssetProperties:
    def __init__(
        self,
        *,
        categorical_fields: typing.Sequence[builtins.str],
        feature_fields: typing.Sequence[builtins.str],
        label_column: builtins.str,
        prediction_field: builtins.str,
        probability_fields: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param categorical_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#categorical_fields Subscription#categorical_fields}.
        :param feature_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#feature_fields Subscription#feature_fields}.
        :param label_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#label_column Subscription#label_column}.
        :param prediction_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#prediction_field Subscription#prediction_field}.
        :param probability_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#probability_fields Subscription#probability_fields}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e0e33494dcd92aa13b93555dd673752a1935ebc748500dfb0e247a4112b7d0)
            check_type(argname="argument categorical_fields", value=categorical_fields, expected_type=type_hints["categorical_fields"])
            check_type(argname="argument feature_fields", value=feature_fields, expected_type=type_hints["feature_fields"])
            check_type(argname="argument label_column", value=label_column, expected_type=type_hints["label_column"])
            check_type(argname="argument prediction_field", value=prediction_field, expected_type=type_hints["prediction_field"])
            check_type(argname="argument probability_fields", value=probability_fields, expected_type=type_hints["probability_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "categorical_fields": categorical_fields,
            "feature_fields": feature_fields,
            "label_column": label_column,
            "prediction_field": prediction_field,
            "probability_fields": probability_fields,
        }

    @builtins.property
    def categorical_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#categorical_fields Subscription#categorical_fields}.'''
        result = self._values.get("categorical_fields")
        assert result is not None, "Required property 'categorical_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def feature_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#feature_fields Subscription#feature_fields}.'''
        result = self._values.get("feature_fields")
        assert result is not None, "Required property 'feature_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def label_column(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#label_column Subscription#label_column}.'''
        result = self._values.get("label_column")
        assert result is not None, "Required property 'label_column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prediction_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#prediction_field Subscription#prediction_field}.'''
        result = self._values.get("prediction_field")
        assert result is not None, "Required property 'prediction_field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def probability_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#probability_fields Subscription#probability_fields}.'''
        result = self._values.get("probability_fields")
        assert result is not None, "Required property 'probability_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionAssetProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionAssetPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionAssetPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f619477ac9da321b1f65356afe9de42b4df3fe6a70c8bd1ba2092fec4f9feec0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="categoricalFieldsInput")
    def categorical_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "categoricalFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="featureFieldsInput")
    def feature_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "featureFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelColumnInput")
    def label_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="predictionFieldInput")
    def prediction_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predictionFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="probabilityFieldsInput")
    def probability_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "probabilityFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="categoricalFields")
    def categorical_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "categoricalFields"))

    @categorical_fields.setter
    def categorical_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7201b033c80ed8778592d10a72b519e08cf281f4c26b6e45802bdb0e05ff12cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoricalFields", value)

    @builtins.property
    @jsii.member(jsii_name="featureFields")
    def feature_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "featureFields"))

    @feature_fields.setter
    def feature_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__535abe4f884d60884e2405768536f4e45f3d6b9333d707adc9ed67413816bd41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureFields", value)

    @builtins.property
    @jsii.member(jsii_name="labelColumn")
    def label_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelColumn"))

    @label_column.setter
    def label_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a49c6881384252fec8871100b7af6850f849f7ccee00c88457b7ee11c6f117e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelColumn", value)

    @builtins.property
    @jsii.member(jsii_name="predictionField")
    def prediction_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predictionField"))

    @prediction_field.setter
    def prediction_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208e1ff8d24747b224a6bd728309ee1d4c1148c310ac8a73740ee570071e8572)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predictionField", value)

    @builtins.property
    @jsii.member(jsii_name="probabilityFields")
    def probability_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "probabilityFields"))

    @probability_fields.setter
    def probability_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae3ce6b2fe00f6ed7d0714dd5bb07e06db5906444ec1441e48785decff351f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probabilityFields", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945437ea361cf625a081c41b5bb83aef9aa986d55aa977295f11521adda9ae7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "asset": "asset",
        "asset_properties": "assetProperties",
        "data_mart_id": "dataMartId",
        "deployment": "deployment",
        "name": "name",
        "service_provider_id": "serviceProviderId",
        "aws_access_key_id": "awsAccessKeyId",
        "aws_region": "awsRegion",
        "aws_secret_access_key": "awsSecretAccessKey",
        "payload_file": "payloadFile",
        "training_data_reference": "trainingDataReference",
        "training_data_schema": "trainingDataSchema",
    },
)
class SubscriptionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        asset: typing.Union[typing.Union[SubscriptionAsset, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        asset_properties: typing.Union[typing.Union[SubscriptionAssetProperties, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        data_mart_id: builtins.str,
        deployment: typing.Union[typing.Union["SubscriptionDeployment", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        service_provider_id: builtins.str,
        aws_access_key_id: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_secret_access_key: typing.Optional[builtins.str] = None,
        payload_file: typing.Optional[builtins.str] = None,
        training_data_reference: typing.Optional[typing.Union[typing.Union["SubscriptionTrainingDataReference", typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
        training_data_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SubscriptionTrainingDataSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param asset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset Subscription#asset}.
        :param asset_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_properties Subscription#asset_properties}.
        :param data_mart_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#data_mart_id Subscription#data_mart_id}.
        :param deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment Subscription#deployment}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.
        :param service_provider_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#service_provider_id Subscription#service_provider_id}.
        :param aws_access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_access_key_id Subscription#aws_access_key_id}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_region Subscription#aws_region}.
        :param aws_secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_secret_access_key Subscription#aws_secret_access_key}.
        :param payload_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#payload_file Subscription#payload_file}.
        :param training_data_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_reference Subscription#training_data_reference}.
        :param training_data_schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_schema Subscription#training_data_schema}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd69251d6134e1b172c4235b4a010d1765ab560bb6fcd3bbd115b01cf5e6e4f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument asset", value=asset, expected_type=type_hints["asset"])
            check_type(argname="argument asset_properties", value=asset_properties, expected_type=type_hints["asset_properties"])
            check_type(argname="argument data_mart_id", value=data_mart_id, expected_type=type_hints["data_mart_id"])
            check_type(argname="argument deployment", value=deployment, expected_type=type_hints["deployment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_provider_id", value=service_provider_id, expected_type=type_hints["service_provider_id"])
            check_type(argname="argument aws_access_key_id", value=aws_access_key_id, expected_type=type_hints["aws_access_key_id"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument aws_secret_access_key", value=aws_secret_access_key, expected_type=type_hints["aws_secret_access_key"])
            check_type(argname="argument payload_file", value=payload_file, expected_type=type_hints["payload_file"])
            check_type(argname="argument training_data_reference", value=training_data_reference, expected_type=type_hints["training_data_reference"])
            check_type(argname="argument training_data_schema", value=training_data_schema, expected_type=type_hints["training_data_schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset": asset,
            "asset_properties": asset_properties,
            "data_mart_id": data_mart_id,
            "deployment": deployment,
            "name": name,
            "service_provider_id": service_provider_id,
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
        if aws_access_key_id is not None:
            self._values["aws_access_key_id"] = aws_access_key_id
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if aws_secret_access_key is not None:
            self._values["aws_secret_access_key"] = aws_secret_access_key
        if payload_file is not None:
            self._values["payload_file"] = payload_file
        if training_data_reference is not None:
            self._values["training_data_reference"] = training_data_reference
        if training_data_schema is not None:
            self._values["training_data_schema"] = training_data_schema

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
    def asset(self) -> typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset Subscription#asset}.'''
        result = self._values.get("asset")
        assert result is not None, "Required property 'asset' is missing"
        return typing.cast(typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def asset_properties(
        self,
    ) -> typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#asset_properties Subscription#asset_properties}.'''
        result = self._values.get("asset_properties")
        assert result is not None, "Required property 'asset_properties' is missing"
        return typing.cast(typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def data_mart_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#data_mart_id Subscription#data_mart_id}.'''
        result = self._values.get("data_mart_id")
        assert result is not None, "Required property 'data_mart_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment(
        self,
    ) -> typing.Union["SubscriptionDeployment", _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment Subscription#deployment}.'''
        result = self._values.get("deployment")
        assert result is not None, "Required property 'deployment' is missing"
        return typing.cast(typing.Union["SubscriptionDeployment", _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_provider_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#service_provider_id Subscription#service_provider_id}.'''
        result = self._values.get("service_provider_id")
        assert result is not None, "Required property 'service_provider_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_access_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_access_key_id Subscription#aws_access_key_id}.'''
        result = self._values.get("aws_access_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_region Subscription#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_secret_access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#aws_secret_access_key Subscription#aws_secret_access_key}.'''
        result = self._values.get("aws_secret_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#payload_file Subscription#payload_file}.'''
        result = self._values.get("payload_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def training_data_reference(
        self,
    ) -> typing.Optional[typing.Union["SubscriptionTrainingDataReference", _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_reference Subscription#training_data_reference}.'''
        result = self._values.get("training_data_reference")
        return typing.cast(typing.Optional[typing.Union["SubscriptionTrainingDataReference", _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def training_data_schema(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SubscriptionTrainingDataSchema"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#training_data_schema Subscription#training_data_schema}.'''
        result = self._values.get("training_data_schema")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SubscriptionTrainingDataSchema"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_id": "deploymentId",
        "deployment_type": "deploymentType",
        "deployment_url": "deploymentUrl",
        "name": "name",
        "scoring_url": "scoringUrl",
    },
)
class SubscriptionDeployment:
    def __init__(
        self,
        *,
        deployment_id: builtins.str,
        deployment_type: builtins.str,
        deployment_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        scoring_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_id Subscription#deployment_id}.
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_type Subscription#deployment_type}.
        :param deployment_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_url Subscription#deployment_url}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.
        :param scoring_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#scoring_url Subscription#scoring_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf2226a2c6b472e872c28b1828b88f4652b1466a648004e2bdf49b015ae95e0)
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument deployment_url", value=deployment_url, expected_type=type_hints["deployment_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scoring_url", value=scoring_url, expected_type=type_hints["scoring_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_id": deployment_id,
            "deployment_type": deployment_type,
        }
        if deployment_url is not None:
            self._values["deployment_url"] = deployment_url
        if name is not None:
            self._values["name"] = name
        if scoring_url is not None:
            self._values["scoring_url"] = scoring_url

    @builtins.property
    def deployment_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_id Subscription#deployment_id}.'''
        result = self._values.get("deployment_id")
        assert result is not None, "Required property 'deployment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_type Subscription#deployment_type}.'''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#deployment_url Subscription#deployment_url}.'''
        result = self._values.get("deployment_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scoring_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#scoring_url Subscription#scoring_url}.'''
        result = self._values.get("scoring_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionDeploymentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionDeploymentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74c5fe815cb457c8442c61f55aba17479c79916c12a36bcec7c9a87e0e45097c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeploymentUrl")
    def reset_deployment_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentUrl", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetScoringUrl")
    def reset_scoring_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoringUrl", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentIdInput")
    def deployment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentUrlInput")
    def deployment_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scoringUrlInput")
    def scoring_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scoringUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentId"))

    @deployment_id.setter
    def deployment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d7657b3d1c69bc1a05fbbe7b4bb828b1eff024cbf86ccf609859bd87fdeff37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentId", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e3c48b83c0ae6f826e2baaffb18f6e8a4897a57ceb98aa177c6efc24ef6d91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentUrl")
    def deployment_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentUrl"))

    @deployment_url.setter
    def deployment_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f267b2db87ffb4cc440a49b78d2556f65d2f00ab99c357f56798607f5d9ca57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3043db1d9b419d9739bdee169d740040a8ee21a43f9dc02d5e2d8fdf85f3a055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scoringUrl")
    def scoring_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scoringUrl"))

    @scoring_url.setter
    def scoring_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044f49fcdd7a2d5b7201dbb41b65cdb244112ab763892ed423ebee356dd4c659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoringUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionDeployment, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionDeployment, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionDeployment, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f1879af0df2df226dbd0a9536e31a61a7c8aa09e8aa827043d2f5ac288c3d9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionTrainingDataReference",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "cos_api_key": "cosApiKey",
        "cos_url": "cosUrl",
        "database_name": "databaseName",
        "file_name": "fileName",
        "hostname": "hostname",
        "iam_url": "iamUrl",
        "password": "password",
        "port": "port",
        "resource_instance_id": "resourceInstanceId",
        "schema_name": "schemaName",
        "ssl": "ssl",
        "table_name": "tableName",
        "type": "type",
        "username": "username",
    },
)
class SubscriptionTrainingDataReference:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        cos_api_key: typing.Optional[builtins.str] = None,
        cos_url: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        file_name: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        iam_url: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        resource_instance_id: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        table_name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#bucket_name Subscription#bucket_name}.
        :param cos_api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#cos_api_key Subscription#cos_api_key}.
        :param cos_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#cos_url Subscription#cos_url}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#database_name Subscription#database_name}.
        :param file_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#file_name Subscription#file_name}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#hostname Subscription#hostname}.
        :param iam_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#iam_url Subscription#iam_url}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#password Subscription#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#port Subscription#port}.
        :param resource_instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#resource_instance_id Subscription#resource_instance_id}.
        :param schema_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#schema_name Subscription#schema_name}.
        :param ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#ssl Subscription#ssl}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#table_name Subscription#table_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#type Subscription#type}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#username Subscription#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a49d8e0d3c862666aebc8f78de9a0922f626eeb5b583907be505342bd5707013)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument cos_api_key", value=cos_api_key, expected_type=type_hints["cos_api_key"])
            check_type(argname="argument cos_url", value=cos_url, expected_type=type_hints["cos_url"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument iam_url", value=iam_url, expected_type=type_hints["iam_url"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument resource_instance_id", value=resource_instance_id, expected_type=type_hints["resource_instance_id"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if cos_api_key is not None:
            self._values["cos_api_key"] = cos_api_key
        if cos_url is not None:
            self._values["cos_url"] = cos_url
        if database_name is not None:
            self._values["database_name"] = database_name
        if file_name is not None:
            self._values["file_name"] = file_name
        if hostname is not None:
            self._values["hostname"] = hostname
        if iam_url is not None:
            self._values["iam_url"] = iam_url
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if resource_instance_id is not None:
            self._values["resource_instance_id"] = resource_instance_id
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if ssl is not None:
            self._values["ssl"] = ssl
        if table_name is not None:
            self._values["table_name"] = table_name
        if type is not None:
            self._values["type"] = type
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#bucket_name Subscription#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cos_api_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#cos_api_key Subscription#cos_api_key}.'''
        result = self._values.get("cos_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cos_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#cos_url Subscription#cos_url}.'''
        result = self._values.get("cos_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#database_name Subscription#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#file_name Subscription#file_name}.'''
        result = self._values.get("file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#hostname Subscription#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#iam_url Subscription#iam_url}.'''
        result = self._values.get("iam_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#password Subscription#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#port Subscription#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#resource_instance_id Subscription#resource_instance_id}.'''
        result = self._values.get("resource_instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#schema_name Subscription#schema_name}.'''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#ssl Subscription#ssl}.'''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#table_name Subscription#table_name}.'''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#type Subscription#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#username Subscription#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionTrainingDataReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionTrainingDataReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionTrainingDataReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b552f2269520c5cfbf504ec6c132a2d9eb562da49273a1f56c95b0b7c213ee1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetCosApiKey")
    def reset_cos_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosApiKey", []))

    @jsii.member(jsii_name="resetCosUrl")
    def reset_cos_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCosUrl", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetFileName")
    def reset_file_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileName", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetIamUrl")
    def reset_iam_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamUrl", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetResourceInstanceId")
    def reset_resource_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceInstanceId", []))

    @jsii.member(jsii_name="resetSchemaName")
    def reset_schema_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaName", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetTableName")
    def reset_table_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cosApiKeyInput")
    def cos_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="cosUrlInput")
    def cos_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cosUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileNameInput")
    def file_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="iamUrlInput")
    def iam_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInstanceIdInput")
    def resource_instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa960ed0dceed12a05da49b4c623963379960856edba44a2848f0f5cb7acf20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cosApiKey")
    def cos_api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosApiKey"))

    @cos_api_key.setter
    def cos_api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__096045e9e188ec3939648eb970d494700e92a4862768bcddac42e8351cd51a59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="cosUrl")
    def cos_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cosUrl"))

    @cos_url.setter
    def cos_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf16494bd1ee297006b0ee25abbecb2349c7a0f446851b418cb7c6df7aabd967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cosUrl", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf6f314132ce3c2b44a2703cbd4dbb823c4711a66c23f73534d45cacc559146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="fileName")
    def file_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileName"))

    @file_name.setter
    def file_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d4806cc2ef9d48a1cf93173b9d93c2094c08564076ddd8c8503c068754ba0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileName", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde70af46ef665894d30cdce268d83049e4ef16a3f2cca192cb5f555b9832f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="iamUrl")
    def iam_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamUrl"))

    @iam_url.setter
    def iam_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a59c6be8799fd98db6df52d7171e7746fc198d8971da42ebb41b4f18911eb3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamUrl", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422821963ff9cbcd28438ee0e6c939b2a10de0cd53f3b72403abde9f2c28298c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993b12e6836f0eb3096df40654be9a59f83a0a0da466093e392bee2e4dd0c50a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="resourceInstanceId")
    def resource_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceInstanceId"))

    @resource_instance_id.setter
    def resource_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d3694cd8ea1b398c8b758d84e0c063866e99e2a800eb5c2ee2a7539779e706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8026793056181a293c70780012628087ec39760be098378c09ea8010f7201973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49712f0539d4db3be035ac767f6dfeaf991ad9c0564da9ef7913a47e437bd5f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba03590a38158e04b694d9e36a41c12edadb145ca11cb400ea51d01f52a36793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c516b4f180d5580c57ae0a57cdf979c8fff7a9acc8cf3eb2ddcd10eeea6ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033e8d59bf6c4281e412a7513d26999a4c4204a0be9b5fdbe0f7a3e2ff3849f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionTrainingDataReference, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionTrainingDataReference, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionTrainingDataReference, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__776177a8b14da1b88c414598eaa51fcb18665b692b4e935bd94210aee3d07222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="ibmcpd.subscription.SubscriptionTrainingDataSchema",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "nullable": "nullable", "type": "type"},
)
class SubscriptionTrainingDataSchema:
    def __init__(
        self,
        *,
        name: builtins.str,
        nullable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        type: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.
        :param nullable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#nullable Subscription#nullable}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#type Subscription#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6f536d4b4187c80c4231e32d76e078f7f84fecae8361d6729d596c141a9064)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "nullable": nullable,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#name Subscription#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#nullable Subscription#nullable}.'''
        result = self._values.get("nullable")
        assert result is not None, "Required property 'nullable' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd/r/subscription#type Subscription#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionTrainingDataSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionTrainingDataSchemaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionTrainingDataSchemaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__da6d111bdee69e5d5b434495905331e5bb7c9af67c0e7dc4aa30acca37476ac3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SubscriptionTrainingDataSchemaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d0763ff3ecb02c2cafb5bc3ac58cf2ce66f6778e699dbbe330d072a99d51a0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SubscriptionTrainingDataSchemaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c512104e37cb346f4caadc9586906d22e09f141f0bc60a229313cc0d61c7a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc9fecf568a9b4f7df8cc833defaf31f328b93166daf9b5b7cf2325633f73f52)
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
            type_hints = typing.get_type_hints(_typecheckingstub__129fba648de83bf727e0837819a498703dfcda32fd5832fd467c8da1296b79f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SubscriptionTrainingDataSchema]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SubscriptionTrainingDataSchema]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SubscriptionTrainingDataSchema]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__373e2c68cfbde078928d1c29a6eac2c04c0c2f1b5b6061270fa8ba54ea73cabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SubscriptionTrainingDataSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.subscription.SubscriptionTrainingDataSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c62c2fc7cf9d943672470b132883ce8876b11a0fa03a87e0adde664867812758)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__74e7a8037a17f52e6d0d91eff9fb470b80dd6f95d914478a2eb627b4b4d253cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec283b0d95c029441ac6be8ffc5d8f2a243e02cae5366d976a5c865963e75ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7526b910cbec2c890b7eca8fbec7cc22e009cc34c063bb3633e59a5bc25002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SubscriptionTrainingDataSchema, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SubscriptionTrainingDataSchema, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SubscriptionTrainingDataSchema, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7f9077184ee6c9add871dd839419baf56f7707dc17ec8bdb95201c305e603e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Subscription",
    "SubscriptionAsset",
    "SubscriptionAssetOutputReference",
    "SubscriptionAssetProperties",
    "SubscriptionAssetPropertiesOutputReference",
    "SubscriptionConfig",
    "SubscriptionDeployment",
    "SubscriptionDeploymentOutputReference",
    "SubscriptionTrainingDataReference",
    "SubscriptionTrainingDataReferenceOutputReference",
    "SubscriptionTrainingDataSchema",
    "SubscriptionTrainingDataSchemaList",
    "SubscriptionTrainingDataSchemaOutputReference",
]

publication.publish()

def _typecheckingstub__b80791c4e231a945761a710c4fe38aa69738133dfec8fc98fc03f8639f74d408(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    asset: typing.Union[typing.Union[SubscriptionAsset, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    asset_properties: typing.Union[typing.Union[SubscriptionAssetProperties, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    data_mart_id: builtins.str,
    deployment: typing.Union[typing.Union[SubscriptionDeployment, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    service_provider_id: builtins.str,
    aws_access_key_id: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_secret_access_key: typing.Optional[builtins.str] = None,
    payload_file: typing.Optional[builtins.str] = None,
    training_data_reference: typing.Optional[typing.Union[typing.Union[SubscriptionTrainingDataReference, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
    training_data_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SubscriptionTrainingDataSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__aac026a9c770f6b70205669a4a061bd83e0d681101a412d8f17a8a372f09a66d(
    value: typing.Union[typing.Union[SubscriptionAsset, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5aab6e8b6321e482e293c0402eb8782cd1421b73e6aeb6262fdfcc058196afd(
    value: typing.Union[typing.Union[SubscriptionAssetProperties, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d1cd38af202b5bc6158ca770773aa96eccde5dbe8f2129927a47d2bf6a744a(
    value: typing.Union[typing.Union[SubscriptionDeployment, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ef500f3427c920dd242217dcc6eb6f4fd3b8051502f3b3ffe91d1e37dc1be8(
    value: typing.Union[typing.Union[SubscriptionTrainingDataReference, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb185344cd5b817d9b637d41b65036b0a558c474852aaed198317425bda47f98(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SubscriptionTrainingDataSchema, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9eddafe0509b7f62b4b93f828eaf0907ef90b6e3026ae867a882b856dea0a3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1228728386cebb40d46b684a65546a938eabea398f5f69316bb218e6229dff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f08692a33898e12ec5dcf7ba3551a252b3111e702dc82fa03cb78f5ca643e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f63ef5fbeceb1da46e5c25bfbdfe7f27e61985ca829cb4e82e2f119fb8bc0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6729ea19d9229e77221d81260d089bfaa79e0639b1ba6b2bb2da3c0608f0eb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a816c4f1bb7d593c3ccda6ced331032dbc164513bbf96597f5cfb88c4901f25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d10926e840f4d4b30feb0ba3f7210b7f3509edc234680b21d7b21d69b9a33fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff16a38431ce6d8d948bd15d3aa1a650df563f1dae315a56fc0d0f819bdf403b(
    *,
    asset_id: builtins.str,
    asset_type: builtins.str,
    input_data_type: builtins.str,
    problem_type: builtins.str,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4c796700597e29bfa16f171251b5cee100719d148e90c3ee02438d01a028b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53546f618226ae6324059c8a42a8fc8f52fa170413d21a76d3b3e9db0d8eef52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c1fcb53824257959a7bea6e6d05d1c988691a32d79f6b69c9fd49efedd1953(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05749eea22f75b351a8c19c705ae87bf981768f9ba96197424ae97b3aa836875(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8b689eedd41e1414cffa3194b1f69142a6baaf72c7d2a7064fab8833179ff4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f4e33a2710471f996401a96be4b1613e5198cf3176aa913407fd64b194c8a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233906f8eabf6a6d9d83b4a3915d17b0f229dd559937ac60fc81338fb4aba031(
    value: typing.Optional[typing.Union[SubscriptionAsset, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e0e33494dcd92aa13b93555dd673752a1935ebc748500dfb0e247a4112b7d0(
    *,
    categorical_fields: typing.Sequence[builtins.str],
    feature_fields: typing.Sequence[builtins.str],
    label_column: builtins.str,
    prediction_field: builtins.str,
    probability_fields: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f619477ac9da321b1f65356afe9de42b4df3fe6a70c8bd1ba2092fec4f9feec0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7201b033c80ed8778592d10a72b519e08cf281f4c26b6e45802bdb0e05ff12cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535abe4f884d60884e2405768536f4e45f3d6b9333d707adc9ed67413816bd41(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a49c6881384252fec8871100b7af6850f849f7ccee00c88457b7ee11c6f117e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208e1ff8d24747b224a6bd728309ee1d4c1148c310ac8a73740ee570071e8572(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae3ce6b2fe00f6ed7d0714dd5bb07e06db5906444ec1441e48785decff351f7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945437ea361cf625a081c41b5bb83aef9aa986d55aa977295f11521adda9ae7a(
    value: typing.Optional[typing.Union[SubscriptionAssetProperties, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd69251d6134e1b172c4235b4a010d1765ab560bb6fcd3bbd115b01cf5e6e4f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    asset: typing.Union[typing.Union[SubscriptionAsset, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    asset_properties: typing.Union[typing.Union[SubscriptionAssetProperties, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    data_mart_id: builtins.str,
    deployment: typing.Union[typing.Union[SubscriptionDeployment, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    service_provider_id: builtins.str,
    aws_access_key_id: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_secret_access_key: typing.Optional[builtins.str] = None,
    payload_file: typing.Optional[builtins.str] = None,
    training_data_reference: typing.Optional[typing.Union[typing.Union[SubscriptionTrainingDataReference, typing.Dict[builtins.str, typing.Any]], _cdktf_9a9027ec.IResolvable]] = None,
    training_data_schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SubscriptionTrainingDataSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf2226a2c6b472e872c28b1828b88f4652b1466a648004e2bdf49b015ae95e0(
    *,
    deployment_id: builtins.str,
    deployment_type: builtins.str,
    deployment_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    scoring_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c5fe815cb457c8442c61f55aba17479c79916c12a36bcec7c9a87e0e45097c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7657b3d1c69bc1a05fbbe7b4bb828b1eff024cbf86ccf609859bd87fdeff37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e3c48b83c0ae6f826e2baaffb18f6e8a4897a57ceb98aa177c6efc24ef6d91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f267b2db87ffb4cc440a49b78d2556f65d2f00ab99c357f56798607f5d9ca57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3043db1d9b419d9739bdee169d740040a8ee21a43f9dc02d5e2d8fdf85f3a055(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044f49fcdd7a2d5b7201dbb41b65cdb244112ab763892ed423ebee356dd4c659(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1879af0df2df226dbd0a9536e31a61a7c8aa09e8aa827043d2f5ac288c3d9f(
    value: typing.Optional[typing.Union[SubscriptionDeployment, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a49d8e0d3c862666aebc8f78de9a0922f626eeb5b583907be505342bd5707013(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    cos_api_key: typing.Optional[builtins.str] = None,
    cos_url: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    file_name: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    iam_url: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    resource_instance_id: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    table_name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b552f2269520c5cfbf504ec6c132a2d9eb562da49273a1f56c95b0b7c213ee1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa960ed0dceed12a05da49b4c623963379960856edba44a2848f0f5cb7acf20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__096045e9e188ec3939648eb970d494700e92a4862768bcddac42e8351cd51a59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf16494bd1ee297006b0ee25abbecb2349c7a0f446851b418cb7c6df7aabd967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf6f314132ce3c2b44a2703cbd4dbb823c4711a66c23f73534d45cacc559146(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d4806cc2ef9d48a1cf93173b9d93c2094c08564076ddd8c8503c068754ba0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde70af46ef665894d30cdce268d83049e4ef16a3f2cca192cb5f555b9832f54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a59c6be8799fd98db6df52d7171e7746fc198d8971da42ebb41b4f18911eb3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422821963ff9cbcd28438ee0e6c939b2a10de0cd53f3b72403abde9f2c28298c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993b12e6836f0eb3096df40654be9a59f83a0a0da466093e392bee2e4dd0c50a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d3694cd8ea1b398c8b758d84e0c063866e99e2a800eb5c2ee2a7539779e706(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8026793056181a293c70780012628087ec39760be098378c09ea8010f7201973(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49712f0539d4db3be035ac767f6dfeaf991ad9c0564da9ef7913a47e437bd5f2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba03590a38158e04b694d9e36a41c12edadb145ca11cb400ea51d01f52a36793(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c516b4f180d5580c57ae0a57cdf979c8fff7a9acc8cf3eb2ddcd10eeea6ca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033e8d59bf6c4281e412a7513d26999a4c4204a0be9b5fdbe0f7a3e2ff3849f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__776177a8b14da1b88c414598eaa51fcb18665b692b4e935bd94210aee3d07222(
    value: typing.Optional[typing.Union[SubscriptionTrainingDataReference, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6f536d4b4187c80c4231e32d76e078f7f84fecae8361d6729d596c141a9064(
    *,
    name: builtins.str,
    nullable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da6d111bdee69e5d5b434495905331e5bb7c9af67c0e7dc4aa30acca37476ac3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d0763ff3ecb02c2cafb5bc3ac58cf2ce66f6778e699dbbe330d072a99d51a0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c512104e37cb346f4caadc9586906d22e09f141f0bc60a229313cc0d61c7a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9fecf568a9b4f7df8cc833defaf31f328b93166daf9b5b7cf2325633f73f52(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129fba648de83bf727e0837819a498703dfcda32fd5832fd467c8da1296b79f1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373e2c68cfbde078928d1c29a6eac2c04c0c2f1b5b6061270fa8ba54ea73cabf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SubscriptionTrainingDataSchema]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62c2fc7cf9d943672470b132883ce8876b11a0fa03a87e0adde664867812758(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e7a8037a17f52e6d0d91eff9fb470b80dd6f95d914478a2eb627b4b4d253cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec283b0d95c029441ac6be8ffc5d8f2a243e02cae5366d976a5c865963e75ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7526b910cbec2c890b7eca8fbec7cc22e009cc34c063bb3633e59a5bc25002(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7f9077184ee6c9add871dd839419baf56f7707dc17ec8bdb95201c305e603e(
    value: typing.Optional[typing.Union[SubscriptionTrainingDataSchema, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
