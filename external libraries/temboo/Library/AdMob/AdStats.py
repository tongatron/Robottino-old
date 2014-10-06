# -*- coding: utf-8 -*-

###############################################################################
#
# AdStats
# Retrieve ad statistics by specifying IDs.
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

class AdStats(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AdStats Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AdStats, self).__init__(temboo_session, '/Library/AdMob/AdStats')


    def new_input_set(self):
        return AdStatsInputSet()

    def _make_result_set(self, result, path):
        return AdStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdStatsChoreographyExecution(session, exec_id, path)

class AdStatsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AdStats
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AdID(self, value):
        """
        Set the value of the AdID input for this Choreo. ((required, string) Search for ads using this ID.)
        """
        super(AdStatsInputSet, self)._set_input('AdID', value)
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        super(AdStatsInputSet, self)._set_input('ClientKey', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) Your AdMob username. Required unless providing a valid Token input.)
        """
        super(AdStatsInputSet, self)._set_input('Email', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) Enter search end date in following format: 2011-09-12)
        """
        super(AdStatsInputSet, self)._set_input('EndDate', value)
    def set_ObjectDimension(self, value):
        """
        Set the value of the ObjectDimension input for this Choreo. ((optional, string) Specify a specific Ad to narrow your search.)
        """
        super(AdStatsInputSet, self)._set_input('ObjectDimension', value)
    def set_OrderBy(self, value):
        """
        Set the value of the OrderBy input for this Choreo. ((optional, string) Order by the number of impressions. Example: [impressions]=asc)
        """
        super(AdStatsInputSet, self)._set_input('OrderBy', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your Admob password. Required unless providing a valid Token input.)
        """
        super(AdStatsInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that your want the response to be in. Accepted values are: xml (the default) and json.)
        """
        super(AdStatsInputSet, self)._set_input('ResponseFormat', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) Enter search start date in following format: 2011-09-12)
        """
        super(AdStatsInputSet, self)._set_input('StartDate', value)
    def set_TimeDimension(self, value):
        """
        Set the value of the TimeDimension input for this Choreo. ((optional, string) Specify whether stats should be grouped by day, week, or month.)
        """
        super(AdStatsInputSet, self)._set_input('TimeDimension', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        super(AdStatsInputSet, self)._set_input('Token', value)

class AdStatsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AdStats Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from AdMob. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        return self._output.get('Token', None)

class AdStatsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AdStatsResultSet(response, path)
