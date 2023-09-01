import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"


from IPython.display import Audio
import nltk  
import numpy as np

from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE


preload_models()

script = """
"मेरे साथ रहने के लिए धन्यवाद, यहां आना सम्मान की बात है और हम दुबई में अपने बच्चों के साथ बहुत अच्छा समय बिता रहे हैं।
यह बहुत शानदार है और वास्तव में ऐसे किसी भी व्यक्ति को उत्साहित करता है जो इस महान शहर में नहीं गया है।
और प्रेरणाओं के संदर्भ में स्पष्टीकरण का एक लंबा प्रश्न है। मूलतः जब मैं बच्चा था तो मैं सोचता था कि जीवन का अर्थ क्या है।
पूछने के लिए सही प्रश्नों को समझने का प्रयास करें। उतना ही हम मानवीय चेतना का दायरा और पैमाना बढ़ा सकते हैं।
हम यह प्रश्न उतना ही बेहतर ढंग से पूछ सकेंगे। और। कुछ चीज़ें जो भविष्य सुनिश्चित करने के लिए आवश्यक हैं।"
""".replace("\n", " ").strip()

sentences = nltk.sent_tokenize(script)



SPEAKER = "v2/en_speaker_7"
silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

pieces = []
for sentence in sentences:
    audio_array = generate_audio(sentence, history_prompt=SPEAKER)
    pieces += [audio_array, silence.copy()]


Audio(np.concatenate(pieces), rate=SAMPLE_RATE)