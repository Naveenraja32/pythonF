from nicegui import ui,app,run
@ui.page('/pudhusu')
def pudhusu():
    ui.label('This is the pudhusu page!')
    ui.button('amuku', on_click=lambda: ui.navigate.to   ('/'))
    
@ui.page('/')
def main():
    ui.label('Hello, World!')
    # ui.button('Click Me', on_click=lambda: ui.notify('Button clicked!'))
    ui.button('aluthu', on_click=lambda: ui.navigate.to   ('/pudhusu'))
    
    
ui.run(host='0.0.0.0',port=5000)

