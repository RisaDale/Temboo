# -*- coding: utf-8 -*-

###############################################################################
#
# ClientLoginAuthentication
# Request an authorization token for Google Analytics.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ClientLoginAuthentication(Choreography):

    """
    Create a new instance of the ClientLoginAuthentication Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Analytics/ClientLoginAuthentication')


    def new_input_set(self):
        return ClientLoginAuthenticationInputSet()

    def _make_result_set(self, result, path):
        return ClientLoginAuthenticationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ClientLoginAuthenticationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ClientLoginAuthentication
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ClientLoginAuthenticationInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ClientLoginAuthentication choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ClientLoginAuthenticationResultSet(ResultSet):
        """
        Retrieve the value for the "AuthorizationKey" output from this choreography execution. ((string) The authorization key which is parsed from the Google response.)
        """
        def get_AuthorizationKey(self):
            return self._output.get('AuthorizationKey', None)

class ClientLoginAuthenticationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ClientLoginAuthenticationResultSet(response, path)
