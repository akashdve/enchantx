EnchantX
========================================================
An extension of `pyenchant` package to serve better.
 

What is EnchantX?
----------------

This package is an extension of [**PyEnchant**](https://pyenchant.github.io/pyenchant/) (which provides a set of Python language bindings for the Enchant
spellchecking library). This package is extended to provide most appropriate suggestions based on given text.
EnchantX Visualizer is available on the EnchantX website:

    http://enchantx.live/

What is Enchant?
----------------

Enchant is used to check the spelling of words and suggest corrections
for words that are miss-spelled.  It can use many popular spellchecking
packages to perform this task, including ispell, aspell and MySpell.  It
is quite flexible at handling multiple dictionaries and multiple
languages.

More information is available on the Enchant website:

    http://www.abisource.com/enchant/


How do I install it?
-------------------

Install the package using pip::

    $ pip install enchantx


This package will also install its dependency of pyenchant package which bundle a pre-built copy of the underlying enchant library.
Users on other platforms will need to install "enchant" using their system
package manager (brew on macOS).

Once the software is installed, python's on-line help facilities can
get you started.  Launch python and issue the following commands:

    >>> import enchantx
    >>> help(enchantx)

**Note:**
EnchantX requires binary file "GoogleNews-vectors-negative300.bin" to work correctly. By default, It will try to search for the file in the following locations:
1. "/home/<$user>/.enchantx/" 
2. Inside current working directory

It is recommended to provide the path of binary file while creating the XDict Object.

How do I use it?
---------------

    >>> import enchantx
    >>> spellchecker = enchantx.XDict("/home/akash/GoogleNews-vectors-negative300.bin")
    >>> spellchecker.check("wofl")
    False
    >>> spellchecker.suggest("wofl")
    ['Wolf', 'wolf', 'wool', 'FOFL', 'ROFL']
    
    
    >>> example = "quanfiction movie"
    >>> spellchecker.check("movie")
    True
    >>> spellchecker.check("quanfiction")
    False
    
    >>> spellchecker.suggest("quanfiction")
    ['qualification', 'quantification', 'nonfiction']
    
    >>> spellchecker.smart_suggest(word="quanfiction", next_word="movie")
    ['nonfiction', 'qualification', 'quantification']