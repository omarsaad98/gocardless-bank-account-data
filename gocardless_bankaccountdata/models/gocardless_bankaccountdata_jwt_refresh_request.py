# coding: utf-8

"""
    GoCardless Bank Account Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0 (v2)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GocardlessBankaccountdataJWTRefreshRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'refresh': 'str'
    }

    attribute_map = {
        'refresh': 'refresh'
    }

    def __init__(self, refresh=None):  # noqa: E501
        """GocardlessBankaccountdataJWTRefreshRequest - a model defined in Swagger"""  # noqa: E501
        self._refresh = None
        self.discriminator = None
        self.refresh = refresh

    @property
    def refresh(self):
        """Gets the refresh of this GocardlessBankaccountdataJWTRefreshRequest.  # noqa: E501


        :return: The refresh of this GocardlessBankaccountdataJWTRefreshRequest.  # noqa: E501
        :rtype: str
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this GocardlessBankaccountdataJWTRefreshRequest.


        :param refresh: The refresh of this GocardlessBankaccountdataJWTRefreshRequest.  # noqa: E501
        :type: str
        """
        if refresh is None:
            raise ValueError("Invalid value for `refresh`, must not be `None`")  # noqa: E501

        self._refresh = refresh

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GocardlessBankaccountdataJWTRefreshRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GocardlessBankaccountdataJWTRefreshRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
