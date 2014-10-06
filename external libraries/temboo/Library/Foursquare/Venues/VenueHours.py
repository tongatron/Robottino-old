# -*- coding: utf-8 -*-

###############################################################################
#
# VenueHours
# Returns hours for a venue.
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

class VenueHours(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VenueHours Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VenueHours, self).__init__(temboo_session, '/Library/Foursquare/Venues/VenueHours')


    def new_input_set(self):
        return VenueHoursInputSet()

    def _make_result_set(self, result, path):
        return VenueHoursResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueHoursChoreographyExecution(session, exec_id, path)

class VenueHoursInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VenueHours
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(VenueHoursInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(VenueHoursInputSet, self)._set_input('ClientSecret', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(VenueHoursInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(VenueHoursInputSet, self)._set_input('ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID of the venue to retrieve hours for.)
        """
        super(VenueHoursInputSet, self)._set_input('VenueID', value)

class VenueHoursResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VenueHours Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class VenueHoursChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VenueHoursResultSet(response, path)
