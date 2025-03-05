import dearpygui.dearpygui as dpg
from typing_extensions import Union, Optional, Any
# * Local Imports
#import database

# ! Initializing
dpg.create_context()

# ! Functions
def start() -> None:
    dpg.start_dearpygui()
    dpg.destroy_context()

# ! Window Functions
def load_table(
    sender: Optional[Union[int, str]],
    app_data: Optional[Any],
    table_name: str
):
    print([sender, app_data, table_name])
    if dpg.does_item_exist(f'{table_name}_table'):
        dpg.delete_item(f'{table_name}_table')
    with dpg.table(
        tag=f'{table_name}_table',
        resizable=True,
        policy=dpg.mvTable_SizingStretchProp,
        row_background=True,
        borders_innerH=True,
        borders_outerH=True,
        borders_innerV=True,
        borders_outerV=True,
        parent=f"{table_name}_table_tab",
        before=f"{table_name}_table_update_button"
    ):
        #column_names = [column.name for column in database.metadata.tables[table_name].columns.values()]
        #
        #for column_name in column_names:
        #    dpg.add_table_column(label=column_name)
        #
        #result = database.connection.execute(database.sqla.text(f"SELECT * FROM '{table_name}';"))
        #
        #for row in result:
        #    with dpg.table_row():
        #        for value in row:
        #            dpg.add_text(str(value))
        dpg.add_button(
            label="Update",
            tag=f"{table_name}_table_update_button",
            callback=(lambda sender, app_data: load_table(sender, app_data, 'Races'))
        )

# ! Main Window
with dpg.window(tag="hippodrome_app"):
    with dpg.tab_bar(label="Hippodrome Tabs"):
        with dpg.tab(label="Horses", tag="Horses_table_tab"):
            load_table(None, None, 'Horses')
        with dpg.tab(label="Jockeys", tag="Jockeys_table_tab"):
            load_table(None, None, 'Jockeys')
        with dpg.tab(label="Races", tag="Races_table_tab"):
            load_table(None, None, 'Races')

# ! Settings
dpg.create_viewport(title=f'Dinamic Widgets', width=800, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("hippodrome_app", True)

# ! Start
if __name__ == "__main__":
    start()
