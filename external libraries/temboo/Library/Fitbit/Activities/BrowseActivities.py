# -*- coding: utf-8 -*-

###############################################################################
#
# BrowseActivities
# Gets a tree of all valid Fitbit public activities from the activities catalog as well as private custom activities the user created.
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

class BrowseActivities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BrowseActivities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(BrowseActivities, self).__init__(temboo_session, '/Library/Fitbit/Activities/BrowseActivities')


    def new_input_set(self):
        return BrowseActivitiesInputSet()

    def _make_result_set(self, result, path):
        return BrowseActivitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BrowseActivitiesChoreographyExecution(session, exec_id, path)

class BrowseActivitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BrowseActivities
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(BrowseActivitiesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(BrowseActivitiesInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(BrowseActivitiesInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(BrowseActivitiesInputSet, self)._set_input('ConsumerSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(BrowseActivitiesInputSet, self)._set_input('ResponseFormat', value)

class BrowseActivitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BrowseActivities Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class BrowseActivitiesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BrowseActivitiesResultSet(response, path)
