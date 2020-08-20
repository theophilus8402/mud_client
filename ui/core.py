
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import SearchToolbar, TextArea


def get_char_stat(prompt_info, stat_type):
    char_stats = prompt_info.get("charstats", [])
    for stat in char_stats:
        if stat.startswith(stat_type):
            s_type, amount = stat.split(" ")
            return amount
    return "???"


def create_prompt_text(prompt_info):
    hp = prompt_info.get("hp", "???")
    max_hp = prompt_info.get("maxhp", "???")
    mp = prompt_info.get("mp", "???")
    max_mp = prompt_info.get("maxmp", "???")
    rage = get_char_stat(prompt_info, "Rage")
    bleed = get_char_stat(prompt_info, "Bleed")
    return f"HP:{hp}/{max_hp} MP:{mp}/{max_mp} Rage:{rage} Bleed:{bleed}"


def update_prompt_info(prompt_info):
    prompt_line.text = create_prompt_text(prompt_info)


search_field = SearchToolbar()  # For reverse search.

input_field = TextArea(
    height=1,
    prompt=">>> ",
    style="class:input-field",
    multiline=False,
    wrap_lines=False,
    search_field=search_field,
)

afflictions_line = TextArea(height=1, style="class:output-field", text="afflictions")
frenemies_line = TextArea(height=1, style="class:output-field", text="frenemies")
prompt_line = TextArea(height=1, style="class:output-field", text=create_prompt_text({}))

container = HSplit(
    [
        afflictions_line,
        frenemies_line,
        prompt_line,
        input_field,
        search_field,
    ]
)

# The key bindings.
kb = KeyBindings()

@kb.add("c-c")
@kb.add("c-q")
def _(event):
    " Pressing Ctrl-Q or Ctrl-C will exit the user interface. "
    event.app.exit()

# Style.
style = Style(
    [
        ("output-field", "bg:#000044 #ffffff"),
        ("input-field", "bg:#000000 #ffffff"),
        ("line", "#004400"),
    ]
)

application = Application(
    layout=Layout(container, focused_element=input_field),
    key_bindings=kb,
    style=style,
    mouse_support=True,
    full_screen=True,
)
