from pathlib import Path

class riddle():
    def __init__(self, day: int, mode:str):
        self.day  = str(day)
        self.path = Path("src") / "2025" / f"day{self.day}"
        assert mode in ["test", "full"]
        self.mode = mode + ".txt"
        self._load_riddle()

    def _load_riddle(self):
        filename = self.path / self.mode
        self.lines = [l.split("\n")[0] for l in open(filename, 'r', encoding='utf-8')]

