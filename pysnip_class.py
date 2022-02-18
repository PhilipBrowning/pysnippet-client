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
        self.main_commands = {'search':'search for specific snippet','show all categories':'show all groups of snippet types'
            ,'show all snippets':'show all text snippets','add':'Add new snippet','upload':'To be added'}

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
        found = False
        for filename in glob.glob(os.path.join(self.snippets_dir, '*.json')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                data = json.load(f)    
                for s in data:
                    for k,v in s.items():
                        if snipname == k:
                            for value in v:
                                print(value)
                                found = True
        if not found:
            print("Snippet not found")

    def user_commands(self,command):
        '''Method that will check commands against list of available commands and execute'''
        #snip_name = command.split()
        #search snippet name if show not in command
        if (command == "search"):
            snip_name = input("Enter snippet name: ")
            self.search_snippet(snip_name)
        if (command == "help"):
            print("The following commands are available.")
            for item in self.main_commands:
                print("\n{} : {}\n".format(item,self.main_commands[item]))
        if command == "show all snippets":
            self.get_all_snippets()
        elif command == "show all categories":
            self.get_categories()
        elif command == "show category snippets":
            category_name = input("Category name: ")
            self.get_categ_snippets(category_name)
        else:
            return

    def add_snippet(self):
        pass

if __name__ == '__main__':
    mySnip = PySnip()
    #testing methods
    # mySnip.get_categories()
    # print('\n\n')
    # mySnip.get_categ_snippets('javascript') 
    # print('\n\n')
    # mySnip.get_snip_content('javascript', 'if statement')
    mySnip.main_session()