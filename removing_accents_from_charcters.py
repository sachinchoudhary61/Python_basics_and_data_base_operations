# Removing accents from characters
import unidecode
str = "Caf$ Munchen"
str = unidecode.unidecode(str)

print(str)

""" This Program removes accents from the accented letters such as $ """
# e^ = e
"""One of the Simplest ways to do that is to use a module "unidecode".\n
It does not come with default python distribution but can be easily
installed using pip."""
