# dictcc2anki
This small program is based on rbaron's dict.cc.py script. Utilizing it to search for translations in the dict.cc online-dictionary.
The results are presented in a list from which the user can choice the most fitting translation to add it as a vocabulary-card to the Anki-Software.

Requirements are the installation of dict.cc.py which you can get here: https://github.com/rbaron/dict.cc.py
as well as the anki development branch from: https://github.com/dae/anki

The current version only works under the english settings of Anki.
To use the program just the line change collection_path = 'path/to/your/collection.anki2' according to the file path of your collection.

Be aware that errors within the code can corrupt your collection. Make sure you got backups ready. Or use only a separate collection.

Within the program enter the word you want to translate choice the input as well as the output language and press return within the textbox.
Choice the most fitting translation within the list click on it. Press the add to anki button to add the flashcard.