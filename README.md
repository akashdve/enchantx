enchantX:  Extended Python bindings for the Enchant spellchecker
========================================================

This package provides a set of Python language bindings for the Enchant
spellchecking library.  For more information, visit the project website:
    
    http://enchantx.live

What is Enchant?
----------------

Enchant is used to check the spelling of words and suggest corrections
for words that are miss-spelled.  It can use many popular spellchecking
packages to perform this task, including ispell, aspell and MySpell.  It
is quite flexible at handling multiple dictionaries and multiple
languages.

More information is available on the Enchant website:

    http://www.abisource.com/enchant/


How do I use it?
----------------

For Windows users, install the pre-built binary packages using
pip::

    pip install enchantx


These packages bundle a pre-built copy of the underlying enchant library.
Users on other platforms will need to install "enchant" using their system
package manager (brew on macOS).

Once the software is installed, python's on-line help facilities can
get you started.  Launch python and issue the following commands:

    >>> import enchantx
    >>> help(enchantx)
