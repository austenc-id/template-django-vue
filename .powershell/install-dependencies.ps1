Function pyenv {
	param (
		[Parameter()]
		[string] $action
	)
	if ('new' -eq $action) {
		"`nCreating Python Virtual Environment`n"
		python -m venv pyenv
		}
	pyenv\Scripts\Activate.ps1
	which pip
}

$path = Split-Path $PSScriptRoot -Parent
cd $path
cd server

pyenv new
"`nInstalling Packages`n"
pip install -r packages.txt
"`nSaving Package Versions`n"
pip freeze > requirements.txt
cd ..
cd client
"`nInstalling Node Packages`n"
npm install
cd ..