# -*- coding: utf-8 -*-

###############################################################################
#
# GetPersonalTags
# Retrieves a user's personal tags.
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

class GetPersonalTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPersonalTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPersonalTags, self).__init__(temboo_session, '/Library/LastFm/User/GetPersonalTags')


    def new_input_set(self):
        return GetPersonalTagsInputSet()

    def _make_result_set(self, result, path):
        return GetPersonalTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPersonalTagsChoreographyExecution(session, exec_id, path)

class GetPersonalTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPersonalTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('Page', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((string) The tag you're interested in.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('Tag', value)
    def set_TaggingType(self, value):
        """
        Set the value of the TaggingType input for this Choreo. ((string) The type of items which have been tagged. Valid values are: artist, album, track.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('TaggingType', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The user who performed the taggings.)
        """
        super(GetPersonalTagsInputSet, self)._set_input('User', value)

class GetPersonalTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPersonalTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetPersonalTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPersonalTagsResultSet(response, path)
