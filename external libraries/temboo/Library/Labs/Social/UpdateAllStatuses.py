# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAllStatuses
# Shares a post across multiple social networks such as Facebook, Tumblr, and Twitter.
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

class UpdateAllStatuses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAllStatuses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateAllStatuses, self).__init__(temboo_session, '/Library/Labs/Social/UpdateAllStatuses')


    def new_input_set(self):
        return UpdateAllStatusesInputSet()

    def _make_result_set(self, result, path):
        return UpdateAllStatusesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAllStatusesChoreographyExecution(session, exec_id, path)

class UpdateAllStatusesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAllStatuses
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A list of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        super(UpdateAllStatusesInputSet, self)._set_input('APICredentials', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The message to be posted across social networks.)
        """
        super(UpdateAllStatusesInputSet, self)._set_input('Message', value)

class UpdateAllStatusesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAllStatuses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) A list of results for each API.)
        """
        return self._output.get('Response', None)

class UpdateAllStatusesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateAllStatusesResultSet(response, path)
