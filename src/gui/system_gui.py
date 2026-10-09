import dearpygui.dearpygui as dpg
from src.automata.dfa import dfa
from src.validator.validator import Validator
from pathlib import Path

dpg.create_context()

validator = Validator(dfa)
BASE_DIR = Path(__file__).resolve().parents[2]
LOGO_PATH = BASE_DIR / "assets" / "GG_fixed.png"

width, height, channels, data = dpg.load_image(str(LOGO_PATH))

with dpg.texture_registry(show=False):
    dpg.add_static_texture(
        width=width, height=height, default_value=data, tag="logo_texture"
    )

def validate_demo():
    code = dpg.get_value("code_input").strip()
    if code == "":
        dpg.set_value("result_title", "NO INPUT")
        dpg.set_value("result_message", "Please enter an access code.")
        dpg.set_value("result_state", "Final State: -")
        show_transitions([])
        transition_diagram([])
        return
    result = validator.validate_code(code)

    if result['accepted']:
        dpg.set_value("result_title", "ACCEPTED")
        dpg.set_value("result_message", "The acccess code matches the defined language")
    else:
        dpg.set_value("result_title", "REJECTED")
        dpg.set_value("result_message", "The access code does not matched the defined language")
    
    dpg.set_value(
        "result_state", f"Final State: {result['final_state']}"
    )
    show_transitions(result["transitions"])
    transition_diagram(result['transitions'])


def show_transitions(transitions):
    dpg.delete_item("transition_container", children_only=True)

    with dpg.table(
        header_row=True,
        borders_innerH=True,
        borders_innerV=True,
        borders_outerH=True,
        borders_outerV=True,
        policy=dpg.mvTable_SizingStretchProp,
        width=-1,
        height=230,
        scrollY=True,
        tag="dfa_table",
        parent="transition_container"
    ):
        dpg.add_table_column(
            label="Step",
            init_width_or_weight=0.12
        )
        dpg.add_table_column(
            label="Symbol",
            init_width_or_weight=0.18
        )
        dpg.add_table_column(
            label="Current State",
            init_width_or_weight=0.35
        )
        dpg.add_table_column(
            label="Next State",
            init_width_or_weight=0.35
        )

        for transition in transitions:
            with dpg.table_row():

                dpg.add_text(
                    str(transition["step"]),
                    tag=f"step_{transition['step']}"
                )

                dpg.add_text(
                    transition["symbol"],
                    tag=f"symbol_{transition['step']}"
                )

                dpg.add_text(
                    transition["current_state"],
                    tag=f"current_{transition['step']}"
                )

                dpg.add_text(
                    transition["next_state"],
                    tag=f"next_{transition['step']}"
                )

    dpg.bind_item_theme("dfa_table", table_theme)
def transition_diagram(transitions):
    dpg.delete_item("transition_visual", children_only=True)

    max_chars = 140
    current_line = ""

    for transition in transitions:
        current_state = transition["current_state"]
        symbol = transition["symbol"]
        next_state = transition["next_state"]

        transition_text = (
            f"{current_state}---[{symbol}]--->{next_state}"
        )

        if current_line == "":
            current_line = transition_text

        elif len(current_line) + len(transition_text) + 3 <= max_chars:
            current_line += "   " + transition_text

        else:
            dpg.add_text(
                current_line,
                parent="transition_visual"
            )
            current_line = transition_text

    if current_line:
        dpg.add_text(
            current_line,
            parent="transition_visual"
        )

with dpg.font_registry():

    default_font = dpg.add_font(
        "C:/Windows/Fonts/segoeui.ttf",
        18
    )

    title_font = dpg.add_font(
        "C:/Windows/Fonts/segoeuib.ttf",
        28
    )

    heading_font = dpg.add_font(
        "C:/Windows/Fonts/segoeuib.ttf",
        21
    )

with dpg.theme() as main_theme:

    with dpg.theme_component(dpg.mvAll):

        dpg.add_theme_color(
            dpg.mvThemeCol_WindowBg,
            (13, 25, 42)
        )

        dpg.add_theme_color(
            dpg.mvThemeCol_ChildBg,
            (22, 38, 60)
        )


        dpg.add_theme_color(
            dpg.mvThemeCol_Button,
            (145, 108, 45)
        )

        dpg.add_theme_color(
            dpg.mvThemeCol_ButtonHovered,
            (170, 130, 58)
        )

        dpg.add_theme_color(
            dpg.mvThemeCol_ButtonActive,
            (170, 130, 58)
        )

      
        dpg.add_theme_color(
            dpg.mvThemeCol_Text,
            (242, 238, 226)
        )

    
        dpg.add_theme_color(
            dpg.mvThemeCol_FrameBg,
            (28, 45, 68)
        )

        dpg.add_theme_color(
            dpg.mvThemeCol_FrameBgHovered,
            (35, 33, 77)
        )

 
        dpg.add_theme_color(
            dpg.mvThemeCol_Border,
            (105, 91, 62)
        )

        dpg.add_theme_style(
            dpg.mvStyleVar_WindowPadding,
            20,
            20
        )

        dpg.add_theme_style(
            dpg.mvStyleVar_FrameRounding,
            6
        )

        dpg.add_theme_style(
            dpg.mvStyleVar_ChildRounding,
            8
        )

        dpg.add_theme_style(
            dpg.mvStyleVar_ItemSpacing,
            10,
            10
        )

with dpg.theme() as table_theme:
    with dpg.theme_component(dpg.mvTable):
        dpg.add_theme_color(
            dpg.mvThemeCol_TableHeaderBg,
            (145, 108, 45)
        )
        dpg.add_theme_color(
            dpg.mvThemeCol_TableBorderStrong,
            (105, 91, 62)
        )
        dpg.add_theme_color(
            dpg.mvThemeCol_TableBorderLight,
            (70, 80, 95)
        )

with dpg.window(
    label="Secure Access Code Validation System",
    tag="main_window",
    
):
    with dpg.group(horizontal=True):
        dpg.add_image("logo_texture", width=50, height=50)
 
        with dpg.group():
            dpg.add_text(
                "SECURE ACCESS CODE VALIDATION SYSTEM",
                color=(50, 180, 255),
                tag="title"
            )

            dpg.bind_item_font("title", title_font)

            dpg.add_text(
                "DFA-Based Pattern Recognition",
                color=(150, 180, 210)
            )

    dpg.add_separator()

    dpg.add_spacer(height=10)

    with dpg.group(horizontal=True):


        with dpg.child_window(
            width=540,
            height=370,
            border=True
        ):
            dpg.add_text(
                "VALIDATE ACCESS CODE",
                color=(201, 164, 92)
            )
            dpg.bind_item_font(
                dpg.last_item(),
                heading_font
            )

            dpg.add_spacer(height=5)

            dpg.add_text(
                "Enter an access code to validate against the minimized DFA."
            )

            dpg.add_spacer(height=5)

            dpg.add_input_text(
                tag="code_input",
                hint="GG-IT-25-AC12-R02-A",
                width=400
            )

            dpg.add_spacer(height=5)

            dpg.add_button(
                label="VALIDATE",
                width=130,
                callback=validate_demo
            )

            dpg.add_spacer(height=15)

            dpg.add_text(
                "VALIDATION RESULT",
                color=(201, 164, 92)
            )

            dpg.add_spacer(height=2)

            dpg.add_text(
                "Waiting...",
                tag="result_title"
            )

            dpg.add_text(
                "Enter an access code and click VALIDATE.",
                tag="result_message"
            )

            dpg.add_text(
                "Final State: —",
                tag="result_state"
            )
        
        dpg.add_spacer(width=1)

        with dpg.child_window(
            width=540,
            height=370,
            border=True,
            no_scrollbar=True
        ):
            dpg.add_text(
                "DFA TRANSITION TRACE",
                color=(201, 164, 92)
            )
            dpg.bind_item_font(
                dpg.last_item(),
                heading_font
            )

            dpg.add_spacer(height=10)

            dpg.add_text(
                "Symbol-by-symbol processing"
            )

            dpg.add_spacer(height=15)

            with dpg.child_window(
                tag="transition_container",
                width=-1,
                height=230,
                border=False,
                
            ):
                dpg.add_text(
                    "No validation performed yet."
                )

    dpg.add_spacer(height=1)
    with dpg.child_window(
        tag="transition_visual",
        width=-1,
        height=145,
        border=True,
        no_scrollbar=True
    ):
        dpg.add_text(
            "DFA TRANSITION SEQUENCE",
            color=(201, 164, 92)
        )

        dpg.add_spacer(height=5)

        dpg.add_text(
            "State-by-state path followed by the input string."
        )

dpg.bind_theme(main_theme)
dpg.create_viewport(title='Secure Access Code Validator', width=1170, height=725
, resizable=False, decorated=True, x_pos=80, y_pos=1)
dpg.set_viewport_clear_color((16, 18, 70))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()