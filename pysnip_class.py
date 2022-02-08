import os
import json
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal


class PySnip:
    def __init__(self):
        self.snippets_dir = 'snippets/'

    def get_categories(self):
        print('\ngetting all categories\n')
        for root,dirs,files  in os.walk(self.snippets_dir):
            for file in files:
                print(file)