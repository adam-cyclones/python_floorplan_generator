from lib.data.Room import Room
from lib.data.Floor import Floor
from lib.data.Building import Building
from dataclasses import asdict

print(Building(width=0, height=0, floors=[Floor(Room(0, 0), Room(0, 0))]))


# import json
# import random
# import argparse
# import networkx as nx
# from shapely.geometry import box
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# class Room:
#     def __init__(self, name, floor, width, height):
#         self.name = name
#         self.floor = floor  # 'Outside', 'F1', 'F2', 'Basement', etc.
#         self.width = width  # Width in meters
#         self.height = height  # Height in meters
#         self.position = None  # (x, y) coordinates in meters
#         self.polygon = None  # Shapely polygon representing the room
#         self.connections = []  # List of connected room names

#     def create_polygon(self):
#         x, y = self.position
#         self.polygon = box(x, y, x + self.width, y + self.height)

#     def add_connection(self, other_room):
#         if other_room.name not in self.connections:
#             self.connections.append(other_room.name)

# def get_room_definitions(house_class):
#     filename = f"{house_class}_class_rooms.json"
#     try:
#         with open(filename, 'r') as f:
#             room_definitions = json.load(f)
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Room definition file '{filename}' not found.")
#     return room_definitions

# def generate_floor_plan(house_class='middle'):
#     # Load room definitions
#     room_definitions = get_room_definitions(house_class)
#     rooms = {}
#     room_list = []

#     # Create the Outside node
#     outside_info = room_definitions.get('Outside')
#     outside = Room('Outside', outside_info['floor'], *outside_info['size'])
#     rooms['Outside'] = outside

#     # Determine which rooms to include based on probabilities
#     for name, info in room_definitions.items():
#         if name == 'Outside':
#             continue
#         include_room = info.get('mandatory', False) or random.random() < info.get('probability', 1.0)
#         if include_room:
#             room = Room(name, info['floor'], *info['size'])
#             rooms[name] = room
#             room_list.append(room)

#     # Ensure essential rooms are included
#     essential_rooms = ['Entrance Hall', 'Hallway', 'Kitchen', 'Staircase', 'Bathroom']
#     missing_rooms = [room_name for room_name in essential_rooms if room_name not in rooms]
#     if missing_rooms:
#         print(f"Essential rooms missing: {missing_rooms}. Regenerating floor plan.")
#         return generate_floor_plan(house_class)

#     # Place rooms using a simple grid layout
#     place_rooms(rooms, room_list)

#     # Create connections between rooms
#     G = create_connections(rooms)

#     # Check navigability using NetworkX
#     if not nx.is_connected(G):
#         print("Generated floor plan is not navigable. Regenerating...")
#         return generate_floor_plan(house_class)

#     return rooms

# def place_rooms(rooms, room_list):
#     # Simple grid placement
#     grid_size = 5  # Number of rooms per row
#     room_spacing = 1.0  # Spacing between rooms in meters
#     x_offset = 0
#     y_offset = 0
#     max_row_height = 0

#     for idx, room in enumerate(room_list):
#         if idx % grid_size == 0 and idx != 0:
#             x_offset = 0
#             y_offset += max_row_height + room_spacing
#             max_row_height = 0

#         room.position = (x_offset, y_offset)
#         room.create_polygon()
#         x_offset += room.width + room_spacing
#         if room.height > max_row_height:
#             max_row_height = room.height

#     # Place Outside node to the left of the Entrance Hall
#     entrance_hall = rooms['Entrance Hall']
#     outside = rooms['Outside']
#     outside.position = (entrance_hall.position[0] - outside.width - room_spacing, entrance_hall.position[1])
#     outside.create_polygon()

# def create_connections(rooms):
#     G = nx.Graph()
#     for room_name in rooms:
#         G.add_node(room_name)

#     # Connect Outside to Entrance Hall
#     G.add_edge('Outside', 'Entrance Hall')
#     rooms['Outside'].add_connection(rooms['Entrance Hall'])
#     rooms['Entrance Hall'].add_connection(rooms['Outside'])

#     # Essential connections
#     G.add_edge('Entrance Hall', 'Hallway')
#     G.add_edge('Entrance Hall', 'Staircase')
#     G.add_edge('Hallway', 'Kitchen')
#     G.add_edge('Staircase', 'Bathroom')

#     rooms['Entrance Hall'].add_connection(rooms['Hallway'])
#     rooms['Entrance Hall'].add_connection(rooms['Staircase'])
#     rooms['Hallway'].add_connection(rooms['Kitchen'])
#     rooms['Staircase'].add_connection(rooms['Bathroom'])

#     # Class-specific connections
#     if 'Drawing Room' in rooms:
#         G.add_edge('Hallway', 'Drawing Room')
#         rooms['Hallway'].add_connection(rooms['Drawing Room'])
#     if 'Living Room' in rooms:
#         G.add_edge('Hallway', 'Living Room')
#         rooms['Hallway'].add_connection(rooms['Living Room'])
#     if 'Dining Room' in rooms:
#         G.add_edge('Hallway', 'Dining Room')
#         rooms['Hallway'].add_connection(rooms['Dining Room'])
#     if 'Study' in rooms:
#         G.add_edge('Hallway', 'Study')
#         rooms['Hallway'].add_connection(rooms['Study'])
#     if 'Library' in rooms:
#         G.add_edge('Hallway', 'Library')
#         rooms['Hallway'].add_connection(rooms['Library'])
#     if 'Conservatory' in rooms:
#         G.add_edge('Hallway', 'Conservatory')
#         rooms['Hallway'].add_connection(rooms['Conservatory'])
#     if 'Scullery' in rooms:
#         G.add_edge('Kitchen', 'Scullery')
#         rooms['Kitchen'].add_connection(rooms['Scullery'])
#     if 'Pantry' in rooms:
#         G.add_edge('Kitchen', 'Pantry')
#         rooms['Kitchen'].add_connection(rooms['Pantry'])

#     return G

# def generate_floor_plan_visualization(rooms, filename='floor_plan.png'):
#     fig, ax = plt.subplots()
#     for room in rooms.values():
#         if room.position is None or room.name == 'graph':
#             continue
#         x, y = room.position
#         rect = patches.Rectangle((x, y), room.width, room.height, linewidth=1, edgecolor='black', facecolor='white')
#         ax.add_patch(rect)
#         ax.text(x + room.width / 2, y + room.height / 2, room.name, ha='center', va='center', fontsize=8)
#     plt.axis('equal')
#     plt.axis('off')
#     plt.tight_layout()
#     plt.savefig(filename)
#     print(f"Floor plan visualization saved as '{filename}'.")

# def display_floor_plan(rooms):
#     print("Floor Plan:")
#     for room in rooms.values():
#         if room.name == 'graph':
#             continue
#         connections = ', '.join(room.connections)
#         print(f"{room.name} connected to: {connections}")

# def parse_arguments():
#     parser = argparse.ArgumentParser(description='Generate a Victorian house floor plan.')
#     parser.add_argument('-c', '--class', dest='house_class', choices=['upper', 'middle', 'lower'],
#                         default='middle', help='Class of the house (upper, middle, lower). Default is middle.')
#     return parser.parse_args()

# if __name__ == "__main__":
#     args = parse_arguments()
#     house_class = args.house_class
#     rooms = generate_floor_plan(house_class)
#     display_floor_plan(rooms)
#     generate_floor_plan_visualization(rooms)
