#basic powershell script to activate python virtual environment. Assumes dir name is venv in current directory
$command = '.\venv\Scripts\activate.ps1'
iex $command
