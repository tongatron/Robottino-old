# -*- coding: utf-8 -*-

###############################################################################
#
# GetRole
# Retrieves information about the specified role, including the role's path, ARN, RoleId, and the policy granting permission to EC2 to assume the role.
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

class GetRole(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRole Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRole, self).__init__(temboo_session, '/Library/Amazon/IAM/GetRole')


    def new_input_set(self):
        return GetRoleInputSet()

    def _make_result_set(self, result, path):
        return GetRoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRoleChoreographyExecution(session, exec_id, path)

class GetRoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRole
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetRoleInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetRoleInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetRoleInputSet, self)._set_input('ResponseFormat', value)
    def set_RoleName(self, value):
        """
        Set the value of the RoleName input for this Choreo. ((required, string) Name of the role to get information about.)
        """
        super(GetRoleInputSet, self)._set_input('RoleName', value)

class GetRoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRole Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetRoleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRoleResultSet(response, path)
