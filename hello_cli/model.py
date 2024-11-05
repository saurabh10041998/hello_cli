from dataclasses import dataclass

@dataclass
class HelloModel:
    name: str = "Test me!!"


    @classmethod
    def with_name(cls, name: str) -> 'HelloModel':
        return cls(name)

    @property
    def msg(self):
        return f"Hello {self.name!r}"
