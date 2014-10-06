# -*- coding: utf-8 -*-

###############################################################################
#
# PutRolePolicy
# Adds or updates a policy document associated with a specified role.
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

class PutRolePolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutRolePolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutRolePolicy, self).__init__(temboo_session, '/Library/Amazon/IAM/PutRolePolicy')


    def new_input_set(self):
        return PutRolePolicyInputSet()

    def _make_result_set(self, result, path):
        return PutRolePolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutRolePolicyChoreographyExecution(session, exec_id, path)

class PutRolePolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutRolePolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PolicyDocument(self, value):
        """
        Set the value of the PolicyDocument input for this Choreo. ((required, json) The policy document. See documentation for formatting examples.)
        """
        super(PutRolePolicyInputSet, self)._set_input('PolicyDocument', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutRolePolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutRolePolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_PolicyName(self, value):
        """
        Set the value of the PolicyName input for this Choreo. ((required, string) The name of the policy document.)
        """
        super(PutRolePolicyInputSet, self)._set_input('PolicyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(PutRolePolicyInputSet, self)._set_input('ResponseFormat', value)
    def set_RoleName(self, value):
        """
        Set the value of the RoleName input for this Choreo. ((required, string) The name of the role to associate the policy with.)
        """
        super(PutRolePolicyInputSet, self)._set_input('RoleName', value)

class PutRolePolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutRolePolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class PutRolePolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutRolePolicyResultSet(response, path)
