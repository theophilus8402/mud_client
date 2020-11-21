from prompt_toolkit.document import Document
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import SearchToolbar, TextArea


def update_frenemies_info(frenemies_text):
    frenemies_line.text = frenemies_text


def update_prompt_info(prompt_text):
    prompt_line.text = prompt_text


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
prompt_line = TextArea(height=1, style="class:output-field", text="???")

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
