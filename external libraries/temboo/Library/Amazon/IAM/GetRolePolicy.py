# -*- coding: utf-8 -*-

###############################################################################
#
# GetRolePolicy
# Retrieves the specified policy document for the specified role.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRolePolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRolePolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRolePolicy, self).__init__(temboo_session, '/Library/Amazon/IAM/GetRolePolicy')


    def new_input_set(self):
        return GetRolePolicyInputSet()

    def _make_result_set(self, result, path):
        return GetRolePolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRolePolicyChoreographyExecution(session, exec_id, path)

class GetRolePolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRolePolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetRolePolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetRolePolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_PolicyName(self, value):
        """
        Set the value of the PolicyName input for this Choreo. ((required, string) Name of the policy document to get.)
        """
        super(GetRolePolicyInputSet, self)._set_input('PolicyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetRolePolicyInputSet, self)._set_input('ResponseFormat', value)
    def set_RoleName(self, value):
        """
        Set the value of the RoleName input for this Choreo. ((required, string) Name of the role associated with the policy.)
        """
        super(GetRolePolicyInputSet, self)._set_input('RoleName', value)

class GetRolePolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRolePolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetRolePolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRolePolicyResultSet(response, path)
