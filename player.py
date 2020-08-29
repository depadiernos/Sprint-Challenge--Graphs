from util import Queue

class Player:
    def __init__(self, starting_room, num_rooms):
        self.current_room = starting_room
        self.num_rooms = num_rooms
        self.visited = set()
        self.path = []
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            self.path.append(direction)
            self.visited.add(self.current_room)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("No room in that direction.")
    def shortest_path(self):
        q = Queue()
        q.enqueue((
            self.current_room, 
            []
            ))
        entered = set()
        while q.size() > 0:
            current, path = q.dequeue()
            if current not in self.visited:
                return path
            elif current not in entered:
                entered.add(current)
                for direction in current.get_exits():
                    new_path = path.copy()
                    new_path.append(direction)
                    q.enqueue((
                        current.get_room_in_direction(direction),
                        new_path
                        ))
        print("No room in that direction")
    def find_path(self):
        self.visited.add(self.current_room)
        while len(self.visited) < self.num_rooms:
            path = self.shortest_path()
            for direction in path:
                self.travel(direction)
                print(self.current_room.id)