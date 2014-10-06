# -*- coding: utf-8 -*-

###############################################################################
#
# GetSimilar
# Retrieves a list of all the artists similar to the specified artist.
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

class GetSimilar(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSimilar Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSimilar, self).__init__(temboo_session, '/Library/LastFm/Artist/GetSimilar')


    def new_input_set(self):
        return GetSimilarInputSet()

    def _make_result_set(self, result, path):
        return GetSimilarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSimilarChoreographyExecution(session, exec_id, path)

class GetSimilarInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSimilar
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        super(GetSimilarInputSet, self)._set_input('APIKey', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        super(GetSimilarInputSet, self)._set_input('Artist', value)
    def set_AutoCorrect(self, value):
        """
        Set the value of the AutoCorrect input for this Choreo. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        super(GetSimilarInputSet, self)._set_input('AutoCorrect', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        super(GetSimilarInputSet, self)._set_input('Limit', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the artist. Required unless providing Artist.)
        """
        super(GetSimilarInputSet, self)._set_input('MbID', value)

class GetSimilarResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSimilar Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetSimilarChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSimilarResultSet(response, path)
