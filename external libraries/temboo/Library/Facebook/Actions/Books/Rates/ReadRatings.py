# -*- coding: utf-8 -*-

###############################################################################
#
# ReadRatings
# Retrieves one or more book rating actions.
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

class ReadRatings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadRatings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReadRatings, self).__init__(temboo_session, '/Library/Facebook/Actions/Books/Rates/ReadRatings')


    def new_input_set(self):
        return ReadRatingsInputSet()

    def _make_result_set(self, result, path):
        return ReadRatingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadRatingsChoreographyExecution(session, exec_id, path)

class ReadRatingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadRatings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(ReadRatingsInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((optional, string) The id of an action to retrieve. If an id is not provided, a list of all rate actions will be returned.)
        """
        super(ReadRatingsInputSet, self)._set_input('ActionID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        super(ReadRatingsInputSet, self)._set_input('Fields', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the response.)
        """
        super(ReadRatingsInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results. Returns results starting from the specified number.)
        """
        super(ReadRatingsInputSet, self)._set_input('Offset', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the user's profile. Defaults to "me" indicating the authenticated user.)
        """
        super(ReadRatingsInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(ReadRatingsInputSet, self)._set_input('ResponseFormat', value)

class ReadRatingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadRatings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_HasNext(self):
        """
        Retrieve the value for the "HasNext" output from this Choreo execution. ((boolean) A boolean flag indicating that a next page exists.)
        """
        return self._output.get('HasNext', None)
    def get_HasPrevious(self):
        """
        Retrieve the value for the "HasPrevious" output from this Choreo execution. ((boolean) A boolean flag indicating that a previous page exists.)
        """
        return self._output.get('HasPrevious', None)

class ReadRatingsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReadRatingsResultSet(response, path)
