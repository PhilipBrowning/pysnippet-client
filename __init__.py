from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import pysnip_class

if __name__ == '__main__':
    run_snip = pysnip_class.PySnip()
    while (True):
        # todo: history on wsl is not working so using history file for now
        session = PromptSession(history=FileHistory('./.pysnip_history'))
        print("Enter command or help for list of commands.")
        user_input = session.prompt('# ')
        #main menu
        if user_input == 'exit':
            break
        else:
            run_snip.user_commands(user_input)