from gui import *
import argparse

def run_GUI():
    ok("GUI version started")
    file_selector()
    with dpg.window(tag="Root"):
        dpg.add_spacer(height=10)
        new_dir("Katalog A")
        new_dir("Katalog B")
        settings()
        advanced_settings()
        current_sync()
        dpg.add_spacer(height=5), dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=(WIDTH - 100) / 2)
            hyperlink("<Credits>", "https://github.com/danteloopz/syncus")



    dpg.set_primary_window("Root", True)
    dpg.create_viewport(title='Syncus - najlepsza aplikacja do synchronizacji plików', width=WIDTH, height=HEIGHT, small_icon=ICON, large_icon=ICON)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def run_CLI():
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

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(filename=os.path.join(LOG_DIR, "syncus.log"), level=logging.INFO)
    log.info("started syncus")
    config = load_config()
    sync_start(config)

    if args.cli:
        run_CLI()
    else:
        run_GUI()
    