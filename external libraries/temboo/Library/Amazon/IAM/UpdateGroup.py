# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateGroup
# Updates the name and/or the path of a specified group.
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

class UpdateGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateGroup, self).__init__(temboo_session, '/Library/Amazon/IAM/UpdateGroup')


    def new_input_set(self):
        return UpdateGroupInputSet()

    def _make_result_set(self, result, path):
        return UpdateGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateGroupChoreographyExecution(session, exec_id, path)

class UpdateGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateGroup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UpdateGroupInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UpdateGroupInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((required, string) The name of the group to update.)
        """
        super(UpdateGroupInputSet, self)._set_input('GroupName', value)
    def set_NewGroupName(self, value):
        """
        Set the value of the NewGroupName input for this Choreo. ((optional, string) The new name of the group. Include a value here only if you are updating the group's name.)
        """
        super(UpdateGroupInputSet, self)._set_input('NewGroupName', value)
    def set_NewPath(self, value):
        """
        Set the value of the NewPath input for this Choreo. ((optional, string) The new path for the group. Include a value here only if you are changing the user's existing path.)
        """
        super(UpdateGroupInputSet, self)._set_input('NewPath', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UpdateGroupInputSet, self)._set_input('ResponseFormat', value)

class UpdateGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateGroupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateGroupResultSet(response, path)
