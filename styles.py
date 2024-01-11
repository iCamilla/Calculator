# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import qdarktheme

from variables import DARKER_COLOR, DARKEST_COLOR, FIRST_COLOR

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {FIRST_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='light',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{FIRST_COLOR}",
            },
            "[light]": {
                "primary": f"{FIRST_COLOR}",
            },
        },
        additional_qss=qss
    )
