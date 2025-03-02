from typing import Iterator, Set

from pydantic import BaseModel, Field


class Section(BaseModel):
    title: str = Field(description="The title of the documentation section")
    file: str = Field(description="The file path corresponding to the section")
    children: list["Section"] = Field(default_factory=list, description="Subsections")

    def iter_sections(self) -> Iterator["Section"]:
        yield self
        for child in self.children:
            yield from child.iter_sections()


class Documentation(BaseModel):
    sections: list[Section] = Field(description="Documentation sections")

    def get_unique_filenames(self) -> Set[str]:
        return {
            section.file
            for section in self.sections
            for section in section.iter_sections()
        }