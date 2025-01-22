import dearpygui.dearpygui as dpg
from themes import setup_themes
from functions import *
import webbrowser

WIDTH = 1000 
HEIGHT = 600 
LOG_DIR = "./log"
ICON = "./imgs/appicon.ico"
LOGO = "./imgs/logo.jpg"

dpg.create_context()
setup_themes()

def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

def hyperlink(text, address):
    hyperlink = dpg.add_button(
        label=text, callback=lambda: webbrowser.open(address))
    dpg.bind_item_theme(hyperlink, "hyperlinkTheme")
    #dpg.bind_item_font(hyperlink, link_font)

def logo():
    width, height, channels, data = dpg.load_image(LOGO)
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="logo")
    dpg.add_image("logo")

def credits():
    dpg.add_text("Credits")
    with dpg.tooltip(dpg.last_item()):
        dpg.add_text("Dominik Burnog, Michal Smietana, Adam Lukasik, Hubert Wrobel")

def file_selector():
    with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", width=700 ,height=400):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")

def new_dir(label):
    with dpg.group(horizontal=True):
        dpg.add_input_text(label=label, callback=callback)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Przegladaj", callback=lambda: dpg.show_item("file_dialog_id"))

def current_sync():
    with dpg.collapsing_header(label="Aktualne synchronizacje"):
         with dpg.tree_node(label="Help (READ ME FIRST)"):
             pass

def settings():
    dpg.add_listbox(("Powiel", "Scal"), label="Typ synchronizacji", num_items=2, callback=callback)
    dpg.add_slider_int(label="Czestotliwosc synchronizacji (co ile min.)", max_value=60, callback=callback)
    dpg.add_checkbox(label="Wl/Wyl synchronizacje", callback=callback)
    dpg.add_button(label="Dodaj", callback=callback)

def advanced_settings():
    with dpg.collapsing_header(label="Ustawienia zaawansowane"):
         with dpg.tree_node(label="Help (READ ME FIRST)"):
            dpg.add_text("These topics are for advanced users.", bullet=True)
            dpg.add_text("Make sure you know what you are doing.", bullet=True) 
       
