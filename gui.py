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
    if sender=="add":
        add_paths(dpg.get_value("kat_a"),dpg.get_value("kat_b"),load_config())
        table_update()
    if sender=="del":
        del_paths(dpg.get_value("kat_a"),dpg.get_value("kat_b"),load_config())
        table_update()

dpg.bind_font(main_font)

def hyperlink(text, address):
    hyperlink = dpg.add_button(
        label=text, callback=lambda: webbrowser.open(address))

    with dpg.tooltip(dpg.last_item()):
        dpg.add_text("Dominik Burnog, Michal Smietana, Adam Lukasik, Hubert Wrobel")

    dpg.bind_item_theme(hyperlink, "hyperlinkTheme")
    dpg.bind_item_font(hyperlink, link_font)

def credits():
     with dpg.group(horizontal=True, tag="credits_tag", parent="Root"):
            dpg.add_spacer(width=(WIDTH - 100) / 2)
            hyperlink("<Credits>", "https://github.com/danteloopz/syncus")

def file_selector():
    with dpg.file_dialog(directory_selector=True, show=False, callback=update_text_input, id="kat_a_selector", width=700 ,height=400):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")

    with dpg.file_dialog(directory_selector=True, show=False, callback=update_text_input, id="kat_b_selector", width=700 ,height=400):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")


def update_text_input(sender, app_data, user_data):
    """Updates the input text field with the selected directory path."""
    receiver_tag = sender[:-9]
    dpg.set_value(receiver_tag, str(app_data["file_path_name"]))
    #print(receiver_tag, app_data["file_path_name"])



def new_dir(label, tag):
    with dpg.group(horizontal=True):
        dpg.add_input_text(label=label, callback=callback, tag=tag)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Przegladaj", callback=lambda: dpg.show_item(tag + "_selector"))

def current_sync():
    with dpg.collapsing_header(label="Aktualne synchronizacje", tag="current"):
        #sync_table()
        pass

def buttons():
    with dpg.group(horizontal=True):
        dpg.add_button(label="Dodaj", callback=callback, tag="add")
        dpg.add_button(label="Usun", callback=callback, tag="del")

def settings():
    with dpg.collapsing_header(label="Ustawienia ogolne"):
        dpg.add_listbox(("Powiel", "Scal"), label="Typ synchronizacji", num_items=2, callback=callback, tag="sync_type")
        dpg.add_slider_int(label="Czestotliwosc synchronizacji (co ile min.)", max_value=60, callback=callback, tag="sync_freq")
        dpg.add_checkbox(label="Wl/Wyl synchronizacje", callback=callback, tag="sync_status")

def change_label():
    dpg.configure_item("my_button", label="New Label")

def table_update():
    config = load_config()
    paths = config["paths"]
    dpg.delete_item("credits_tag")
    dpg.delete_item("pliki", children_only=True)
    dpg.add_table_column(label="src", parent="pliki")
    dpg.add_table_column(label="dest", parent="pliki")
    for rec in paths:
        with dpg.table_row(parent="pliki"):
            for i in range(0, 2):
                dpg.add_text(rec[i])

            dpg.add_text("Newly")
            dpg.add_text("Added")

    credits()

    #if children.__len__() > 0:
    ##    for child in children:
    ##       dpg.delete_item(child)

    #for rec in paths:
    #        with dpg.table_row():
    #            for i in range(0, 2):
    #                dpg.add_text(rec[i])
    
def sync_table():
    config = load_config()
    paths = config["paths"]
    with dpg.table(header_row=True, label="pliki", tag="pliki",parent="current"):
        dpg.add_table_column(label="src")
        dpg.add_table_column(label="dest")
        for rec in paths:
            with dpg.table_row():
                for i in range(0, 2):
                    dpg.add_text(rec[i])
    dpg.add_button(
        label="Update",
        tag="table_update_button",
        callback=table_update
    )
    add_paths("./imgs", "./imgs", config)
    table_update()


