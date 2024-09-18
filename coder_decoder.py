ALPH = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def coder(text: str, key: int, alph: str, swith: bool = True) -> str:
    chip_text = ""

    if key < 0:
        raise ValueError("The key must be greater than zero")
    
    if swith is True:
        for i in text:
            if i.isalpha():
                new_letter = alph[(alph.find(i) + key) % len(alph)]
                chip_text += new_letter
            else:
                chip_text += i
                
    else:
        for i in text:
            if i.isalpha():
                new_letter = alph[(alph.find(i) - key) % len(alph)]
                chip_text += new_letter
            else:
                chip_text += i

    return chip_text

print("Зашифрованный текст: ", coder("фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб"
                                     , 3, ALPH, False))


#съешь же ещё этих мягких французских булок да выпей чаю
#фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб