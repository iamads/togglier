import sys
import logging
import getpass
from optparse import OptionParser
import zmq
import sleekxmpp
from xmpp_settings import xmpp_settings


context = zmq.Context()

# Define the socket using the "Context" command
socket = context.socket(zmq.PAIR)
socket.bind("tcp://127.0.0.1:5696")

if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding

    setdefaultencoding('utf8')
else:
    raw_input = input


class SendMsgBot(sleekxmpp.ClientXMPP):
    """
    A basic SleekXMPP bot that will log in, 
    send multiple message to diferent bot
    """

    def __init__(self, jid, password, recipient, message):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # The message we wish to send, and the JID that will receive it.
        self.recipient = recipient
        self.msg = message
        """
        The session_start event will be triggered when the 
        bot establishes its connection with the server and 
        the XML streams are ready for use. We want to listen 
        for this event so that we can initialize our roster.
        """
        self.add_event_handler("session_start", self.start, threaded=True)

    def start(self, event):
        """
        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.
        """
        self.send_presence()
        self.get_roster()

        """
        An empty dictionary. The session_start
        event does not provide any additional data.
        """
        while True:
            # socket connection
            from_webapp = str(socket.recv())

            if not from_webapp:
                pass
            else:
                self.recepient, self.message = from_webapp.split()
                self.send_message(mto=self.recepient,
                                  mbody=self.message,
                                  mtype='chat')


if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")
    optp.add_option("-t", "--to", dest="to",
                    help="JID to send the message to")
    optp.add_option("-m", "--message", dest="message",
                    help="message to send")

    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    if opts.jid is None:
        opts.jid = raw_input("Username: ")
    if opts.password is None:
        opts.password = getpass.getpass("Password: ")

    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    xmpp = SendMsgBot(opts.jid, opts.password, opts.to, opts.message)
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    # If you are working with an OpenFire server, you may need
    # to adjust the SSL version used:
    # xmpp.ssl_version = ssl.PROTOCOL_SSLv3

    # If you want to verify the SSL certificates offered by a server:
    # xmpp.ca_certs = "path/to/ca/cert"

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect((xmpp_settings.xmpp_ip, 5222)):
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")
        
