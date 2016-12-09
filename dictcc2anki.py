from tkinter import *
from tkinter import ttk
import sys, re
from anki import Collection
from anki.importing import TextImporter
import csv, os, re
from dictcc import Dict, AVAILABLE_LANGUAGES

collection_path = 'C:/Users/Lorenz/Documents/Anki/Lorenz1/collection.anki2'



def ensure_unicode(string):
    if hasattr(string, "decode"):
        return string.decode("utf-8")
    return string

def run(event):
    translation_lb.delete(0, END)
    word = in_word_entry.get()
    input_language = in_lan_cb.get()
    output_language = out_lan_cb.get()
    max_results = 50
    result = Dict.translate(word,
                            input_language,
                            output_language)

    if not result.n_results:
        print("No results found for {} ({} <-> {}).".format(
            word, input_language, output_language))
        return

    for i, (input_word, output_word) in enumerate(result.translation_tuples):
        print_translation(output_word)
        if i == max_results:
            break


def print_translation(output_word):
    translation_lb.insert(END, output_word)


def make_cards(event):
    card_type = 'Basic (and reversed card)'
    deck_name = 'Englisch'
    card_front = str(in_word_entry.get())
    card_back  = str(translation_lb.get(translation_lb.curselection()[0]))
    deck = Collection(collection_path);
    deck_id = deck.decks.id(deck_name)
    deck.decks.select( deck_id )
    model = deck.models.byName( card_type )
    model['did']=deck_id
    deck.models.save( model )
    deck.models.setCurrent( model )
    fact            = deck.newNote()
    fact['Front']   = card_front
    fact['Back']    = card_back
    deck.addNote( fact )
    deck.save()
    deck.close()
    print("{} <-> {} card was added".format(card_front, card_back))
    in_word_entry.delete(0, END)

window = Tk()
window.config(bg="WHITE")
lan = ['de', 'en', 'ro', 'it', 'fr', 'ru', 'bg', 'pt', 'es']
in_word_entry = ttk.Entry(window, width=54)
in_lan_label = Label(window, text='Input Language')
out_lan_label = Label(window, text='Output Language')
in_lan_label.config(bg="WHITE")
out_lan_label.config(bg="WHITE")
in_lan_var = StringVar(window)
in_lan_var.set('en')
out_lan_var = StringVar(window)
out_lan_var.set('de')
in_lan_cb = ttk.Combobox(window, textvariable=in_lan_var)
in_lan_cb['values'] = lan
out_lan_cb = ttk.Combobox(window, textvariable=out_lan_var)
in_lan_cb.config(width=4)
out_lan_cb.config(width=4)
translation_lb = Listbox(window, width=54)
add_to_anki_btn = ttk.Button(window, text='Add to Anki', width=54)
in_word_entry.grid(column=1, row=0, columnspan=2)
in_lan_label.grid(column=1, row=1, sticky=W)
out_lan_label.grid(column=1, row= 2, sticky=W)
in_lan_cb.grid(column=2, row=1, sticky=E)
out_lan_cb.grid(column=2, row=2, sticky=E)
translation_lb.grid(column=1, row=3, columnspan=2)
add_to_anki_btn.grid(column=1, row=4, columnspan=2)
add_to_anki_btn.bind('<Button-1>', make_cards)
in_word_entry.bind('<Return>', run)
window.mainloop()
