#Instruction of chatroom

## Notice!! some IME may not type other languages(except English) in Textedit.

## As you can see there are total four .py files and one .ui file,

### Chatroom.ui is the file for editing the GUI with qtdesigner
    
### client.py is the client of the chatroom with GUI.
    
### client_ui.py is the GUI setting of the client.py
    
### client_shell.py is the client of the chatroom without GUI
    
### server.py is the server of the chatroom
    
---
### The tips of development
You can import the chatroom.ui in your own qtdesiner, and export a new client_ui.py,
then just COPY-PASTE the Ui_MainWindow or others classes that it might be used in 
the client.py, the tips above can help you develop well.

The client.py is all base on client_shell.py, 
If you want to design other UI, you can use the client.py to help you develop.


