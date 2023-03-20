from recipe_scrapers.cookomix import Cookomix
from tests import ScraperTest


class TestCookomixScraper(ScraperTest):

    scraper_class = Cookomix

    def test_host(self):
        self.assertEqual("cookomix.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.cookomix.com/recettes/polenta-cremeuse-thermomix/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Polenta crémeuse")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Nathalie")

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 portions", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 Gousses d'ail",
                "100 grammes Oignons",
                "30 grammes Huile d'olive",
                "1500 grammes Eau",
                "1 cuillère à café Sel",
                "2 pincées Poivre",
                "400 grammes Polenta",
                "50 grammes Parmesan",
                "100 grammes Crème fraîche épaisse",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            [
                "Mettre 2 gousses d'ail épluchées et (à ajuster en fonction des goûts) et 100 grammes d'oignons épluchés et coupés en morceaux dans le Thermomix. Mélanger 4 sec/vitesse 6.",
                "Ajouter 30 grammes d'huile d'olive dans le Thermomix et rissoler 4 min 30 sec/120°C/vitesse 1.",
                "Ajouter 1500 grammes d'eau, 1 cuillère à café de sel et 2 pincées de poivre dans le Thermomix. Cuire 10 min/100°C/vitesse 1.",
                "Ajouter le fouet.",
                "Ajouter 400 grammes de polenta dans le Thermomix et cuire 40 min/100°C/vitesse 2 sans le gobelet doseur.",
                "Ajouter 50 grammes de parmesan rapés et 100 grammes de crème fraîche épaisse dans le Thermomix. Mélanger 1 min/vitesse 2.",
                "Servir chaud.",
            ],
            self.harvester_class.instructions(),
        )
