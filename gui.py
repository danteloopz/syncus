import dearpygui.dearpygui as dpg
from themes import setup_themes
from functions import *
import webbrowser

WIDTH = 550
HEIGHT = 800

dpg.create_context()
setup_themes()

def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

def hyperlink(text, address):
    hyperlink = dpg.add_button(
        label=text, callback=lambda: webbrowser.open(address))
    dpg.bind_item_theme(hyperlink, "hyperlinkTheme")
    dpg.bind_item_font(hyperlink, link_font)

def run_GUI():

    width, height, channels, data = dpg.load_image("logo.jpg")
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")


    with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", width=700 ,height=400):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")
    
    
    with dpg.window(tag="Primary Window", label="Main Window", width=1000, height=600, no_move=True, no_title_bar=True, no_resize=True):
        with dpg.group(horizontal=True):
            dpg.add_image("texture_tag")
            #dpg.add_loading_indicator(circle_count=4)
            with dpg.group():
                dpg.add_text(f'Syncus - najlepsza aplikacja do synchronizacji plików. Wersja: ({get_syncus_version()})')

        with dpg.collapsing_header(label="Aktualne synchronizacje"):
            pass

                
        with dpg.group(horizontal=True):
            dpg.add_input_text(label="Katalog A", callback=callback)
            with dpg.group(horizontal=True):
                dpg.add_button(label="Przegladaj", callback=lambda: dpg.show_item("file_dialog_id"))

        with dpg.group(horizontal=True):
            dpg.add_input_text(label="Katalog B", callback=callback)
            with dpg.group(horizontal=True):
                dpg.add_button(label="Przegladaj", callback=lambda: dpg.show_item("file_dialog_id"))

        dpg.add_listbox(("Powiel", "Scal"), label="Typ synchronizacji", num_items=3, callback=callback)
        dpg.add_slider_int(label="Czestotliwosc synchronizacji (ile razy na sek.)", max_value=60, callback=callback)

        dpg.add_checkbox(label="Wl/Wyl synchronizacje", callback=callback)
        dpg.add_button(label="Dodaj", callback=callback)


        
    
        with dpg.collapsing_header(label="Ustawienia zaawansowane"):
                with dpg.tree_node(label="Help (READ ME FIRST)"):
                    dpg.add_text("These topics are for advanced users.", bullet=True)
                    dpg.add_text("Make sure you know what you are doing.", bullet=True) #Can we remove this?
    
        dpg.add_text("Credits")
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("Dominik Burnog, Michal Smietana, Adam Lukasik, Hubert Wrobel")
