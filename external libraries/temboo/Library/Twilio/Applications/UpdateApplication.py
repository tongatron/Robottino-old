# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateApplication
# Updates an existing application within your account.
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

class UpdateApplication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateApplication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateApplication, self).__init__(temboo_session, '/Library/Twilio/Applications/UpdateApplication')


    def new_input_set(self):
        return UpdateApplicationInputSet()

    def _make_result_set(self, result, path):
        return UpdateApplicationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateApplicationChoreographyExecution(session, exec_id, path)

class UpdateApplicationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateApplication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIVersion(self, value):
        """
        Set the value of the APIVersion input for this Choreo. ((optional, string) Requests to this application's URLs will start a new TwiML session with this API version. Either 2010-04-01 or 2008-08-01. Defaults to your account's default API version.)
        """
        super(UpdateApplicationInputSet, self)._set_input('APIVersion', value)
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(UpdateApplicationInputSet, self)._set_input('AccountSID', value)
    def set_ApplicationSID(self, value):
        """
        Set the value of the ApplicationSID input for this Choreo. ((required, string) The id of the application to update.)
        """
        super(UpdateApplicationInputSet, self)._set_input('ApplicationSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(UpdateApplicationInputSet, self)._set_input('AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) A human readable description of the new application. Maximum 64 characters.)
        """
        super(UpdateApplicationInputSet, self)._set_input('FriendlyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(UpdateApplicationInputSet, self)._set_input('ResponseFormat', value)
    def set_SmsFallbackMethod(self, value):
        """
        Set the value of the SmsFallbackMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsFallbackUrl. Must be either GET or POST. Defaults to POST.)
        """
        super(UpdateApplicationInputSet, self)._set_input('SmsFallbackMethod', value)
    def set_SmsFallbackURL(self, value):
        """
        Set the value of the SmsFallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl.)
        """
        super(UpdateApplicationInputSet, self)._set_input('SmsFallbackURL', value)
    def set_SmsMethod(self, value):
        """
        Set the value of the SmsMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsUrl. Must be either GET or POST. Defaults to POST.)
        """
        super(UpdateApplicationInputSet, self)._set_input('SmsMethod', value)
    def set_SmsStatusCallback(self, value):
        """
        Set the value of the SmsStatusCallback input for this Choreo. ((optional, string) Twilio will make a POST request to this URL to pass status parameters (such as sent or failed) to your application.)
        """
        super(UpdateApplicationInputSet, self)._set_input('SmsStatusCallback', value)
    def set_SmsURL(self, value):
        """
        Set the value of the SmsURL input for this Choreo. ((optional, string) The URL that Twilio should request when somebody sends an SMS to a phone number assigned to this application.)
        """
        super(UpdateApplicationInputSet, self)._set_input('SmsURL', value)
    def set_StatusCallbackMethod(self, value):
        """
        Set the value of the StatusCallbackMethod input for this Choreo. ((optional, string) The HTTP method Twilio will use to make requests to the StatusCallback URL. Either GET or POST. Defaults to POST.)
        """
        super(UpdateApplicationInputSet, self)._set_input('StatusCallbackMethod', value)
    def set_StatusCallback(self, value):
        """
        Set the value of the StatusCallback input for this Choreo. ((optional, string) The URL that Twilio will request to pass status parameters (such as call ended) to your application.)
        """
        super(UpdateApplicationInputSet, self)._set_input('StatusCallback', value)
    def set_VoiceApplicationSID(self, value):
        """
        Set the value of the VoiceApplicationSID input for this Choreo. ((optional, string) The 34 character sid of the application Twilio should use to handle phone calls to this number.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceApplicationSID', value)
    def set_VoiceCallerIDLookup(self, value):
        """
        Set the value of the VoiceCallerIDLookup input for this Choreo. ((optional, string) Do a lookup of a caller's name from the CNAM database and post it to your app. Either true or false. Defaults to false.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceCallerIDLookup', value)
    def set_VoiceFallbackMethod(self, value):
        """
        Set the value of the VoiceFallbackMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the VoiceFallbackUrl. Either GET or POST. Defaults to POST.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceFallbackMethod', value)
    def set_VoiceFallbackURL(self, value):
        """
        Set the value of the VoiceFallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs requesting or executing the TwiML at Url.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceFallbackURL', value)
    def set_VoiceMethod(self, value):
        """
        Set the value of the VoiceMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the VoiceUrl. Must be either GET or POST. Defaults to POST.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceMethod', value)
    def set_VoiceURL(self, value):
        """
        Set the value of the VoiceURL input for this Choreo. ((optional, string) The URL that Twilio should request when somebody dials a phone number assigned to this application.)
        """
        super(UpdateApplicationInputSet, self)._set_input('VoiceURL', value)

class UpdateApplicationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateApplication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class UpdateApplicationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateApplicationResultSet(response, path)
