import sys
sys.path.insert(0, '.\module')
import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        '_my_module', # имя библиотеки собранной pybind11
        ['my_module.cpp'], # Тестовый файлик который компилируем
        include_dirs=[pybind11.get_include()],  # не забываем добавить инклюды pybind11
        language='c++', # Указываем язык
        extra_compile_args=['-std=c++11'], # флаг с++11
    ),
]

setup(
    name='_my_module', # имя библиотеки собранной pybind11
    version='1.0.0',
    author='djvu',
    author_email='djvu@inbox.ru',
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11'],  # Указываем зависимость от pybind11
    package_dir = {'': 'lib'}
)