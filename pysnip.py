#!/bin/env python

# author: Philip Browning

#use prompt_toolkit to handle snippet searching
#read json based snippets

#input snippet and convert to json

import os
import json
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal

def search_snip():
    #need try except here 
    print("Search Snippet Category\n")
    snipname =  input("Enter snippet category: ")
    if snipname == 'avail':
        get_categories()
        return _
    
    print("Enter snippet name or all(for all snippet names)") 
    snippet = input("Enter snippet name: ")

    with open('snippets/' + snipname + ".json", 'r') as f:
        data = json.load(f)    
        for s in data:
            x = s
            for k,v in s.items():
                #print(k,v)
                if k == snippet:
                    for value in v:
                        print(value)
                elif snippet == "all":
                    print(k)

def get_categories():
    print('getting all categories')
    snippets_dir = 'snippets/'
    for root,dirs,files  in os.walk(snippets_dir):
        for file in files:
            print(file)

    
def write_json(data, filename):
# pass in json data using top level key ex. snippets
# write to filename provided
    with open(filename,'w') as f:
        json.dump(data,f, indent=4)    

def create_category(name):
    file_path = 'snippets/' + name + ".json"

    if os.path.exists(file_path):
        print("Category currently exists")
    else:
        with open(file_path, 'w') as s:
            snippet_init = []
            json.dump(snippet_init,s, indent=4)

def snippet_input():
    snippet_content = []
    snippet_dict = {}
    snip_name = input("Input unique snippet name: ")
    print("type ctrl d or ctrl z on windows to exit")
    print("Input snippet: ") 
    while(True):
        
        try:
            line = prompt("# ")
    
        except EOFError:
            break
    
        snippet_content.append(line)
        snippet_dict[snip_name] = snippet_content
    return snippet_dict


bindings = KeyBindings()
# key bindings
@bindings.add('c-s')
def _(event):
    " Search when `c-s` is pressed. "
    run_in_terminal(search_snip)

session = PromptSession()

while(True):    
# todo: Add help function, delete snippet function, edit function    
    print("Type in search to search for a snippet, add to add new snippet or avail for available: ")
    text1 = session.prompt('# ', key_bindings = bindings)
        
    if text1 == "add":
        # check if snippet name exists first then open if not
        print("Enter foldername of snippet to be searched by. Example java for java snippets or cooking for recipes etc..\n")
        snip_name = input("Enter folder name: ")
        # if statement to check if 
        snip_save = snippet_input()
        with open('snippets/' + snip_name + ".json", 'r') as s:
            append_snip = json.load(s)
            #temp = append_snip['snippets']
            #temp.append(snip_save)
            append_snip.append(snip_save)
            print(append_snip)
        #print(temp)
        write_json(append_snip,'snippets/' + snip_name + ".json")
        

    elif text1 == "avail":
        get_categories()

    elif text1 == "exit":
        break
    elif text1 == "search":
        print("Enter category name:")
        lang_type =  session.prompt('# ')
        print("Enter snippet name or all(for all snippet names)") 
        snippet = session.prompt('# ')
        #snippet = input("Enter snippet name or all(for all snippet names): ")
        search_snip(lang_type,snippet)
    elif text1 == "new":
        print("Input new snippet category")
        category = input("# ")
        create_category(category)
    else:
        print("Enter a valid choice")
#when creating a snippet check for existing snippet name and prompt for tag and name of snippet
# add config file for things like snippet directory
