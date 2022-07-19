from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError("Not implemented")

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, self.dest / path.relative_to(self.source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        Parser.copy(path, source, dest)


