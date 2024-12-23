This prototype is developed and debugged using Visual Studio Code with the extension Python and Python Debugger.

After downloading and opening the prototype folder, ensure everything is saved

To start the program: 
    Run main.py file

Troubleshooting: 
        1. If there is ModuleNotFoundError, check the import names in files involved
        2. Manually install tkcalendar by running "pip install tkcalendar" in terminal (Though it should download automatically)
        3. Config fixing (To-Do List Manager):
        
            a. Do not delete or edit ToDoConfig.txt, however, if it is deleted or edited, the prototype can fix it up to the range of 10000, "ToDo.fixConfig()"

            b. If you want to directly edit a ToDo.txt file, do not edit the first line which is an id, doing so may result in a glitch where file will keep reappearing after you deleted it, to fix this, ensure the id on the first line matches the number of the file name. E.g. If the id on the first line of the file is 80, then the filename should be ToDo80.txt

        4. Display considerations (To-Do List Manager):
            a. The GUI is designed for a display with the screen size of approximately 56cmx30cm, there is a create button on the bottom right of the screen that may not appear if the height of the device is too small

            b. To adjust this, go to Gui.py, comment out line 200 and uncomment line 201. You can adjust the y value accordingly to make the button higher or lower.



