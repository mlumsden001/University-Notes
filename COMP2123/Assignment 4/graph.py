"""
The polar expedition graph!
===========================

Contains the graph connecting the vertices (or base stations) on the map.

This is going to be the main file that you are modifying. :)

Usage:
    Contains the graph, requires the connection to vertices and edges.
"""
import math
import sys

from vertex import Vertex
from edge import Edge


# Define a "edge already exists" exception
class EdgeAlreadyExists(Exception):
    """Raised when edge already exists in the graph"""
    def __init__(self, message):
        super().__init__(message)


class Graph:
    """
    Graph Class
    -----------

    Represents the graph of vertices, which is equivalent to the map of base
    stations for our polar expedition.

    Attributes:
        * vertices (list): The list of vertices
    """

    def __init__(self):
        """
        Initialises an empty graph
        """
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        """
        Insert the vertex storing the y_pos and x_pos

        :param x_pos: The x position of the new vertex.
        :param y_pos: The y position of the new vertex.

        :type x_pos: float
        :type y_pos: float

        :return: The new vertex, also stored in the graph.
        """

        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        """
        Inserts the edge between vertex u and v.

        We're going to assume in this assignment that all vertices given to
        this will already exist in the graph.

        :param u: Vertex U
        :param v: Vertex V

        :type u: Vertex
        :type v: Vertex

        :return: The new edge between U and V.
        """

        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        """
        Removes the vertex V from the graph.

        :param v:  The pointer to the vertex to remove
        :type v: Vertex
        """

        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v)
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        """
        Get the distance between vertex u and v.

        :param u: A vertex to get the distance between.
        :param v: A vertex to get the distance between.

        :type u: Vertex
        :type v: Vertex
        :return: The Euclidean distance between two vertices.
        """

        # Euclidean Distance
        # sqrt( (x2-x1)^2 + (y2-y1)^2 )

        return math.sqrt(((v.x_pos - u.x_pos)**2) + ((v.y_pos - u.y_pos)**2))

    @staticmethod
    def opposite(e, v):
        """
        Returns the vertex at the other end of v.

        :param e: The edge to get the other node.
        :param v: Vertex on the edge.
        :return: Vertex at the end of the edge, or None if error.
        """

        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    def find_emergency_range(self, v):
        """
        Returns the distance to the vertex W that is furthest from V.

        :param v: The vertex to start at.
        :return: The distance of the vertex W furthest away from V.
        """
        if len(self._vertices) <= 1:
            return 0
        furthest = 0
        for i in self._vertices:
            if self.distance(v, i) > furthest:
                furthest = self.distance(v, i)
        return furthest

    def path_finder(self, start, b, s, r, path, visited):
        """
        Recursive function which finds all paths from node "start" to "s" within maximum range "r"

        :param start: The starting node, used to store that node whilst recursing.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :param path: List of all nodes in the path.
        "param visited: Dictionary of all nodes which have been visited, with a key-value pair of 
        the node and a boolean True or False if has been visited.
        :return: The LIST of the VERTICES in the path.
        """
        if visited[b] == False:
            visited[b] = True
            path.append(b)

        if b.__eq__(s) == True:
            return path
        else:
            for e in b.edges:
                if (e.v).__eq__(b) == True:
                    x = e.u 
                else:
                    x = e.v
                if visited.get(x) == False and self.distance(start, x) <= r and x not in path:
                    return self.path_finder(start, x, s, r, path, visited)
                
            path.pop()
            if path != []:
                u = path[-1]
                return self.path_finder(start, u, s, r, path, visited)
            else:
                return None
                
    
    def find_path(self, b, s, r):
        """
        Find a path from vertex B to vertex S, such that the distance from B to
        every vertex in the path is within R.  If there is no path between B
        and S within R, then return None.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :return: The list of the vertices in the path.
        """

        start = b
        path = []
        visited = {}
        for node in self._vertices:
            visited.update({node: False})
        return self.path_finder(start, b, s, r, path, visited) 
        
    def minimum_finder(self, b, s, final_paths, path, visited):
        """
        Find all possible paths from "b" to "s". Returns a list of all lists.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param final_paths: Final list of paths to be returned.
        :param path: List of all vertices in the path.
        :param visited: Dictionary of all nodes which have been visited, with a key-value pair of 
        the node and a boolean True or False if has been visited.
        :return: The list of paths.
        """
        if visited[b] == False:
            visited[b] = True
            path.append(b)

        if b.__eq__(s) == True:
            new_path = list(path)
            final_paths.append(new_path)
        else:
            for e in b.edges:
                if (e.v).__eq__(b) == True:
                    x = e.u 
                else:
                    x = e.v
                if visited.get(x) == False:
                    final_paths = self.minimum_finder(x, s, final_paths, path, visited)
        if len(path) > 0:
            path.pop()
            visited[b] = False
        return final_paths


    def range_finder(self, path):
        """
        Finds the maximum range of a path.
        
        :param path: List of all nodes in the path.
        :return: The maximum range of the path.
        """
        root = path[0]
        r = 0
        for node in path:
            if self.distance(root, node) > r:
                r = self.distance(root, node)
        return r

    def minimum_range(self, b, s):
        """
        Returns the minimum range required to go from Vertex B to Vertex S.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :return: The minimum range in all the paths to go from B to S.
        """
        path = []
        final_paths = []
        visited = {}
        for node in self._vertices:
            visited.update({node: False})
        shortest = None

        max_ranges = []
        
        output = self.minimum_finder(b, s, final_paths, path, visited)
        for lists in output:
            max_ranges.append(self.range_finder(lists))

        return min(max_ranges)
     
    def move_vertex(self, v, new_x, new_y):
        """
        Move the defined vertex.

        If there is already a vertex there, do nothing.

        :param v: The vertex to move
        :param new_x: The new X position
        :param new_y: The new Y position
        """
        #Check if vertex exists at position
        for u in self._vertices:
            if u.x_pos != new_x and u.y_pos != new_y:
                v.move_vertex(new_x, new_y)