# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteAction
# Deletes a given custom action.
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

class DeleteAction(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteAction Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteAction, self).__init__(temboo_session, '/Library/Facebook/Actions/Custom/DeleteAction')


    def new_input_set(self):
        return DeleteActionInputSet()

    def _make_result_set(self, result, path):
        return DeleteActionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteActionChoreographyExecution(session, exec_id, path)

class DeleteActionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteAction
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(DeleteActionInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of an action to delete.)
        """
        super(DeleteActionInputSet, self)._set_input('ActionID', value)

class DeleteActionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteAction Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeleteActionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteActionResultSet(response, path)
