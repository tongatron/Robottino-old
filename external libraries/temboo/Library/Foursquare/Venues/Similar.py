# -*- coding: utf-8 -*-

###############################################################################
#
# Similar
# Returns a list of venues similar to the specified venue.
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

class Similar(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Similar Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Similar, self).__init__(temboo_session, '/Library/Foursquare/Venues/Similar')


    def new_input_set(self):
        return SimilarInputSet()

    def _make_result_set(self, result, path):
        return SimilarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SimilarChoreographyExecution(session, exec_id, path)

class SimilarInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Similar
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(SimilarInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(SimilarInputSet, self)._set_input('ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The id for the venue you want similar venues for.)
        """
        super(SimilarInputSet, self)._set_input('VenueID', value)

class SimilarResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Similar Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class SimilarChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SimilarResultSet(response, path)
