from googletrans import Translator
from SearchMusic import searchmus

translator = Translator()

def tarjimasi(matni):
    tarjima = translator.translate(matni,'uz').text
    return tarjima

