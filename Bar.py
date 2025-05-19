




from libqtile import bar, qtile

from options import default_bar_type, default_colorscheme, default_options


def load_module(module_path: str) -> object:
    try:
        module = importlib.import_module(module_path)
        return module
    except ImportError:
        print("Error: Could not import module")
        return None



# dynamic module loading
colorscheme_module_path = f"themes.colorschemes.{default_colorscheme}.colors"
colors = load_module(colorscheme_module_path)

widgets_module_path = f"widgets.{default_bar_type}.widgets"
w = load_module(widgets_module_path)

custom_widgets_module_path = f"widgets.{default_bar_type}.custom_widgets"
cw = load_module(custom_widgets_module_path)
# ---------------------

widget_list = (
        w.app_launcher
        + w.separator_small
        + w.tray
        + w.separator_small
        + w.windowname
        + w.separator_auto
        + w.client_count
        + w.separator_small
        + w.groups
        + w.separator_small
        + w.layout_icon
        + w.separator_auto
        + w.widgetbox_info
        + w.separator_small
        + w.battery
        + w.separator_small
        + w.time
        + w.separator_small
        + w.date
    )

gaps_size = default_options["gaps_size"]

top_bar = bar.Bar(
    widget_list,
    size=30,
    background=colors.bar_colors["bg"],
    margin=[gaps_size, gaps_size, 0, gaps_size],  # [top, right, bottom, left]
    border_width=[5, 5, 5, 5],  # [top, right, bottom, left]
    border_color=[
        colors.bar_colors["border"],
        colors.bar_colors["border"],
        colors.bar_colors["border"],
        colors.bar_colors["border"],
    ],
)

