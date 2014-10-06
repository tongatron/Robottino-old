# -*- coding: utf-8 -*-

###############################################################################
#
# PhotosFromVenue
# Returns photos for a venue.
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

class PhotosFromVenue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PhotosFromVenue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PhotosFromVenue, self).__init__(temboo_session, '/Library/Foursquare/Venues/PhotosFromVenue')


    def new_input_set(self):
        return PhotosFromVenueInputSet()

    def _make_result_set(self, result, path):
        return PhotosFromVenueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhotosFromVenueChoreographyExecution(session, exec_id, path)

class PhotosFromVenueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PhotosFromVenue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('ClientSecret', value)
    def set_Group(self, value):
        """
        Set the value of the Group input for this Choreo. ((optional, string) By default, public venue photos are returned ordered by relevance. Pass "venue" for public venue photos, ordered by most recent. Pass "checkin" for venue photos from friends, ordered by most recenct.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('Group', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 200.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API OAuth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used in combination with the Limit input to page through results.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID of the venue to retrieve photos for.)
        """
        super(PhotosFromVenueInputSet, self)._set_input('VenueID', value)

class PhotosFromVenueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PhotosFromVenue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class PhotosFromVenueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PhotosFromVenueResultSet(response, path)
