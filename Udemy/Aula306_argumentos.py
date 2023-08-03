# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
'''configurando o sistema como 
{
  "window.zoomLevel": 2,
  "editor.fontSize": 24,
  "editor.hover.enabled": true,
  "workbench.startupEditor": "none",
  "explorer.compactFolders": false,
  "terminal.integrated.fontSize": 24,
  "editor.rulers": [80, 120],
  "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
  "workbench.iconTheme": "material-icon-theme",
  "code-runner.executorMap": {
    "python": "clear ; python -u"
  },
  "code-runner.runInTerminal": true,
  "code-runner.ignoreSelection": true,
  "editor.fontFamily": "'Fira Code', Consolas, 'Dank Mono', 'Source Code Pro', 'Fira Code', Menlo, 'Inconsolata', 'Droid Sans Mono', 'DejaVu Sans Mono', 'Ubuntu Mono', 'Courier New', Courier, Monaco, monospace",
  "terminal.integrated.fontFamily": "",
  "editor.fontLigatures": false,
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4,

    '''