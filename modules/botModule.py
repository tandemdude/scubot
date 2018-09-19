from tinydb import TinyDB, Query
import re

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
        SUBCOMMAND = ''  # This regex should match every subcommand.
        PARAMETERS = ''  # This regex should capture a parameter only.
        param_dict = {}
        subcommand_list = []
        # Iterable of every subcommand
        for match in re.finditer(SUBCOMMAND, message_content):
            parameter_match = re.match(PARAMETERS, match[0])
            if parameter_match:
                param_dict[parameter_match[0]] = parameter_match[1]
            else:
                subcommand_list.append(match[0])
        return subcommand_list, param_dict

    async def parse_command(self, message, client):
        raise NotImplementedError("Parse function not implemented in module:" + self.name)

    async def background_loop(self, client):
        raise NotImplementedError("background_loop function not implemented in module:" + self.name)

    async def on_reaction_add(self, reaction, client, user):
        raise NotImplementedError("on_reaction_add function not implemented in module:" + self.name)

    async def on_reaction_remove(self, reaction, client, user):
        raise NotImplementedError("on_reaction_remove function not implemented in module:" + self.name)
