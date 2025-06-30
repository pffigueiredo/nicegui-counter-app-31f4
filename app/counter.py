from nicegui import ui

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value
        counter = {'value': 0}
        
        # Create UI elements
        ui.label('Simple Counter').classes('text-2xl font-bold mb-4')
        
        with ui.row().classes('items-center gap-4'):
            ui.button('-', on_click=lambda: decrement_counter()).classes('text-xl').mark('decrement')
            counter_label = ui.label(str(counter['value'])).classes('text-3xl font-mono min-w-16 text-center').mark('counter')
            ui.button('+', on_click=lambda: increment_counter()).classes('text-xl').mark('increment')
        
        def increment_counter():
            counter['value'] += 1
            counter_label.set_text(str(counter['value']))
            
        def decrement_counter():
            counter['value'] -= 1
            counter_label.set_text(str(counter['value']))