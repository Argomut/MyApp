This prototype is developed and debugged using Visual Studio Code with the extension Python and Python Debugger.

After downloading and opening the prototype folder, ensure everything is saved

To start the program: 
    Run main.py file

Troubleshooting:
    If the IDE glitched and a ModuleNotFoundError appear: 
        1. go to main.py, line 9 and 10, delete the imports and manually retype the imports "from MyClasses.Gui import Gui" & "from MyClasses.ToDo import ToDo"
        2. go to Gui.py, line 2, 3, and 4,  delete the imports and manually retype the imports "from MyClasses.Gui import Gui", "from MyClasses.ToDo import ToDo", "from MyClasses.ProgressBars import ProgressBars" & "from MyClasses.pmdr import PomodoroTimer"
        3. in the terminal, run "pip install tkcalendar"

Navigation
    There is a navigation bar with 3 buttons to navigate to each of the module. The default module in the To-Do List Manager Module, you can click on the other to navigate to pomodoro module/gpa module. You can also click on the button of the current module to refresh the page.

To-Do List Manager Module -- Elden:
    How to use:
        1. Create: Click on the square blue button on the bottom right corner. It will bring you to another page where you can edit the contents of your tasks
        
            a. To edit progress bar, click on the progress bar itself or the "update progress" button. A popup will appear and you can enter the percentage of your current progress from 1-100
               It can accept a number below 0 or higher than 100, however, it will set it to 0 if the input is a negative number or set it to 100 if the input is higher than 100
               It can accept a decimal number, it will round out the number using Bankers's rounding (even number with .5 will go down while odd number with .5 will go up)
               It will reject strings, a error message will popup if a string is entered
               After setting the progress, press the "update progress" to save the change or close the popup to cancel the change
            
            b. To edit the task's title, click on the title field, default value is untitled. In the field you can type in your own title. 
                The field will automatically add a new line when the width limit is reached (unless it is copied and paste, then click any keys to update the lines)
                Press enter to exit the field save and the title
            
            c. To edit the deadline, click on the "deadline" button, a calendar will pop up for you to select the task's deadline
                The calendar will reject any dates that are before current's date
                After choosing a date, click the "select" button to save the deadline

            d. To edit description, click on the description field and type in the task's description
                To add a new line, press alt + enter
                Press enter to exit the field and save the description
            
            e. To go back to main To-Do List page, click the up button on the top left corner.

        2. Read: The To-Do List Manager Module will by default display all the tasks 
            a. Sorting: Pinned tasks are displayed at the top while unpinned tasks are displayed at the bottom. The tasks are also sorted according to deadline, the closer the deadline, the higher the task. E.g. Pinned task with closer deadline will be on top of pinned task with further deadline which will be above unpinned task with upcoming deadline
            
            b. Filtering: enter a keyword on search bar, then press enter or click on the "search" button.
                Only tasks with titles that contain the keyword would be displayed
                Uppercase or lowercase doesn't matter
                Leading and trailing white spaces doesn't matter
                To display all the tasks again, insert empty string ("") into the search bar and submit
            
            c. Refreshing: You can refresh the page by entering empty string ("") into the search bar and submit or press the To-Do List button in the navigation bar at the bottom
        
        3. Update:
            a. You can pin or unpin a task by pressing the task's respective pin icon next to the trash icon. After refreshing the page, the newly pinned/unpinned task will be sorted accordingly

            b. To edit the contents of a task, click on the respective task (anything including background in the box other than the pin & trash icon), then you can perform the actions like creating a new task

        4. Delete:
            a. Click on the respective trash icon of task you want to delete

            b. The prototype is not advanced enough to undo deletion, so once you deleted it, the file is gone forever

        5. Config fixing
            a. Do not delete or edit ToDoConfig.txt, however, if it is deleted or edited, the prototype can fix it up to the range of 10000

            b. If you want to directly edit a ToDo.txt file, do not edit the first line which is an id, doing so may result in a glitch where file will keep reappearing after you deleted it, to fix this, ensure the id on the first line matches the number of the file name. E.g. If the id on the first line of the file is 80, then the filename should be ToDo80.txt


Pomodoro Timer Module -- Wong GuanHao:


GPA Calculator -- Pang Qian Fu:



