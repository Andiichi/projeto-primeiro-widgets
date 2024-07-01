from sys import platform
from cx_Freeze import setup, Executable

base = None

if platform =='win32':
    base = 'Win32Gui'

setup(
    name='tradutor_andrezza',
    version='1.0',
    description='Tradutor de idiomas feito na live Dunossauro',
    options = {
        'build_exe':{
            'includes': ['tkinter', 'ttkbootstrap']
            }
        },
    executables=[
        Executable('tradutor.py',base=base)
    ],
)