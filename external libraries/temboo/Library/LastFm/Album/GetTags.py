# -*- coding: utf-8 -*-

###############################################################################
#
# GetTags
# Retrieves the tags applied by an individual user to an album on Last.fm.
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

class GetTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTags, self).__init__(temboo_session, '/Library/LastFm/Album/GetTags')


    def new_input_set(self):
        return GetTagsInputSet()

    def _make_result_set(self, result, path):
        return GetTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTagsChoreographyExecution(session, exec_id, path)

class GetTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        super(GetTagsInputSet, self)._set_input('APIKey', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((conditional, string) The album name. Required unless providing MbID.)
        """
        super(GetTagsInputSet, self)._set_input('Album', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        super(GetTagsInputSet, self)._set_input('Artist', value)
    def set_AutoCorrect(self, value):
        """
        Set the value of the AutoCorrect input for this Choreo. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        super(GetTagsInputSet, self)._set_input('AutoCorrect', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the album. Required unless providing the Album and Artist.)
        """
        super(GetTagsInputSet, self)._set_input('MbID', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The last.fm username to lookup.)
        """
        super(GetTagsInputSet, self)._set_input('User', value)

class GetTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTagsResultSet(response, path)
