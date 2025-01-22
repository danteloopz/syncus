from gui import *
import argparse

def ok(mess):
    print(OKGREEN + "[+] " + mess + ENDC)

def warn(mess):
    print(WARNING + "[!] " + mess + ENDC)

def fail(mess):
    print(FAILRED + "[-] " + mess + ENDC)

def run_GUI():
    ok("GUI version started")
    with dpg.window(tag="Root"):
        pass
    dpg.set_primary_window("Root", True)
    icon = "./imgs/appicon.ico"
    dpg.create_viewport(title='Syncus', width=WIDTH, height=HEIGHT, resizable = False, small_icon=icon, large_icon=icon)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def run_CLI():
    # Set terminal ANSI code colors
    ok("CLI version started")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Choose between CLI and GUI version of the app.")
    parser.add_argument(
        '--cli', 
        action='store_true', 
        help="Run the CLI version of the app (default is GUI)"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.cli:
        run_CLI()
    else:
        run_GUI()
