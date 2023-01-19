'''
# `provider`

Refer to the Terraform Registory for docs: [`ibmcpd`](https://www.terraform.io/docs/providers/ibmcpd).
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


class IbmcpdProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="ibmcpd.provider.IbmcpdProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ibmcpd ibmcpd}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ibmcpd ibmcpd} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param url: URL for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#url IbmcpdProvider#url}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#alias IbmcpdProvider#alias}
        :param api_key: API key for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#api_key IbmcpdProvider#api_key}
        :param password: Password for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#password IbmcpdProvider#password}
        :param username: Username for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#username IbmcpdProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c534006d7aeacc21a3d439e4e4950a935e76af138a9dcd662713595ac742e92)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = IbmcpdProviderConfig(
            url=url, alias=alias, api_key=api_key, password=password, username=username
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ade711dc8dbfa35026d99b728c1a66ffc92dc7707a8cb87ef01ef997697bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005099104cb9d6ad423f24c6ea83680c5b47db5af69075aac6c81477fb1f96f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225537d3ab6c1f81bd8b14545f77eb16c72f0bfd32fce8e19e2a03c565d6ade2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3b5037f350ecb45e44371010ebb218cb972e62b3a67cc04a2025202140fdc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07aa4b62ccc09b22db865f9bafef7e37c2b666137af473a4631a286a500b3099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="ibmcpd.provider.IbmcpdProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "alias": "alias",
        "api_key": "apiKey",
        "password": "password",
        "username": "username",
    },
)
class IbmcpdProviderConfig:
    def __init__(
        self,
        *,
        url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: URL for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#url IbmcpdProvider#url}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#alias IbmcpdProvider#alias}
        :param api_key: API key for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#api_key IbmcpdProvider#api_key}
        :param password: Password for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#password IbmcpdProvider#password}
        :param username: Username for IBM Cloud Pak for Data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#username IbmcpdProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b18332c9d2b2a70bc9ee875d7a62bf40d9f7f331284e9d191a17824a04602a)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if alias is not None:
            self._values["alias"] = alias
        if api_key is not None:
            self._values["api_key"] = api_key
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def url(self) -> builtins.str:
        '''URL for IBM Cloud Pak for Data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#url IbmcpdProvider#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#alias IbmcpdProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''API key for IBM Cloud Pak for Data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#api_key IbmcpdProvider#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for IBM Cloud Pak for Data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#password IbmcpdProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for IBM Cloud Pak for Data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ibmcpd#username IbmcpdProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IbmcpdProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IbmcpdProvider",
    "IbmcpdProviderConfig",
]

publication.publish()

def _typecheckingstub__5c534006d7aeacc21a3d439e4e4950a935e76af138a9dcd662713595ac742e92(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    api_key: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ade711dc8dbfa35026d99b728c1a66ffc92dc7707a8cb87ef01ef997697bbb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005099104cb9d6ad423f24c6ea83680c5b47db5af69075aac6c81477fb1f96f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225537d3ab6c1f81bd8b14545f77eb16c72f0bfd32fce8e19e2a03c565d6ade2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3b5037f350ecb45e44371010ebb218cb972e62b3a67cc04a2025202140fdc0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07aa4b62ccc09b22db865f9bafef7e37c2b666137af473a4631a286a500b3099(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b18332c9d2b2a70bc9ee875d7a62bf40d9f7f331284e9d191a17824a04602a(
    *,
    url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    api_key: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
