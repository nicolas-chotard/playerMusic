import tkinter as tk
import tkinter.filedialog
import pygame

#Variable pour choisir un fichier et l'ajouter dans la liste

def choisir_fichier():
    pygame.mixer.init()
    chemin_fichier = tkinter.filedialog.askopenfilename(
        filetypes=[("Fichiers audio", "*.mp3")]
    )
    if chemin_fichier:
        playlist.append(chemin_fichier)
        listbox_pistes.insert(tk.END, chemin_fichier)

#Variable pour choisir supprimer un fichier 

def supprimer_piste():
    selection = listbox_pistes.curselection()
    if selection:
        index = int(selection[0])
        del playlist[index]
        listbox_pistes.delete(index) 

#Variable pour lancer la musique

def jouer_audio():
    selection = listbox_pistes.curselection()
    if selection:
        index = int(selection[0])
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()

#Variable pour mettre en pause

def mettre_pause_audio():
    pygame.mixer.music.pause()

#Variable pour arreter l'audio

def arreter_audio():
    pygame.mixer.music.stop()

#Variable pour augmenter le volume

def augmenter_volume():
    volume_actuel = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(min(volume_actuel + 0.1, 1.0))

#Variable pour baisser le volume

def baisser_volume():
    volume_actuel = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(max(volume_actuel - 0.1, 0.0))

#Variable pour activer un boucle

def activer_boucle():
    pygame.mixer.music.play(-1 if pygame.mixer.music.get_busy() else 0)

# Initialisation de la liste de lecture

playlist = []

#Interface graphique

fenetre = tk.Tk()
fenetre.title("Lecteur audio")

bouton_choisir_fichier = tk.Button(
    fenetre, text="Ajouter fichier", command=choisir_fichier
)
bouton_choisir_fichier.pack()

bouton_supprimer_fichier = tk.Button(
    fenetre, text="Supprimer fichier", command=supprimer_piste
)
bouton_supprimer_fichier.pack()

listbox_pistes = tk.Listbox(fenetre)
listbox_pistes.pack()

bouton_jouer = tk.Button(fenetre, text="Jouer", command=jouer_audio)
bouton_jouer.pack()

bouton_mettre_pause = tk.Button(fenetre, text="Mettre en pause", command=mettre_pause_audio)
bouton_mettre_pause.pack()

bouton_arreter = tk.Button(fenetre, text="Arrêter", command=arreter_audio)
bouton_arreter.pack()

bouton_augmenter_volume = tk.Button(
    fenetre, text="Volume +", command=augmenter_volume
)
bouton_augmenter_volume.pack()

bouton_baisser_volume = tk.Button(
    fenetre, text="Volume -", command=baisser_volume
)
bouton_baisser_volume.pack()

bouton_activer_boucle = tk.Button(
    fenetre, text="Activer boucle", command=activer_boucle
)
bouton_activer_boucle.pack()

fenetre.mainloop()
