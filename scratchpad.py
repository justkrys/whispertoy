import sounddevice as sd

fs = 48000
sd.default.samplerate = fs
sd.default.channels = 2
# sd.default.device = 'default'

print("Recording...")
duration = 10.5  # seconds
myrecording = sd.rec(int(duration * fs))
sd.wait()

print("Playing...")
sd.play(myrecording)
sd.wait()

print("Done.")
