import mysql.connector
from nicegui import ui,app,run
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="app"
)
cr=con.cursor()
@ui.page('/pudhusu')
def pudhusu():
    with ui.grid(columns='25% 25% 50%').classes('w-full gap-1'):
        ui.card().classes('w-full').props('outlined').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);')
        ui.card().classes('w-full').props('outlined').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);')
        ui.card().classes('w-full').props('outlined').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);')

        #     ui.label('This is the pudhusu page!').style('color:white;')
        #     ui.button('amuku', on_click=lambda: ui.navigate.to   ('/'),icon ='phone',color='red')
        #     ui.textarea('This is the pudhusu page!').classes('w-full h-full items-center justify-center').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);')
    # ui.label('This is the pudhusu page!')
    # ui.button('amuku', on_click=lambda: ui.navigate.to   ('/'),icon ='phone')
    # ui.textarea('This is the pudhusu page!').classes('w-full h-full items-center justify-center').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);')

@ui.page('/')
def main():
    ui.add_css('''body {background-image: url("/static/gyomei.jpg");background-size: cover;background-position:top center;}
               .white-input .q-field__label {color: white !important;}
               .white-input .q-field__native {color: white !important;}
               .white-input .q-field__control:before {border-bottom: 1px solid white !important;}
               .white-input .q-field__control:after {border-bottom: 2px solid white !important;}
               .white-input .q-field__append .q-icon {color: white !important;}
               .white-input .q-field__append .q-icon:hover {color: grey !important;}
 ''')
    # ui.label('Hello, World!')
    # ui.button('Click Me', on_click=lambda: ui.notify('Button clicked!'))
    # ui.card().props('outlined').style('max-width: 400px; margin: auto;')
    # with ui.column().classes('w-full h-full items-center justify-center'):
    with ui.card().classes('w-65 max-w-sm mx-auto my-4 items-center').props('outlined').style('background-color: rgba(1, 1, 1, 0.6);text-color: white; backdrop-filter: blur(1px); border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);'): 
           usr= ui.input('Enter your name', placeholder='Name').classes('white-input')
           pwd=  ui.input('Enter your password', placeholder='Password', password=True).classes('white-input')
           ui.button('aluthu', on_click=lambda: ui.navigate.to   ('/pudhusu'),icon ='home',color='red')
           
        #    ui.button('aluthu', on_click=lambda: print(usr.value,pwd.value),icon ='home',color='red')
    
app.add_static_files('/static', 'img')
ui.run(host='0.0.0.0',port=5000)

