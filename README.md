# REALTIME-EDITOR
COMPANY : CODTECH IT SOLUTIONS
NAME : YENDLURU SAI SRI SINGH
INTERN ID : CT06DM65
DOMAIN : FULL STACK WEB DEVELOPMENT
DURATION : 6 WEEKS
MENTOR : NEELA SANTHOSH KUMAR
#DESCRIPTION :
The core goal of this project was to build a real-time collaborative environment similar to Google Docs, but on a smaller and simpler scale. 
I wanted to understand how socket connections, live data synchronization, and multi-user editing work under the hood.
This helped me improve both my backend and frontend development skills.

For the backend, I used Python with the Flask framework. Flask helped me set up the web server and manage routes. 
To implement real-time features, I integrated Flask-SocketIO, which allows bidirectional communication between the client and server. 
This means that when one user makes a change to the text, the server picks up that event and immediately broadcasts the change to all other connected users.

The frontend was developed using standard HTML and CSS to create a clean and simple interface. 
The user interface includes a text area where users can type and edit content.
I also used JavaScript on the client side to listen for incoming changes from the server and update the text editor in real time.

In addition to live editing, I included a simple SQLite database (documents.db) to store document content.
This ensures that any edits made are not lost when the server is restarted. 
When users open the editor, the last saved version of the document is loaded from the database.
Any new changes are also saved automatically as users type.
#OUTPUT :

