# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteListen
# Deletes a given listen action.
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

class DeleteListen(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteListen Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteListen, self).__init__(temboo_session, '/Library/Facebook/Actions/Music/Listens/DeleteListen')


    def new_input_set(self):
        return DeleteListenInputSet()

    def _make_result_set(self, result, path):
        return DeleteListenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteListenChoreographyExecution(session, exec_id, path)

class DeleteListenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteListen
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(DeleteListenInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of an action to delete.)
        """
        super(DeleteListenInputSet, self)._set_input('ActionID', value)

class DeleteListenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteListen Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeleteListenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteListenResultSet(response, path)
