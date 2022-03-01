from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.basic import load_basic_bindings
from prompt_toolkit.application import run_in_terminal
import argparse
import pysnip_class

bindings = KeyBindings()
# key bindings
# @bindings.add('c-s')
# def _(event):
#     " Search when `c-s` is pressed. "
#     event.app.current_buffer.insert_text("search")
# @bindings.add('c-r')
# def _(event):
#     event.app.run(run_snip.user_commands("search"))
#     return

if __name__ == '__main__':
    run_snip = pysnip_class.PySnip()

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--search',help="Add snippet name as argument to search for", type=str)
    parser.add_argument('--allsnippets',help="Output all snippets",action='store_true')
    parser.add_argument('--addsnippet',help="Add a new snippet",action='store_true')
    parser.add_argument('-m','--menu',help="Run menu based input",action='store_true')

    args = parser.parse_args()
    if args.search:
        run_snip.search_snippet(args.search)
    elif args.allsnippets:
        run_snip.get_all_snippets()
    elif args.addsnippet:
        run_snip.add_snippet()
    elif args.menu:
        while True:
            # todo: history on wsl is not working so using history file for now
            session = PromptSession(history=FileHistory('./.pysnip_history'))
            print("Enter command or help for list of commands.")
            user_input = session.prompt('# ',  key_bindings=bindings)
            #main menu
            if user_input == 'exit':
                break
            else:
                run_snip.user_commands(user_input)
    else:
        print("Please pass a valid option or --help")