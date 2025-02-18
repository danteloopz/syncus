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

with dpg.font_registry():
    logo_font = dpg.add_font(
        "./fonts/bevan/Bevan-Regular.ttf", 50)
    main_font = dpg.add_font("./fonts/Noto_Sans_Mono/static/NotoSansMono_Condensed-Black.ttf", 18)
        #"./fonts/libre_franklin/LibreFranklin-Black.ttf", 15)
    keyboard_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-Bold.ttf", 20)
    keyboard_action_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-SemiBold.ttf", 15)
    link_font = dpg.add_font(
        "./fonts/libre_franklin/LibreFranklin-SemiBold.ttf", 15)


def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

dpg.bind_font(main_font)

def hyperlink(text, address):
    hyperlink = dpg.add_button(
        label=text, callback=lambda: webbrowser.open(address))

    with dpg.tooltip(dpg.last_item()):
        dpg.add_text("Dominik Burnog, Michal Smietana, Adam Lukasik, Hubert Wrobel")

    dpg.bind_item_theme(hyperlink, "hyperlinkTheme")
    dpg.bind_item_font(hyperlink, link_font)

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
        pass

def settings():
    with dpg.group(horizontal=True):
        dpg.add_button(label="Dodaj", callback=callback)
        dpg.add_button(label="Usun", callback=callback)

def advanced_settings():
    with dpg.collapsing_header(label="Ustawienia ogolne"):
        dpg.add_listbox(("Powiel", "Scal"), label="Typ synchronizacji", num_items=2, callback=callback)
        dpg.add_slider_int(label="Czestotliwosc synchronizacji (co ile min.)", max_value=60, callback=callback)
        dpg.add_checkbox(label="Wl/Wyl synchronizacje", callback=callback)
       
