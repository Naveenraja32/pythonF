from nicegui import app,run,ui
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="app"
)
 
 
from nicegui import app, ui
# LOGIN PAGE
@ui.page('/')
def loginpage():
    ui.page_title("Login Page")
    with ui.element("div").classes("w-screen h-screen flex items-center justify-center"):
 
        with ui.card().classes("w-[50%] items-center"):
            ui.label("LOGIN").classes("text-3xl font-bold")
 
            username = ui.input(label="Username",placeholder="Enter Username")
 
            password = ui.input(label="Password",placeholder="Enter Password",password=True,password_toggle_button=True)
 
            ui.button("LOGIN",icon="login")
            ui.separator()
            ui.label("Don't have an account?")
 
            ui.button("REGISTER",icon="person_add",on_click=lambda: ui.navigate.to('/register')
)
 
# REGISTER PAGE
@ui.page('/register')
def registerpage():
    ui.page_title("Register Page")
    def save():
        username_value = username.value
        password_value = password.value
 
        cursor = connection.cursor()
        select_query = "SELECT * FROM login WHERE userid = %s"
        cursor.execute(select_query, (username_value,))
        result = cursor.fetchone()
 
        if result:
            ui.notify("Username already exists!")
        else:
            insert_query = "INSERT INTO login (userid, pwd) VALUES (%s, %s)"
            cursor.execute(insert_query, (username_value, password_value))
            connection.commit()
            ui.notify("Registration successful!")
 
        cursor.close()
 
        ui.notify("Registration successful!")
 
        # Redirect to the login page after successful registration
        ui.navigate.to('/')
    with ui.element("div").classes("w-screen h-screen flex items-center justify-center"):
 
        with ui.card().classes("w-[50%] items-center"):
 
            ui.label("REGISTER").classes("text-3xl font-bold")
 
            username = ui.input(label="Username",placeholder="Enter Username")
 
            password = ui.input(label="Password",placeholder="Enter Password",password=True,password_toggle_button=True)
 
            ui.button("REGISTER",icon="person_add",on_click=save)
 
            ui.separator()
 
            ui.label("Already have an account?")
 
            ui.button("BACK TO LOGIN",icon="login",on_click=lambda: ui.navigate.to('/'))
@ui.page('/home')
def homepage():
    ui.page_title("Home Page")
    with ui.element("div").classes( "w-screen h-screen flex items-center justify-center" ):
         with ui.card().classes( "w-[50%] items-center" ):
             ui.label("HOME PAGE").classes( "text-3xl font-bold" )
             ui.label("Login successful!")
             ui.button( "LOGOUT", on_click=lambda: ui.navigate.to('/') )

# Run
ui.run(host='0.0.0.0',port=5000)