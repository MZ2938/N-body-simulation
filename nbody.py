import pygame
import numpy as np
import sys
import os

# Constantes physiques et paramètres de la simulation
GRAVITY = 1
NB_PARTICLES = 800

class NBody:
    def __init__(self):
        pygame.init()
        self.W, self.H = 1000, 700
        self.win = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("N-Body Simulation")

        self.dt = 0.001        # pas de temps : plus petit = plus précis mais plus lent
        self.epsilon = 0.001   # évite la division par zéro quand deux particules sont trop proches
        self.zoom = 0.7 * self.H
        self.offset = np.array([self.W//5,self.H//5], dtype=float)  # décalage de la caméra

        np.random.seed(10)
        # Positions aléatoires dans [0, 1]²
        self.r = np.random.uniform(0, 1, (NB_PARTICLES, 2))
        # Vitesses initiales faibles et aléatoires
        self.v = np.random.uniform(-0.1, 0.1, (NB_PARTICLES, 2))
        # Toutes les particules ont la même masse fixé à 1
        self.mass = np.ones(NB_PARTICLES)

    def compute_forces(self):
        # Calcule l'accélération de chaque particule due à toutes les autres
        # Loi de Newton : a_i = sum_j G * mj * (rj - ri) / |rj - ri|^3
        a = np.zeros((NB_PARTICLES, 2))
        for i in range(NB_PARTICLES):
            diff = self.r - self.r[i]          # vecteurs de i vers toutes les autres
            dist = np.linalg.norm(diff, axis=1).reshape((NB_PARTICLES, 1))
            dist = np.maximum(dist, self.epsilon)  # évite dist = 0
            F = GRAVITY * self.mass.reshape(-1,1) * diff / (dist**3 + self.epsilon)
            a[i] = np.sum(F, axis=0)
        return a

    def update(self):
        # Intégrateur d'Euler : simple mais accumule des erreurs au fil du temps
        # v(t+dt) = v(t) + a(t) * dt
        # r(t+dt) = r(t) + v(t) * dt
        a = self.compute_forces()
        self.v += a * self.dt
        self.r += self.v * self.dt

    def handle_events(self):
        # Gestion des événements pygame (fermeture, clavier)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        # Déplacement de la caméra
        if keys[pygame.K_LEFT]:  self.offset[0] += 20
        if keys[pygame.K_RIGHT]: self.offset[0] -= 20
        if keys[pygame.K_UP]:    self.offset[1] += 20
        if keys[pygame.K_DOWN]:  self.offset[1] -= 20
        # Zoom
        if keys[pygame.K_z]:     self.zoom *= 1.05
        if keys[pygame.K_s]:     self.zoom *= 0.95
        # Screenshot
        if keys[pygame.K_p]:
            os.makedirs("screenshots", exist_ok=True)
            pygame.image.save(self.win, f"screenshots/frame_{len(os.listdir('screenshots'))}.png")

    def draw(self):
        # Efface l'écran puis redessine chaque particule
        self.win.fill((0, 0, 0)) # couleur noire
        for r in self.r:
            # Conversion coordonnées simulation -> pixels
            pos = (r * self.zoom + self.offset).astype(int)
            pygame.draw.circle(self.win, (0, 200, 255), pos, 1)
        pygame.display.update()

    def run(self):
        # Boucle principale : événements -> physique -> rendu
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)  # limite à 60 FPS

if __name__ == "__main__":
    NBody().run()