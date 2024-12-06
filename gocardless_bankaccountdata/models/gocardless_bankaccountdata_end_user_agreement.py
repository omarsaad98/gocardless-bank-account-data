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

class GocardlessBankaccountdataEndUserAgreement(object):
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
        'id': 'str',
        'created': 'datetime',
        'institution_id': 'str',
        'max_historical_days': 'int',
        'access_valid_for_days': 'int',
        'access_scope': 'list[object]',
        'accepted': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'institution_id': 'institution_id',
        'max_historical_days': 'max_historical_days',
        'access_valid_for_days': 'access_valid_for_days',
        'access_scope': 'access_scope',
        'accepted': 'accepted'
    }

    def __init__(self, id=None, created=None, institution_id=None, max_historical_days=90, access_valid_for_days=90, access_scope=None, accepted=None):  # noqa: E501
        """GocardlessBankaccountdataEndUserAgreement - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._institution_id = None
        self._max_historical_days = None
        self._access_valid_for_days = None
        self._access_scope = None
        self._accepted = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        self.institution_id = institution_id
        if max_historical_days is not None:
            self.max_historical_days = max_historical_days
        if access_valid_for_days is not None:
            self.access_valid_for_days = access_valid_for_days
        if access_scope is not None:
            self.access_scope = access_scope
        if accepted is not None:
            self.accepted = accepted

    @property
    def id(self):
        """Gets the id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        The ID of this End User Agreement, used to refer to this end user agreement in other API calls.  # noqa: E501

        :return: The id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GocardlessBankaccountdataEndUserAgreement.

        The ID of this End User Agreement, used to refer to this end user agreement in other API calls.  # noqa: E501

        :param id: The id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        The date & time at which the end user agreement was created.  # noqa: E501

        :return: The created of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GocardlessBankaccountdataEndUserAgreement.

        The date & time at which the end user agreement was created.  # noqa: E501

        :param created: The created of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def institution_id(self):
        """Gets the institution_id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        an Institution ID for this EUA  # noqa: E501

        :return: The institution_id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this GocardlessBankaccountdataEndUserAgreement.

        an Institution ID for this EUA  # noqa: E501

        :param institution_id: The institution_id of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: str
        """
        if institution_id is None:
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def max_historical_days(self):
        """Gets the max_historical_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        Maximum number of days of transaction data to retrieve.  # noqa: E501

        :return: The max_historical_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: int
        """
        return self._max_historical_days

    @max_historical_days.setter
    def max_historical_days(self, max_historical_days):
        """Sets the max_historical_days of this GocardlessBankaccountdataEndUserAgreement.

        Maximum number of days of transaction data to retrieve.  # noqa: E501

        :param max_historical_days: The max_historical_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: int
        """

        self._max_historical_days = max_historical_days

    @property
    def access_valid_for_days(self):
        """Gets the access_valid_for_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        Number of days from acceptance that the access can be used.  # noqa: E501

        :return: The access_valid_for_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: int
        """
        return self._access_valid_for_days

    @access_valid_for_days.setter
    def access_valid_for_days(self, access_valid_for_days):
        """Sets the access_valid_for_days of this GocardlessBankaccountdataEndUserAgreement.

        Number of days from acceptance that the access can be used.  # noqa: E501

        :param access_valid_for_days: The access_valid_for_days of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: int
        """

        self._access_valid_for_days = access_valid_for_days

    @property
    def access_scope(self):
        """Gets the access_scope of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        Array containing one or several values of ['balances', 'details', 'transactions']  # noqa: E501

        :return: The access_scope of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: list[object]
        """
        return self._access_scope

    @access_scope.setter
    def access_scope(self, access_scope):
        """Sets the access_scope of this GocardlessBankaccountdataEndUserAgreement.

        Array containing one or several values of ['balances', 'details', 'transactions']  # noqa: E501

        :param access_scope: The access_scope of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: list[object]
        """

        self._access_scope = access_scope

    @property
    def accepted(self):
        """Gets the accepted of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501

        The date & time at which the end user accepted the agreement.  # noqa: E501

        :return: The accepted of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :rtype: datetime
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this GocardlessBankaccountdataEndUserAgreement.

        The date & time at which the end user accepted the agreement.  # noqa: E501

        :param accepted: The accepted of this GocardlessBankaccountdataEndUserAgreement.  # noqa: E501
        :type: datetime
        """

        self._accepted = accepted

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
        if issubclass(GocardlessBankaccountdataEndUserAgreement, dict):
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
        if not isinstance(other, GocardlessBankaccountdataEndUserAgreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
