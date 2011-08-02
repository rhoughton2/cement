"""Cement core controller module."""

from zope import interface
from cement2.core import backend, exc

Log = backend.minimal_logger(__name__)

def controller_handler_invariant(obj):
    members = [
        'setup',
        'dispatch',
        ]
    backend.validate_invariants(obj, members)
    
class IControllerHandler(interface.Interface):
    """
    This class defines the Controller Handler Interface.  Classes that 
    implement this handler must provide the methods and attributes defined 
    below.
    
    """
    meta = interface.Attribute('Handler meta-data')
    registered_controllers = interface.Attribute('List of registered controllers')
    interface.invariant(controller_handler_invariant)
    
    def setup(base_app):
        """
        The setup function is after application initialization and after it
        is determined that this controller was requested via command line
        arguments.  Meaning, a controllers setup() function is only called
        right before it's dispatch() function is called to execute a command.
        Must 'setup' the handler object making it ready for the framework
        or the application to make further calls to it.
        
        Required Arguments:
        
            base_app
                The application object, after it has been setup() and run().
                
        Returns: n/a
        
        """
    
    def dispatch(self):
        """
        Reads the application object's data to dispatch a command from this
        controller.  For example, reading self.app.pargs to determine what
        command was passed, and then executing that command function.
                
        """

class CementControllerHandler(object):
    """
    This is an implementation of the IControllerHandler interface, and also
    acts as a base class that application controllers can subclass from.
    
    """
    interface.implements(IControllerHandler)
    class meta:
        type = 'controller'
        label = None # provided in subclass
        
    def __init__(self):
        pass
        
    def setup(self, base_app):
        self.app = base_app
        
        # shortcuts
        self.config = self.app.config
        self.log = self.app.log
        self.pargs = self.app.pargs
        
    def dispatch(self):
        pass