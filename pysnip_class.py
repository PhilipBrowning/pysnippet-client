import os
import json
import glob
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit import Application
from prompt_toolkit.widgets import Box, Frame, TextArea, Label
from prompt_toolkit.layout import Layout


class PySnip:
    def __init__(self):
        self.snippets_dir = 'snippets/'
        self.main_commands = {'search':'search for specific snippet',
            'search category':'search by category',
            'show all categories':'show all groups of snippet types',
            'show all snippets':'show all text snippets',
            'show all snippets in category':'show all snippet names in category',
            'add':'Add new snippet',
            'add category':'Add new category',
            'sync':'To be added'}

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

    def get_snip_names(self,filename):
        data = json.load(filename)    
        for s in data:
            for k,v in s.items():
                print("\n\n {}".format(k))

    def get_all_snippets(self):
        for filename in glob.glob(os.path.join(self.snippets_dir, '*.json')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                self.get_snip_names(f)

    def search_snippet(self,snipname):
        found = False
        if snipname == "all":
            self.get_all_snippets()
            found = True
        else:
            for filename in glob.glob(os.path.join(self.snippets_dir, '*.json')):
                with open(os.path.join(os.getcwd(), filename), 'r') as f:
                    data = json.load(f)    
                    for s in data:
                        for k,v in s.items():
                            if snipname == k:
                                for value in v:
                                    print("\n{}".format(value))
                                    found = True
                                    return
        if not found:
            print("Snippet not found")
            return

    def user_commands(self,command):
        '''Method that will check commands against list of available commands and execute'''
        #snip_name = command.split()
        #search snippet name if show not in command
        if (command == "search"):
            snipname = prompt("Enter snippet name or all for all snippets: ")
            self.search_snippet(snipname)
        if (command == "help"):
            print("The following commands are available.")
            for item in self.main_commands:
                print("\n{} : {}\n".format(item,self.main_commands[item]))
        if (command == "add"):
            self.add_snippet()
        if (command == "add category"):
            self.create_category()
        if (command == "delete snippet"):
            self.del_snippet()
        if command == "show all snippets":
            self.get_all_snippets()
        elif command == "show all categories":
            self.get_categories()
        elif command == "show snippets in category":
            category_name = input("Category name: ")
            self.get_categ_snippets(category_name)
        else:
            return

    def snippet_input(self):
        snippet_content = []
        snippet_dict = {}
        snip_name = input("Input unique snippet name: ")
        print("Press ctrl d to exit and save")
        print("If pasting multiline snippets, press esc then enter then ctrl d to exit and save")
        print("Input snippet: ") 
        while(True):
            try:
                line = prompt("# ", multiline=True)
        
            except EOFError:
                break
        
            snippet_content.append(line)
            snippet_dict[snip_name] = snippet_content
        return snippet_dict

    def add_snippet(self):
        #get categories and add if category exist. if not create_category and append ?
        snip_name = input("Enter category to save snippet to: ")
        snip_save = self.snippet_input()
        #load file append snippet dict to current file
        with open('snippets/' + snip_name + ".json", 'r') as s:
            append_snip = json.load(s)
            append_snip.append(snip_save)
        with open('snippets/' + snip_name + ".json",'w') as f:
            json.dump(append_snip,f, indent=4)

    def create_category(self):
        cat_name = input("Input new Category name: ")
        file_path = self.snippets_dir + cat_name + ".json"
    
        if os.path.exists(file_path):
            print("Category currently exists")
        else:
            with open(file_path, 'w') as s:
                snippet_init = []
                json.dump(snippet_init,s, indent=4)

    def write_json(data, filename):
        # pass in json data to write to file
        try:
            with open(filename,'w') as f:
                json.dump(data,f, indent=4) 
        except:
            print("File error while writing snippet to file!")

    def del_snippet(self):
        categ_name = input("Input category name: ")
        snip_name = input("Input snippet name to delete: ")
        with open('snippets/' + categ_name + ".json", 'r') as s:
            data = json.load(s) 
        for snip in data:
            snip.pop(snip_name, None)
        with open('snippets/' + categ_name + ".json", 'w') as s:
            data = json.dump(data, s)
    
    def update_snippet(self):    
        categ_name = input("Input category name: ")
        snip_name = input("Input snippet name to update: ")
        kb = KeyBindings()
        with open('snippets/' + categ_name + ".json", 'r') as s:
            data = json.load(s) 
            print(data)
            for x in data:
                for k,v in x.items():
                    if k == snip_name:
                        root_container = Box(
                            Frame(
                                TextArea(
                                    text= "{}".format("".join(v)),
                                    width=50,
                                    height=20,
                                )
                            ),
                        )
        layout = Layout(container=root_container) 
        @kb.add('c-q')
        def exit_(event):
            event.app.exit()
        #app = Application(key_bindings=kb, full_screen=True)
        Application(layout=layout, key_bindings=kb, full_screen=True).run()
        #app.run()


         

if __name__ == '__main__':
    mySnip = PySnip()
    mySnip.update_snippet()
    #testing methods
    # mySnip.get_categories()
    # print('\n\n')
    # mySnip.get_categ_snippets('javascript') 
    # print('\n\n')
    # mySnip.get_snip_content('javascript', 'if statement')
    #mySnip.get_all_snippets()