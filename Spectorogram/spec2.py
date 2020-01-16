#coding:utf-8
# 参考サイト　https://emracrue.hatenablog.com/entry/2019/05/18/010541
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def main():
    # fileload
    y, sr = librosa.load('oct.wav')

    # STFT
    S = np.abs(librosa.stft(y))

    # output
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max))
    plt.savefig('spec.png', transparent = True, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
    main()
