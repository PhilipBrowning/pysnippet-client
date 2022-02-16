import os
import json
import glob
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal


class PySnip:
    def __init__(self):
        self.snippets_dir = 'snippets/'

    def get_categories(self):
        print('\n---Getting all categories---\n')
        for root,dirs,files  in os.walk(self.snippets_dir):
            for file in files:
                file_output = file.split('.')
                print(file_output[0])

    def get_categ_snippets(self,category):
        with open('snippets/' + category + ".json", 'r') as f:
            data = json.load(f)    
            for s in data:
                for k,v in s.items():
                    print(k)

    def get_snip_content(self,category,snipname):
        with open('snippets/' + category + ".json", 'r') as f:
            data = json.load(f)    
            for s in data:
                for k,v in s.items():
                    if k == snipname:
                        for value in v:
                            print(value)

    def get_snip_names(self,filename):
        data = json.load(filename)    
        for s in data:
            for k,v in s.items():
                print("\n {}".format(k))

    def get_all_snippets(self):
        for filename in glob.glob(os.path.join(self.snippets_dir, '*.json')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                self.get_snip_names(f)
    def search_snippet(self, snipname):
        for filename in glob.glob(os.path.join(self.snippets_dir, '*.json')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                data = json.load(f)    
                for s in data:
                    for k,v in s.items():
                        if snipname == k:
                            for value in v:
                                print(value)
                        else:
                            pass

    def user_commands(self,command):
        '''Method that will check commands against list of available commands and execute'''
        snip_name = command.split()
        #if "get_command length = 1 assume snippet name and search
        if ("show" not in snip_name):
            self.search_snippet(command)
        #if len > 1 get element 0 and determine if show or add
        #if len > 2 command not found, len == 0 command not found
        commands = ['show','categories','snippets']
        if command == "show snippets":
            print(snip_name)
            self.get_all_snippets()
        elif command == "show categories":
            self.get_categories()
        elif command == "show category snippets":
            category_name = input("Category name: ")
            self.get_categ_snippets(category_name)
        elif command == "show snip":
            snip_name = input("snippet name: ")
            print(snip_name)
        else:
            print("Command not found.")
        return 

    def snip_session(self):
        session = PromptSession()
        user_input = session.prompt('# ')
        #user_input = user_input.split();
        #main menu
        if user_input == 'exit':
            return 0
        else:
            self.user_commands(user_input)
    
    def main_session(self):
        while (True):
            search_session = self.snip_session()
            if search_session == 0:
                break


if __name__ == '__main__':
    mySnip = PySnip()
    #testing methods
    # mySnip.get_categories()
    # print('\n\n')
    # mySnip.get_categ_snippets('javascript') 
    # print('\n\n')
    # mySnip.get_snip_content('javascript', 'if statement')
    mySnip.main_session()