# -*- coding: utf-8 -*-

###############################################################################
#
# ListSets
# Returns the photosets belonging to the specified user.
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

class ListSets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListSets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListSets, self).__init__(temboo_session, '/Library/Flickr/PhotoSets/ListSets')


    def new_input_set(self):
        return ListSetsInputSet()

    def _make_result_set(self, result, path):
        return ListSetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSetsChoreographyExecution(session, exec_id, path)

class ListSetsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListSets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ListSetsInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((conditional, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret). Required when accessing a protected resource or when UserID is not provided.)
        """
        super(ListSetsInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((conditional, string) The Access Token Secret retrieved during the OAuth process. Required when accessing a protected resource or when UserID is not provided.)
        """
        super(ListSetsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource or when UserID is not provided.)
        """
        super(ListSetsInputSet, self)._set_input('AccessToken', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to get. Currently, if this is not provided, all sets are returned, but this behaviour may change in future.)
        """
        super(ListSetsInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of sets to get per page. If paging is enabled, the maximum number of sets per page is 500.)
        """
        super(ListSetsInputSet, self)._set_input('PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ListSetsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The NSID of the user to get a photoset list for. When OAuth parameters are passed, the authenticated user is assumed.)
        """
        super(ListSetsInputSet, self)._set_input('UserID', value)

class ListSetsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListSets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListSetsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListSetsResultSet(response, path)
