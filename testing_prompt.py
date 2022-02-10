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

    def search_snip(self):
    #need try except here 
        print("Search Snippet Category\n")
        snipname =  input("Enter snippet category: ")
        if snipname == 'avail':
            self.get_categories()
            return
        
        print("Enter snippet name or all(for all snippet names)") 
        snippet = input("Enter snippet name: ")

        with open('snippets/' + snipname + ".json", 'r') as f:
            data = json.load(f)    
            for s in data:
                for k,v in s.items():
                    if k == snippet:
                        for value in v:
                            print(value)
                    elif snippet == "all":
                        print(k)
    
    def snip_session(self):
        session = PromptSession()
        print("Type in search to search for a snippet, add to add new snippet or avail for available: ")
        user_input = session.prompt('# ')
        user_input = user_input.split();
        print(user_input)
        #temp code to break out of session
        if user_input[0] == 'exit':
            return 0
    
    def main_session(self):
        while(True):
            search_session = self.snip_session()
            if search_session == 0:
                break


if __name__ == '__main__':
    mySnip = PySnip()
    mySnip.get_categories()
    print('\n\n')
    mySnip.get_categ_snippets('javascript') 
    print('\n\n')
    mySnip.get_snip_content('javascript', 'if statement')
    mySnip.main_session()