from collections import defaultdict


class Directory:
    """
    Generic tree class for the creation of `directory` objects matching to similar patterns implemented in Unix
    computer systems.
    """
    def __init__(self, name: str, parent: any = None, total_size: int = 0, has_files: bool = False) -> None:
        """
        Initializer for class level variables.
        """
        self.name = name
        self.parent = parent
        self.total_size = total_size
        self.has_files = has_files
        self.directories = defaultdict(Directory)

    def __iter__(self) -> None:
        """
        Override Dunder method for formation of a generator loop to return an iterator for `directory` objects (nodes).
        """
        yield self  # Create generator from `self`
        for sub_directory in self.directories.values():
            yield from sub_directory

    def add_child_directory(self, child_directory: any) -> None:
        """
        Adds a child node (subdirectory) to the current node (parent directory).
        """
        pwd = self  # Set the present working directory (node) to the current self (node)
        self.directories[child_directory.name] = child_directory
        self.total_size += child_directory.total_size

        while pwd.parent:
            pwd.parent.total_size += child_directory.total_size  # Sum child node sizes to become parent node total size
            pwd = pwd.parent
