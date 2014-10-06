# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRun
# Updates an existing run action.
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

class UpdateRun(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRun Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateRun, self).__init__(temboo_session, '/Library/Facebook/Actions/Fitness/Runs/UpdateRun')


    def new_input_set(self):
        return UpdateRunInputSet()

    def _make_result_set(self, result, path):
        return UpdateRunResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRunChoreographyExecution(session, exec_id, path)

class UpdateRunInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRun
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(UpdateRunInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        super(UpdateRunInputSet, self)._set_input('ActionID', value)
    def set_Course(self, value):
        """
        Set the value of the Course input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the course.)
        """
        super(UpdateRunInputSet, self)._set_input('Course', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(UpdateRunInputSet, self)._set_input('EndTime', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        super(UpdateRunInputSet, self)._set_input('ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        super(UpdateRunInputSet, self)._set_input('Message', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        super(UpdateRunInputSet, self)._set_input('Place', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        super(UpdateRunInputSet, self)._set_input('Tags', value)

class UpdateRunResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRun Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook.)
        """
        return self._output.get('Response', None)

class UpdateRunChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateRunResultSet(response, path)
