# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccountBalance
# Retrieves the current balance of your account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAccountBalance(Choreography):

    """
    Create a new instance of the GetAccountBalance Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetAccountBalance')


    def new_input_set(self):
        return GetAccountBalanceInputSet()

    def _make_result_set(self, result, path):
        return GetAccountBalanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountBalanceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAccountBalance
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAccountBalanceInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) The endpoint should be fps.sandbox.amazonaws.com when accessing the sandbox. Defaults to production setting:  fps.amazonaws.com.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)


"""
A ResultSet with methods tailored to the values returned by the GetAccountBalance choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAccountBalanceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAccountBalanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountBalanceResultSet(response, path)
