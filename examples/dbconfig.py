"""
Configuration example for ``ptpdb``.

Copy this file to ~/.ptpython/dbconfig.py
"""

from prompt_toolkit.layout.dimension import LayoutDimension

__all__ = (
    'configure',
)

def configure(debugger):
    # Set preffered height to 20 lines
    height = LayoutDimension(preferred=20)
    debugger._source_code_window._height = (lambda cli: height)
