# -*- coding: utf-8 -*-

###############################################################################
#
# GetBuyLinks
# Retrieves a list of Buy Links for a particular Album.
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

class GetBuyLinks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBuyLinks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBuyLinks, self).__init__(temboo_session, '/Library/LastFm/Album/GetBuyLinks')


    def new_input_set(self):
        return GetBuyLinksInputSet()

    def _make_result_set(self, result, path):
        return GetBuyLinksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBuyLinksChoreographyExecution(session, exec_id, path)

class GetBuyLinksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBuyLinks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        super(GetBuyLinksInputSet, self)._set_input('APIKey', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((conditional, string) The album name. Required unless providing MbID.)
        """
        super(GetBuyLinksInputSet, self)._set_input('Album', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        super(GetBuyLinksInputSet, self)._set_input('Artist', value)
    def set_AutoCorrect(self, value):
        """
        Set the value of the AutoCorrect input for this Choreo. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        super(GetBuyLinksInputSet, self)._set_input('AutoCorrect', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) A country name, as defined by the ISO 3166-1 country names standard.)
        """
        super(GetBuyLinksInputSet, self)._set_input('Country', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the album. Required unless providing the Album and Artist.)
        """
        super(GetBuyLinksInputSet, self)._set_input('MbID', value)

class GetBuyLinksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBuyLinks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetBuyLinksChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBuyLinksResultSet(response, path)
