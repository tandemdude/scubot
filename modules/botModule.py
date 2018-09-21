from tinydb import TinyDB, Query
import shlex

class BotModule:
    name = ''  # name of your module

    description = ''  # description of its function

    help_text = ''  # help text for explaining how to do things

    trigger_string = ''  # string to listen for as trigger

    has_background_loop = False

    listen_for_reaction = False

    trigger_on_mention = False

    loaded_modules = []

    admin_modules = ['370934086111330308', '372729159933362177']

    trigger_char = '!'  # char preceding trigger string

    module_version = '0.0.0'

    def __init__(self):
        self.module_db = TinyDB('./modules/databases/' + self.name)

    @staticmethod
    async def parse_subcommand(message_content):
        message_content = shlex.split(message_content)
        subcommands = []
        parameters = {}
        for t in message_content:
            s = t.split("=", 1)
            if s[0] == t:  # Then this must be a subcommand.
                subcommands.append(t)
            else:  # Else, it is a parameter.
                parameters[s[0]] = s[1]
        return subcommands, parameters

    async def parse_command(self, message, client):
        raise NotImplementedError("Parse function not implemented in module:" + self.name)

    async def background_loop(self, client):
        raise NotImplementedError("background_loop function not implemented in module:" + self.name)

    async def on_reaction_add(self, reaction, client, user):
        raise NotImplementedError("on_reaction_add function not implemented in module:" + self.name)

    async def on_reaction_remove(self, reaction, client, user):
        raise NotImplementedError("on_reaction_remove function not implemented in module:" + self.name)
