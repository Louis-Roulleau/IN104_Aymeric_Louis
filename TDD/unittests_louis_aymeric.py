import unittest
from identite import vehicule

class TestVehicule(unittest.TestCase):
	K=vehicule('Kangoo',90,2000)
	K.getPoids()
	K.getVitesse()

	def test_doubler(self):
		self.assertEqual(self.K.doubler(40),0,"Schould return false")

    def test_doubler2(self):
        self.assertEqual(self.K.doubler(140),1,"Schould return true")

	def test_vitesse(self):
		self.assertEqual(self.K.getVitesse(),self.K.vitesse,"Retourne la vitesse")

	def test_poids(self):
		self.assertEqual(self.K.getPoids(),self.K.poids, "Retourne le poids")
    

if __name__ == '__main__':
    unittest.main()
