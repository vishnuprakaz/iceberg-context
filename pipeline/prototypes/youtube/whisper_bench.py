import sys, time
from faster_whisper import WhisperModel
model_name, path, out = sys.argv[1:4]
t0 = time.time()
m = WhisperModel(model_name, device='cpu', compute_type='int8', cpu_threads=4)
t1 = time.time()
import wave, numpy as np
w = wave.open(path); audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
segs, info = m.transcribe(audio, language='en', vad_filter=True, beam_size=1)
text = ' '.join(s.text.strip() for s in segs)
t2 = time.time()
open(out, 'w').write(text)
print(f'{model_name}: load {t1-t0:.1f}s, transcribe {t2-t1:.1f}s for {info.duration:.0f}s audio -> RTF {(t2-t1)/info.duration:.3f}, {len(text.split())} words')
