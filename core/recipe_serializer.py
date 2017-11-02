class RecipeSerializer():
  def __init__(self, scraper):
    self.scraper = scraper

  def to_json(self):
    return {
      "title": self.scraper.title(),
      "time": self.scraper.total_time(),
      "ingredients": self.scraper.ingredients(),
      "instructions": self.scraper.instructions()
    }