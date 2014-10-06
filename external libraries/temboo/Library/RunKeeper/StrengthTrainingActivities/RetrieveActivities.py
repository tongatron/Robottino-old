# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveActivities
# Returns the feed for a user's strength training activities.
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

class RetrieveActivities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveActivities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveActivities, self).__init__(temboo_session, '/Library/RunKeeper/StrengthTrainingActivities/RetrieveActivities')


    def new_input_set(self):
        return RetrieveActivitiesInputSet()

    def _make_result_set(self, result, path):
        return RetrieveActivitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveActivitiesChoreographyExecution(session, exec_id, path)

class RetrieveActivitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveActivities
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        super(RetrieveActivitiesInputSet, self)._set_input('AccessToken', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number entries to return per page. Defaults to 25.)
        """
        super(RetrieveActivitiesInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of entries to return. This parameter is used in combination with the PageSize input to page through results. Defaults to 0 (the first page).)
        """
        super(RetrieveActivitiesInputSet, self)._set_input('Page', value)

class RetrieveActivitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveActivities Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)
    def get_Next(self):
        """
        Retrieve the value for the "Next" output from this Choreo execution. ((integer) The next page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Next', None)
    def get_Previous(self):
        """
        Retrieve the value for the "Previous" output from this Choreo execution. ((integer) The previous page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Previous', None)

class RetrieveActivitiesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveActivitiesResultSet(response, path)
