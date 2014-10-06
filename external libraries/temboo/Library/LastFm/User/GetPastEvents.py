# -*- coding: utf-8 -*-

###############################################################################
#
# GetPastEvents
# Retrieves a paginated list of all events a user has attended in the past. 
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

class GetPastEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPastEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPastEvents, self).__init__(temboo_session, '/Library/LastFm/User/GetPastEvents')


    def new_input_set(self):
        return GetPastEventsInputSet()

    def _make_result_set(self, result, path):
        return GetPastEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPastEventsChoreographyExecution(session, exec_id, path)

class GetPastEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPastEvents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(GetPastEventsInputSet, self)._set_input('APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        super(GetPastEventsInputSet, self)._set_input('Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        super(GetPastEventsInputSet, self)._set_input('Page', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The username to fetch the events for.)
        """
        super(GetPastEventsInputSet, self)._set_input('User', value)

class GetPastEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPastEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetPastEventsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPastEventsResultSet(response, path)
