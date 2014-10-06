# -*- coding: utf-8 -*-

###############################################################################
#
# LogActivity
# Log a new activity for a particular date.
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

class LogActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LogActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LogActivity, self).__init__(temboo_session, '/Library/Fitbit/Activities/LogActivity')


    def new_input_set(self):
        return LogActivityInputSet()

    def _make_result_set(self, result, path):
        return LogActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogActivityChoreographyExecution(session, exec_id, path)

class LogActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LogActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(LogActivityInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(LogActivityInputSet, self)._set_input('AccessToken', value)
    def set_ActivityID(self, value):
        """
        Set the value of the ActivityID input for this Choreo. ((conditional, integer) This can be the id of the activity, directory activity, or intensity level activity.)
        """
        super(LogActivityInputSet, self)._set_input('ActivityID', value)
    def set_ActivityName(self, value):
        """
        Set the value of the ActivityName input for this Choreo. ((conditional, string) Custom activity name; either activityId or activityName should be provided.)
        """
        super(LogActivityInputSet, self)._set_input('ActivityName', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(LogActivityInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(LogActivityInputSet, self)._set_input('ConsumerSecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date that corresponds with the new log entry (in the format yyyy-MM-dd).)
        """
        super(LogActivityInputSet, self)._set_input('Date', value)
    def set_DistanceUnit(self, value):
        """
        Set the value of the DistanceUnit input for this Choreo. ((conditional, string) Corresponds with the Distance parameter (i.e. Mile). See Choreo documentation for links to unit charts.)
        """
        super(LogActivityInputSet, self)._set_input('DistanceUnit', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((conditional, decimal) The activity distance. Used when activityId corresponds to 'Running'  or 'Walking' for example.)
        """
        super(LogActivityInputSet, self)._set_input('Distance', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((required, integer) The duration of the activity in milliseconds.)
        """
        super(LogActivityInputSet, self)._set_input('Duration', value)
    def set_ManualCalories(self, value):
        """
        Set the value of the ManualCalories input for this Choreo. ((conditional, integer) The amount of calories defined manually; required when using the ActivityName parameter, otherwise optional.)
        """
        super(LogActivityInputSet, self)._set_input('ManualCalories', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(LogActivityInputSet, self)._set_input('ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((required, string) The hour and minutes for the start of the activity formatted like HH:mm.)
        """
        super(LogActivityInputSet, self)._set_input('StartTime', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(LogActivityInputSet, self)._set_input('UserID', value)

class LogActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LogActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class LogActivityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LogActivityResultSet(response, path)
