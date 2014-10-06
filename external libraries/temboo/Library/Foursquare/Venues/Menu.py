# -*- coding: utf-8 -*-

###############################################################################
#
# Menu
# Returns menu information for a venue.
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

class Menu(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Menu Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Menu, self).__init__(temboo_session, '/Library/Foursquare/Venues/Menu')


    def new_input_set(self):
        return MenuInputSet()

    def _make_result_set(self, result, path):
        return MenuResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MenuChoreographyExecution(session, exec_id, path)

class MenuInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Menu
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(MenuInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(MenuInputSet, self)._set_input('ClientSecret', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(MenuInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(MenuInputSet, self)._set_input('ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID of the venue to retrieve menu information for.)
        """
        super(MenuInputSet, self)._set_input('VenueID', value)

class MenuResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Menu Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class MenuChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MenuResultSet(response, path)
