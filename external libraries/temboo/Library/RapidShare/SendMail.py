# -*- coding: utf-8 -*-

###############################################################################
#
# SendMail
# Send an email that contains a link to a file available on RapidShare.
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

class SendMail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendMail, self).__init__(temboo_session, '/Library/RapidShare/SendMail')


    def new_input_set(self):
        return SendMailInputSet()

    def _make_result_set(self, result, path):
        return SendMailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMailChoreographyExecution(session, exec_id, path)

class SendMailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((required, string) A comment that you want to send with the email)
        """
        super(SendMailInputSet, self)._set_input('Comment', value)
    def set_Email1(self, value):
        """
        Set the value of the Email1 input for this Choreo. ((required, string) The first email address to send to)
        """
        super(SendMailInputSet, self)._set_input('Email1', value)
    def set_Email2(self, value):
        """
        Set the value of the Email2 input for this Choreo. ((optional, string) The second email address to send to)
        """
        super(SendMailInputSet, self)._set_input('Email2', value)
    def set_Email3(self, value):
        """
        Set the value of the Email3 input for this Choreo. ((optional, string) The third email address to send to)
        """
        super(SendMailInputSet, self)._set_input('Email3', value)
    def set_FileID1(self, value):
        """
        Set the value of the FileID1 input for this Choreo. ((required, integer) The id for the file to inform the email recipient about)
        """
        super(SendMailInputSet, self)._set_input('FileID1', value)
    def set_FileName1(self, value):
        """
        Set the value of the FileName1 input for this Choreo. ((required, string) The name of the file to inform the email recipient about)
        """
        super(SendMailInputSet, self)._set_input('FileName1', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        super(SendMailInputSet, self)._set_input('Login', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The senders name)
        """
        super(SendMailInputSet, self)._set_input('Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        super(SendMailInputSet, self)._set_input('Password', value)
    def set_ReplyEmail(self, value):
        """
        Set the value of the ReplyEmail input for this Choreo. ((required, string) The sender reply email address)
        """
        super(SendMailInputSet, self)._set_input('ReplyEmail', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject line for the email)
        """
        super(SendMailInputSet, self)._set_input('Subject', value)

class SendMailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare)
        """
        return self._output.get('Response', None)

class SendMailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendMailResultSet(response, path)
