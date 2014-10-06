# -*- coding: utf-8 -*-

###############################################################################
#
# DestroyList
# Deletes the specified list.
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

class DestroyList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DestroyList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DestroyList, self).__init__(temboo_session, '/Library/Twitter/Lists/DestroyList')


    def new_input_set(self):
        return DestroyListInputSet()

    def _make_result_set(self, result, path):
        return DestroyListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DestroyListChoreographyExecution(session, exec_id, path)

class DestroyListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DestroyList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(DestroyListInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(DestroyListInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(DestroyListInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(DestroyListInputSet, self)._set_input('ConsumerSecret', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((conditional, string) The numerical ID of the list. Required unless Slug is provided.)
        """
        super(DestroyListInputSet, self)._set_input('ListId', value)
    def set_OwnerId(self, value):
        """
        Set the value of the OwnerId input for this Choreo. ((optional, string) The user ID of the user who owns the list being requested by a slug.)
        """
        super(DestroyListInputSet, self)._set_input('OwnerId', value)
    def set_OwnerScreenName(self, value):
        """
        Set the value of the OwnerScreenName input for this Choreo. ((optional, string) The screen name of the user who owns the list being requested by a slug.)
        """
        super(DestroyListInputSet, self)._set_input('OwnerScreenName', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) When identifying a list by a slug, either OwnerScreenName or OwnerId must be provided.)
        """
        super(DestroyListInputSet, self)._set_input('Slug', value)

class DestroyListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DestroyList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class DestroyListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DestroyListResultSet(response, path)
