# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFriendship
# Allows you to follow another Twitter user by specifying a Twitter user id or screen name.
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

class CreateFriendship(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFriendship Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateFriendship, self).__init__(temboo_session, '/Library/Twitter/FriendsAndFollowers/CreateFriendship')


    def new_input_set(self):
        return CreateFriendshipInputSet()

    def _make_result_set(self, result, path):
        return CreateFriendshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFriendshipChoreographyExecution(session, exec_id, path)

class CreateFriendshipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFriendship
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(CreateFriendshipInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(CreateFriendshipInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(CreateFriendshipInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(CreateFriendshipInputSet, self)._set_input('ConsumerSecret', value)
    def set_Follow(self, value):
        """
        Set the value of the Follow input for this Choreo. ((optional, boolean) A boolean flag that enables notifications for the target user when set to true.)
        """
        super(CreateFriendshipInputSet, self)._set_input('Follow', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name for the friend you want to create a friendship with. Required if UserId isn't specified.)
        """
        super(CreateFriendshipInputSet, self)._set_input('ScreenName', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((conditional, string) The user id for the friend you want to create a friendship with. Required if ScreenName isn't specified.)
        """
        super(CreateFriendshipInputSet, self)._set_input('UserId', value)

class CreateFriendshipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFriendship Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class CreateFriendshipChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateFriendshipResultSet(response, path)
