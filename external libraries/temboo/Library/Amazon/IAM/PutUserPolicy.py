# -*- coding: utf-8 -*-

###############################################################################
#
# PutUserPolicy
# Adds or updates a policy document associated with a specified user.
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

class PutUserPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutUserPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PutUserPolicy, self).__init__(temboo_session, '/Library/Amazon/IAM/PutUserPolicy')


    def new_input_set(self):
        return PutUserPolicyInputSet()

    def _make_result_set(self, result, path):
        return PutUserPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutUserPolicyChoreographyExecution(session, exec_id, path)

class PutUserPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutUserPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PolicyDocument(self, value):
        """
        Set the value of the PolicyDocument input for this Choreo. ((required, json) The policy document. See documentation for formatting examples.)
        """
        super(PutUserPolicyInputSet, self)._set_input('PolicyDocument', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(PutUserPolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(PutUserPolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_PolicyName(self, value):
        """
        Set the value of the PolicyName input for this Choreo. ((required, string) The name of the policy document.)
        """
        super(PutUserPolicyInputSet, self)._set_input('PolicyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(PutUserPolicyInputSet, self)._set_input('ResponseFormat', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) The name of the user to associate the policy with.)
        """
        super(PutUserPolicyInputSet, self)._set_input('UserName', value)

class PutUserPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutUserPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class PutUserPolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PutUserPolicyResultSet(response, path)
