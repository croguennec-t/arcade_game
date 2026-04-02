 import pyxel

    class shoot :
        def __init__(self, jeu, x, y):

        
        # =====================================================
        # == UPDATE
        # =====================================================
        def update(self):
            """Mise à jour du vaisseau (30FPS)
            """
            self._move()


        def _move(self):
            
        
        
        # =====================================================
        # == DRAW
        # =====================================================
        def draw(self):
            """
            Dessin du tir
            """
            pyxel.blt(self.x, self.y, 0, 10, 1, self.w, self.h)