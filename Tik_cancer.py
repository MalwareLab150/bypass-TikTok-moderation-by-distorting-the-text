import random


distortion_map = {
    'a': ['а', 'á', 'à'],
    'b': ['Ƅ', 'Ь'],
    'c': ['ᴄ', 'с'],
    'd': ['ԁ', 'ɗ'],
    'e': ['е', 'è', 'é'],
    'f': ['ƒ'],
    'g': ['ɡ'],
    'h': ['һ', 'н'],
    'i': ['і', 'í', 'ï'],
    'j': ['ј'],
    'k': ['κ'],
    'l': ['ⅼ', 'ӏ'],
    'm': ['м'],
    'n': ['п', 'ɴ'],
    'o': ['о', 'ò', 'ó'],
    'p': ['р'],
    'q': ['զ'],
    'r': ['г'],
    's': ['ѕ', '$'],
    't': ['т'],
    'u': ['ᴜ', 'υ'],
    'v': ['ν'],
    'w': ['ԝ'],
    'x': ['х'],
    'y': ['у'],
    'z': ['ᴢ'],
}


def distort_text(text):
    distorted = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in distortion_map:
            substitute = random.choice(distortion_map[lower_char])
            if char.isupper():
                substitute = substitute.upper()
            distorted += substitute
        else:
            distorted += char
    return distorted

# Salva su file
def salva_su_file(testo, filename="text_bypass_tiktok.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(testo)
    print(f"\nText saved in: {filename}")

if __name__ == "__main__":
    user_input = input("write whatever you want: ")
    risultato = distort_text(user_input)

    print("\nresult:\n" + risultato)

    salva_su_file(risultato)
