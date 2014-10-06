# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteGroupPolicy
# Deletes the specified policy that is associated with the specified group.
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

class DeleteGroupPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteGroupPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteGroupPolicy, self).__init__(temboo_session, '/Library/Amazon/IAM/DeleteGroupPolicy')


    def new_input_set(self):
        return DeleteGroupPolicyInputSet()

    def _make_result_set(self, result, path):
        return DeleteGroupPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteGroupPolicyChoreographyExecution(session, exec_id, path)

class DeleteGroupPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteGroupPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteGroupPolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteGroupPolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((required, string) Name of the group the policy is associated with.)
        """
        super(DeleteGroupPolicyInputSet, self)._set_input('GroupName', value)
    def set_PolicyName(self, value):
        """
        Set the value of the PolicyName input for this Choreo. ((required, string) Name of the policy document.)
        """
        super(DeleteGroupPolicyInputSet, self)._set_input('PolicyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DeleteGroupPolicyInputSet, self)._set_input('ResponseFormat', value)

class DeleteGroupPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteGroupPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteGroupPolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteGroupPolicyResultSet(response, path)
