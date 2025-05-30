#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")
    
    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list")
    
    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list")
        return item

    def extend(self, iterable):
        for item in iterable:
            super().append(item)
        print(f"Extended the list with {iterable}")
