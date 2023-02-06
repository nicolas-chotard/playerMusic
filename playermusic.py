import tkinter as tk
import tkinter.filedialog
import pygame

def jouer_audio():
    pygame.mixer.music.play()

def mettre_pause_audio():
    pygame.mixer.music.pause()

def arreter_audio():
    pygame.mixer.music.stop()

def augmenter_volume():
    volume_actuel = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(min(volume_actuel + 0.1, 1.0))

def baisser_volume():
    volume_actuel = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(max(volume_actuel - 0.1, 0.0))

def activer_boucle():
    pygame.mixer.music.play(-1 if pygame.mixer.music.get_busy() else 0)

def choisir_fichier():
    chemin_fichier = tkinter.filedialog.askopenfilename(filetypes=[("Fichiers audio", "*.mp3;*.wav;*.m4a")])
    pygame.mixer.music.load(chemin_fichier)

fenetre = tk.Tk()
fenetre.title("Lecteur audio")

bouton_choisir_fichier = tk.Button(fenetre, text="Choisir fichier", command=choisir_fichier)
bouton_choisir_fichier.pack()

bouton_jouer = tk.Button(fenetre, text="Jouer", command=jouer_audio)
bouton_jouer.pack()

bouton_mettre_pause = tk.Button(fenetre, text="Mettre en pause", command=mettre_pause_audio)
bouton_mettre_pause.pack()

bouton_arreter = tk.Button(fenetre, text="Arrêter", command=arreter_audio)
bouton_arreter.pack()

bouton_augmenter_volume = tk.Button(fenetre, text="Volume +", command=augmenter_volume)
bouton_augmenter_volume.pack()

bouton_baisser_volume = tk.Button(fenetre, text="Volume -", command=baisser_volume)
bouton_baisser_volume.pack()

bouton_activer_boucle = tk.Button(fenetre, text="Activer boucle", command=activer_boucle)
bouton_activer_boucle.pack()

pygame.mixer.init()

fenetre.mainloop()