text = "съешь же ещё этих мягких французских булок да выпей чаю"
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
key = 3
chip_text = ""

for i in text:
    if i.isspace():
        chip_text += " "
        continue
    a = alph.find(i)
    index = (a + 3) % 33
    chip_text = chip_text + alph[index]

print(chip_text)