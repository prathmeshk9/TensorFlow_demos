import sys
import irc.bot
import irc.strings
from eliza import analyze
 
 
class ElizaBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
 
    def on_welcome(self, connection, event):
        connection.join(self.channel)
 
    def on_pubmsg(self, connection, event):
        args = event.arguments[0].split(":", 1)
        if len(args) > 1 and irc.strings.lower(args[0]) == irc.strings.lower(self.connection.get_nickname()):
            connection.privmsg(self.channel, "{0}: {1}".format(event.source.nick, analyze(args[1]).strip()))
        return
 
 
def main():
    if len(sys.argv) != 4:
        print("Usage: testbot <server[:port]> <channel> <nickname>")
        sys.exit(1)
 
    server_port = sys.argv[1].split(":", 1)
    server = server_port[0]
    if len(server_port) == 2:
        try:
            port = int(server_port[1])
        except ValueError:
            print("Error: bad port.")
            sys.exit(1)
    else:
        port = 6667
 
    channel = sys.argv[2]
    nickname = sys.argv[3]
 
    bot = ElizaBot(channel, nickname, server, port)
    bot.start()
 
 
if __name__ == "__main__":
    main()