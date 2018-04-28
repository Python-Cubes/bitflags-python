.. bitflags-python
    FileName:   README.rst
    Author:     Fasion Chan
    Created:    2018-04-28 13:31:13
    @contact:   fasionchan@gmail.com
    @version:   $Id$

    Description:

    Changelog:


===============
bitflags-python
===============

`bitflags` for both python 2 and python 3.

Quick start
===========

First, you have to define your bits, starts from bit 0, one by one:

.. code-block:: pycon

    >>> from bitflags import BitFlags
    >>> class TextStyle(BitFlags):
    ...     names = (
    ...         'bold',
    ...         'italic',
    ...         'underline',
    ...     )
    >>>

Then, you've got all bit masks, with same name but in uppercase:

.. code-block:: pycon

	>>> TextStyle.BOLD
	TextStyle(bits=1)
	>>> TextStyle.ITALIC
	TextStyle(bits=2)
	>>> TextStyle.UNDERLINE
	TextStyle(bits=4)

You can combinate different masks to make what you want:

.. code-block:: pycon

	>> my_style = TextStyle.BOLD | TextStyle.UNDERLINE
	>>> my_style
	TextStyle(bits=5)

You can tell whether specific bit is set:

.. code-block:: pycon

	>>> my_style.is_bold
	True
	>>> my_style.is_italic
	False
	>>> my_style.is_underline
	True

Also, you can get value of given bit:

.. code-block:: pycon

	>>> my_style.bold
	TextStyle(bits=1)
	>>> my_style.italic
	TextStyle(bits=0)
	>>> my_style.underline
	TextStyle(bits=4)

You can get all set bits:

.. code-block:: pycon

	>>> my_style.flags
	['bold', 'underline']

You can use bit operator to set another bit:

.. code-block:: pycon

	>>> my_style |= TextStyle.ITALIC
	>>> my_style
	TextStyle(bits=7)
	>>> my_style.is_italic
	True
	>>> my_style.italic
	TextStyle(bits=2)
