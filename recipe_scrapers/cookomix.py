# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class Cookomix(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookomix.com"

    def title(self):
        return self.soup.select_one("div.entry-header > h1").text.strip()

    def description(self):
        return self.soup.select_one(
            "div.entry-content > div.entry-content__meta"
        ).text.strip()

    def total_time(self):
        total_time_elem = self.soup.select_one(
            "dl.entry-content__meta__item--preptime > dd:nth-child(2)"
        )
        return int(total_time_elem.text.strip().split()[0])

    def yields(self):
        yields_elem = self.soup.select_one(
            "dl.entry-content__meta__item--quantity > dd:nth-child(2)"
        )
        return f"{yields_elem.text.strip()} servings"

    def ingredients(self):
        ingredients = []
        ingredients_sections = self.soup.select("h2.ribbon.ingredients + ul")
        for section in ingredients_sections:
            for ingredient in section.find_all("li"):
                ingredients.append(normalize_string(ingredient.text.strip()))

        return ingredients

    def instructions(self):
        instructions_list = self.soup.select(
            "div.entry-content__instructions > ol > li"
        )
        return "\n".join(
            [
                normalize_string(instruction.text.strip())
                for instruction in instructions_list
            ]
        )

    def image(self):
        img_elem = self.soup.select_one(
            "div.entry-content__featured-image > picture > img"
        )
        return img_elem["src"] if img_elem else None
