"""
Name - Myint Myat Thura
ID - 31861067
"""

"""
Question 1 Approach

This is a pretty interesting question but I'll get straight to it. The main point of this problem was splitting
the edges into two by using layered graphs. What this means is that the first layer will hold all the slow routes,
and every layer that is created afterwards will have fast routes. There are about 3 functions in total that modifies
the input so that I may build the graph with new vertices. The new vertices are chosen like this: 
Consider these vertices

[0,1,2,3,4], if there are two layers including the first layer (original) we create 5 more vertices, but how? 
We use the (maximum vertex + 1)+ v in list.
After that, we will have [0,1,2,3,4,5,6,7,8,9]. If there are more layers then we add the formula to the new
vertices as well.

The dijkstra runs 2 times, it runs on the first layer to find the distance if we don't pick up new passengers. It
runs another time to the very last layer and the end vertex of it. This represents the distance if we had stops.
Then we compare the two distances and see which one is shorter, then we return the shortest distance. This brings
the question to printing, if we did take the shortest path on the last layer, the paths will be displayed as very 
high numbers depending on the number of duplicated vertices.

For example: [0,1,3,7,7,15,16,12,18,19]

You can see that there are repeated vertices such as 5 which notifies that we have gone into another layer, then
we have super high numbers that should not exist. To get rid of the repeated vertices, we set a new attribute to 
Vertex called layer_switch. If layer switch is true, then it means that it is a vertex that is connected to another
layer. We can remove these unnecessary layers using that attribute. Then we have the higher numbers, to remove those
we loop through the list and subtract every element that is higher than the maximum vertex in the original list, in 
this case, 4.
Start - 0, End - 4, Passengers [2]
First loop: [0,1,3,2,2,10,11,7,13,14]
Second loop: [0,1,3,2,2,5,6,2,8,9]
Third loop: [0,1,3,2,2,0,1,2,3,4]
Then we may remove the repeated numbers, to be more precise, I meant the vertices that are connected to the layers.
Finally we get [0,1,3,2,0,1,2,3,4]

Thank you for reading, I loved this assignment question.

Time Complexity - O(E*log(V)+E)
Space Complexity - O(|E|+|L|)

Written by Myint Myat Thura
"""

def optimalRoute(start, end, passengers, roads):
    """_summary_
        This function is the main function that sets the algorithm in motion. This finds out
        how many layers to create, what is the max vertex value in roads. This decided what the 
        end values should be and what the start value should be.
        
        The overall simplified time complexity of my optimalRoute function would be 
        O((V + E) log V + E + m), where V is the number of vertices in the graph, 
        E is the number of edges in the graph, and m is the number of elements in the passengers list.
    
        Since V is almost always less than E and m is less than E, the overall time complexity of this function
        can be simplified to O(E*log(V)+E)

        Precondition: start,end both must be vertex objects. passenger must be a list, roads must be a 
        list of tuples
        Postcondition: return value must be a list

        Input:
            start - the start vertex
            end - the end vertex on the first layer
            passengers - the list of passengers
            roads - the list of roads in tuples
        Return:
            Returns a list of the shortest path

        Time complexity: 
            Best: O(E*log(V)+E)
            Worst: O(E*log(V)+E)
        Space complexity: 
            Input: O(|E|+|V|log|V|)
            Aux: O(|E|+|L|) where L is the key locations and E is the roads 

    """
    my_graph = Graph(50)
    # finds the max vertex in the roads tuples
    max_vertex = my_graph.find_end_vertex(roads)
    # calls add_layers
    layers = my_graph.add_layers(roads,len(passengers)+1,max_vertex)
    layer_num = len(passengers)
    answer = None
    if layer_num % 2 == 0:
        # checks if the layer number is even or odd, if it is even, the the end veretx is passenger -1
        my_graph.build_graph(max_vertex,passengers,layers,len(passengers)+1,my_graph)
        start = my_graph.get_vertex(start)
        end_a = my_graph.get_vertex((len(passengers)-1)*(max_vertex+1)+end) 
        answer = my_graph.print_path(start,end_a,max_vertex,len(passengers),my_graph.get_vertex(end),my_graph) 
    else:
        # if the layer number is odd, then we use the normal length of psasengers
        my_graph.build_graph(max_vertex,passengers,layers,len(passengers)+1,my_graph)
        start = my_graph.get_vertex(start)
        end_a = my_graph.get_vertex((len(passengers))*(max_vertex+1)+end)
        
        answer = my_graph.print_path(start,end_a,max_vertex,len(passengers),my_graph.get_vertex(end),my_graph)    
    return answer


class MinHeap:
    """
    This is a minHeap class that is implemented for the dijkstra algorithm. The algorithm is based on the
    maxHeap abstract class given in FIT1008. This has then been refactored and implemented in my own way to 
    make a minHeap.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_size):
        """
        Initializes the heap.
        Time complexity - O(1)
        """
        self.length = 0
        self.the_array = [None] * (max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self):
        """
        Checks the size of the heap
        Time complexity - O(1)
        """
        return self.length

    def is_full(self):
        """
       Checks if the heap is full
        Time complexity - O(1)
        """
        return self.length + 1 == len(self.the_array)
    
    def is_empty(self):
        """
        Checks if the heap is empty
        Time complexity - O(1)
        """
        return self.length == 0

    def rise(self, k):
        """
        Rise element at index k to its correct position
        Time Complexity - O(logn)
        """
        item = self.the_array[k]
        while k > 1 and item[0] < self.the_array[k // 2][0]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, obj, key):
        """
        Rise element at index k to its correct position using rise function
        Time Complexity - O(logn)
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = (key, obj)
        self.rise(self.length)
        return key


    def sink(self, k):
        """ 
        Make the element at index k sink to the correct position.
        Time Complexity - O(logn)
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if item[0] <= self.the_array[min_child][0]:
                break
            self.the_array[k] = self.the_array[min_child]
            k = min_child

        self.the_array[k] = item
    def smallest_child(self, k):
        """
        Returns the index of k's child with smallest key value.
        Time Complexity - O(1)
        """
        if 2 * k == self.length or \
                self.the_array[2 * k][0] < self.the_array[2 * k + 1][0]:
            return 2 * k
        else:
            return 2 * k + 1
        

    def get_min(self):
        """ 
        Remove (and return) the minimum element from the heap.
        Time Complexity - O(logn)
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return min_elt[1]

class Graph:
    """
    This class has been modified from the Graph class given in tutorial to suit
    this question's requirements. Functions do not work the same way as I have modified
    the input.
    """
    def __init__(self, v):
        """
        Initializes the Graph with size v.
        Time Complexity - O(1)
        """
        self.vertices =[None]*v
        
    
    def add_vertex(self, vertex, my_graph):
        """
        This function adds the vertex to the graph.

        Precondition: veretx must be an integer
        Postcondition: must have added all vertices without running out of space

        Input:
            vertex - the vertex that is to be added
            my_graph - the Graph object
        Return:
            None

        Time complexity: 
            Best: O(n)
            Worst: O(n)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        try:
            if (my_graph.get_vertex(vertex)).id != vertex:
                new_vertex = Vertex(vertex)
                for space in range(len(self.vertices)):
                    if self.vertices[space] is None:
                        self.vertices[space] = new_vertex
                        return
                raise ValueError("Ran out of Space in Graph")
        except:
            new_vertex = Vertex(vertex)
            for space in range(len(self.vertices)):
                if self.vertices[space] is None:
                    self.vertices[space] = new_vertex
                    return
            raise ValueError("Ran out of Space in Graph")
        
    def add_edge(self,vertex_a,vertex_b,weight): 
        """
        This function adds the edge to the vertex.

        Precondition:
        Postcondition:

        Input:
            vertex_a = starting vertex 
            vertex_b = ending veretx
            edge = weight of the edge between vertex_a and vertex_b
        Return:
            None

        Time complexity: 
            Best: O(n)
            Worst: O(n)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        v_a = self.get_vertex(vertex_a)
        v_a_edge = Edge(vertex_a,vertex_b,weight)
        v_a.edges.append(v_a_edge)
          
    def get_vertex(self, id):
        """
        This function retrieves a vertex object.

        Precondition: id must be an integer
        Postcondition: vertex must be returned

        Input:
            id - the key of the vertex
        Return:
            Returns a vertex object

        Time complexity: 
            Best: O(n)
            Worst: O(n)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        for vertex in self.vertices:
            if vertex is not None and vertex.id == id:
                return vertex
        return None
            
    def dijkstra(self,source,end,max_v,layers,my_graph):   
        """
        This function is based on the breath first search algorithm shown in tutorial class.
        Dijkstra is implemented with my very own minHeap abstract class, nothing was imported. 
        The max_v value is used to print out the list. It is used to display layered vertices as
        normal vertices.
        
        Precondition: source, end and my_graph must all be objects.
        Postcondition: my_list must have more than 1 element and end.distance cannot be none

        Input:
            source - the source node of the algorithm
            end - the target destination
            max_v - the max vertex value in the list
            layers - the number of layers
            graph - the graph object
        Return:
            end.distance - the total distance of the path taken
            my_list - the path taken displayed by vertices

        Time complexity: 
            Best: O(ElogV)
            Worst: O(ElogV)
        Space complexity: 
            Input: O(|E|+|V|log|V|)
            Aux: O(|E|+|L|) where L is the key locations and E is the roads 
        """
        source.distance = 0
        discovered = MinHeap(100)
        discovered.add(source,source.distance)
        while discovered.__len__() > 0:
            u = discovered.get_min()
            u.visited = True
            for attribute in u.edges:
                v = self.get_vertex(attribute.v)
                weight = attribute.weight
                if v.discovered == False:
                    v.discovered = True
                    v.distance = u.distance + weight
                    v.previous = u
                    discovered.add(v,v.distance)
                elif v.visited == False:
                    if v.distance > u.distance + weight:
                        v.distance = u.distance + weight
                        v.previous = u
                        discovered.add(v,v.distance)
        
        path = []
        current_vertex = end
        while current_vertex != source:
                vertex_id = current_vertex.id 
                path.append(vertex_id)
                current_vertex = current_vertex.previous
                
        source_id = source.id
        path.append(source_id)
        path.reverse()

        my_list = path
        max_value = max_v
        layers = layers
        
        for i in path:
            x = my_graph.get_vertex(i)
            if x.layer_switch and x.id>max_v:
                path.remove(i)

        for i in range(layers):
            for index, value in enumerate(my_list):
                if value > max_value:
                    my_list[index] -= max_value + 1
        return my_list,end.distance
        

    def print_path(self,source,end,max_v,layers,real_end,my_graph):
        """
        This is the heart of the function, this decided where the end destination
        of the dijkstra algorithm should be. This depends on how many layers there are
        if there is only one layer, it will choose the destination of the first layer, if it has
        more than 1 layers, it will choose nth layer's end vertex.
        
        In cases where the number of layers are complex to handle, this will run dijkstra two times. 
        One where the destination is the first layer and one where the destination is at the nth layer.
        Then it will compare the two using distances and return the one with the shortest distance.

        Precondition: source, end and my_graph must all be objects.
        Postcondition: my_list must have more than 1 element and end.distance cannot be none

        Input:
            source - the source node of the algorithm
            end - the target destination which is usually not the first layer
            max_v - the max vertex value in the list
            layers - the number of layers
            real end - the ending of the first layer
            graph - the graph object
        Return:
            Returns - result, which is the shortest path

        Time complexity: 
           Time complexity: 
            Best: O(2*(ElogV)) = O(ElogV)
            Worst: O(2*(ElogV)) = O(ElogV)
        Space complexity: 
            Input: O(|E|+|V|log|V|)
            Aux: O(|E|+|L|) where L is the key locations and E is the roads 
        """
        paths = []
        end_vertices = [end,real_end]
        print(end)
        graph = my_graph
        # if layer is more than 1, we choose the end vertex on the nth layer
        if layers >= 1:
            path = my_graph.dijkstra(source,end_vertices[1],max_v,layers,graph)
            # appends the path and distance to a list
            paths.append(path)
            try:
                # tries to run dijkstra with the end vertex on the first graph
                path_2 = my_graph.dijkstra(source,end_vertices[0],max_v,layers,graph)
                # appends the path and distance to a list
                paths.append(path_2)
            except:
                pass
        elif layers == 0:
            # if there are no passengers, we choose the end vertex on the first layer
            path = my_graph.dijkstra(source,end_vertices[1],max_v,layers,graph)
            paths.append(path)
        # chooses the tuple with the minimum distance in the list
        min_value = float('inf')
        min_index = 0
        for i in range(len(paths)):
            if paths[i][1] < min_value:
                min_value = paths[i][1]
                min_index = i

        # Keep only the tuple with the smaller second element
        paths = [paths[min_index]]
        # Extract the first element of the remaining tuple
        result = paths[0][0]
        return result  
    
    def build_graph(self,end,passenger,roads,layers,my_graph):
        """
        This function builds the graph by adding vertices. The vertices include the duplicated
        ones on the new layers too. This function plays a key role in modifying the input along with
        add_layers() function.

        Precondition: end and my_graph must all be objects, layers must be a list, roads must be a list of tuples
        Postcondition: my_list must have more than 1 element and end.distance cannot be none

        Input:
            end - the maximum vertex number in the entire graph
            passenger - the list of passengers
            roads - a list of tuples
            layers - number of layers
            graph - the graph object
        Return:
            Returns nothing

        Time complexity: 
            Best: O(n + m + lp) where m is the number of edges in roads, p is the number of passengers, l is the number fo
            layers and n is the end.
            Since we know that p<l and n is less than m, this can be simplified to O(m)
            Worst: O(m)
        Space complexity: 
            Input: O(m)
            Aux: O(m)
        """
        layer_count = layers
        duplicated_vertices = []
        passenger_w = passenger
        lst = passenger
        # we add vertex to depending on the maximum number of layers
        for vertex in range (0,((end+1)*layer_count)):
            my_graph.add_vertex(vertex,my_graph)
            duplicated_vertices.append(vertex)
        offset = max(duplicated_vertices)
        # we add the duplicated vertices to the vertex as well
        for dup_vertex in duplicated_vertices:
            my_graph.add_vertex(dup_vertex,my_graph)
        # we add the slow road as the first layer
        for a,b,c in roads:
            my_graph.add_edge(a,b,c)
            lst = passenger
        if len(passenger)>0:
            # we add the fast roads to the layers that follows
            for i in range(layers-1):
                lst = [x + end+1 for x in lst]
                # we add the connected edges between layers and weigh them as 0
                for passengers, l in zip(passenger_w, lst):
                    my_graph.add_edge(passengers, l,0)
                    vtx = my_graph.get_vertex(l)
                    vtx_2 = my_graph.get_vertex(passengers)
                    # we note down the vertices that are used to switch layers excluding the vertices
                    # in the first layer
                    vtx.layer_switch = True
                    vtx_2.layer_switch = True   
    
    def add_layers(self, original_list, num_layers, max_v):
        """
        This is another function that creates duplicated vertices, this will then be used by
        build_graph() to add all the necessary vertices.

        Precondition: original_list must be the original inputted road list
        Postcondition: new_list must be a list of tuples

        Input:
            original_list - the original input list of tuples (roads)
            num_layers - the number of layers which are number of passengers+1
            max_v - the maximum value in the original list
        Return:
            Returns list of newly created roads

        Time complexity: 
            Best: O(nm) where n is the size of the original list and where m is the number of layers
            Worst: O(nm) where n is the size of the original list and where m is the number of layers
        Space complexity: 
            Input: O(n) where n is the size of the original list
            Aux: O(n) where n is the size of the original list
        """
        new_list = []
        offset = max_v + 1
        # we use a for loop to seperate the slow layer with fast layers
        for item in original_list:
            new_item = (item[0], item[1], item[2])
            new_list.append(new_item)
        # seperating the fast layer from the slow layer
        for i in range(1, num_layers):
            for item in original_list:
                if i % 2 == 1:
                    new_item = (item[0] + i * offset, item[1] + i * offset, item[3])
                else:
                    new_item = (item[0] + i * offset, item[1] + i * offset, item[2])
                new_list.append(new_item)
        
        return new_list
    

        
   
    def find_end_vertex(self,roads):
        """
        This function finds the largest vertex number in roads

        Precondition: roads must be a list of tuples
        Postcondition: return value must be a float

        Input:
            roads - a list of tuple of roads
        Return:
            Returns a float of highest vertex number

        Time complexity: 
            Best: O(n)
            Worst: O(n)
        Space complexity: 
            Input: O(1)
            Aux: O(1)
        """
        largest = float('-inf')
        for item in roads:
            largest = max(largest, item[0], item[1])
        return largest
            

class Vertex:
    def __init__(self,id):
        """
        Initializes attributes
        Time Complexity - O(1)
        Aux Space - O(1)
        """
        self.id = id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.distance = 0
        self.previous = None
        self.layer_switch = None

class Edge:
    def __init__(self, u,v,weight):
        """
        Initializes attributes
        Time Complexity - O(1)
        Aux Space - O(1)
        """
        self.u = u
        self.v = v
        self.weight = weight

"""
------------------------------------------------------------------------------------------------------------------------------------
"""

"""
Question 2 Approach Explanation

This question was definitely easier than the dijkstra but this is my first time with dynamic programming so
it was quite challenging, neverthless I will get straight into the point.

The main approach of this was to create another list to set the first row of the 2D array to serve as a base case. 
Everything that comes after will use the previous rows, this is tabulation. I used a bottom-up approach to solve this because
frankly, my brain cannot comprehend recursion. This approach in short, solves the problem from the top row to the bottom row,
it makes more sense to go through the columns first and then through the rows. That's because we can use the results from the 
previous row to compute the current row. Then the solution is built from the bottom to the top.

Anyway, we create two empty lists to aid us in our tabulation; min_occupancy and path. Min_occupancy stores
the minimum occupancy values and path is used to store the previous cell that was selected in the optimum
path to reach an n cell.

Consider the following input:

Using the first row of the occupancy probability, we will set the first row of min_occupancy to be equal to that, this
will serve as the base case and will be useful later in finding the adjacent cells.

 occupancy_probability            min_occupancy                paths
   [                           [                          [
    [1,2,3]                     [1, 2, 3],                 [None, None, None]
    [4,5,6]                     [max, max, max],           [None, None, None]
    [7,8,9]                     [max, max, max]            [None, None, None]
   ]                           ]                          ]

The point of my algorithm is to compare the cell with adjacent cell, which means that list[i][j] would be compared with 
list[i+1][j-1], list[i+1][j], list[i+1][j+1].
After my main function checks the "adjacent" values and returns the list with the added values, 
my min_occupancy will look like:
[                        [                                         [
 [1,2,3]                  [1, 2, 3],                                [1,2,3]
 [4,5,6]      ---->       [4+1, 5+1, 6+2],               --->       [5,6,8]
 [7,8,9]                  [7+(4+1), 8+(4+1), 9+(5+1)]               [12,13,15]
]                        ]                                         ]

This returns (12,0) where 12 is the minimum occupancy and 0 is the minimum index on the last row.

This was pretty simple to do but I had a challenge, meeting the time complexity. Because no matter how you
look at it, the 3 nested loops give a time complexity of O(nm^2), that is, unless you read the instructions 
carefully. We have a very useful piece of information where rows will always be more than columns. The innermost loop
is basically checking the occupancy probabilities of each section at a given time step. 
By removing exactly one section from each row, we only need to look at the adjacent sections in the next row. 
So we only need to check at most 3 columns (the one that was removed, and the ones to the left and right of it).
This means that no matter what, the most-innner loop will run for 3 times maximum. Therefore there is no more worry
about the complexity being O(nm^2), it is now O(nm).

Because we got more rows than columns, that means it makes more sense to go through the columns first 
and then through the rows. That's because we can use the results from the previous row to compute the 
current row. This made a big difference. Instead of iterating over each column in every row, we only need 
to check a small number of columns in each row.

The final parts of the algorithm are pretty simple, we're not explicitely using backtracking but we are going 
through the previously solved cases from the last row all the way up to the top row. Remember the output we got?
(12,0)
We use the 0 to travel back up the list, using a reversed range for loop. This looks something like 
for i in reverse(num_rows):
    minimum_path = list[i][0]
    
This gives us [12, (0, 0), (1, 0), (2, 0)] as the final output.
      
Time Complexity - O(nm)
Space Complexity - O(nm)
    
Written By Myint Myat Thura   
"""
def select_sections(occupancy_probability): 
    """
    This is the main function. I have used a modular programming approach where I tried to split up 
    my code into multiple functions, it is easier for me to maintain and test. It is also easier for a 
    reader to understand what is going on. Additional comments on each function also makes sure of that 
    too.
    
    Precondition: occupancy_probility must be a 2D array where number of rows is more than the number of columns
    Postcondition: returns min_total_occupancy (integer) and sections_location (list of tuples) as a list.

    Input:
        path: occupancy_probility must be a 2D array where the occupancy probability is represented
    Return:
        [min_total_occupany,sections_location] -  returns min_total_occupancy (integer) and sections_location (list of tuples) as a list.

    Time complexity:
        Best: O(nm), where n is the number of rows in path.
        Worst: O(nm) where n is the number of rows in path
        
        5 functions are called by select_sections. The time complexity of each are as follows:
        initialize() - O(nm)
        base_case_intialize() - O(1)
        update_min_occupancy_and_path() - O(nm)
        find_min_total_occupancy_and_index() - O(m)
        construct_sections_location - O(n)
        
        O(nm+m+nm+m+n) = O(2nm+m+n) = O(2nm) = O(nm)
        
        The overall time complexity of running select_sections is O(nm)
    Space Complexity:
        Input: O(nm), where n is the number of elements in path
        Aux: O(nm), where n is the number of rows in path.
        
    Recurrence Relations
    
    Base case: For the first row of the grid, the minimum occupancy for each cell is equal to its occupancy probability:
    M[0][j] = occupancy_probability[0][j]
    
    General case: For cells in the rest of the rows, the minimum occupancy is equal to the sum of its occupancy probability
    and the smallest min occupancy of its three neighboring cells in the row above:
    M[i][j] = occupancy_probability[i][j] + min(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
    
    Edge cases: For cells in the first and last columns in the grid, we have to consider only two pairs of neighbors:
    M[i][0] = occupancy_probability[i][0] + min(M[i-1][0], M[i-1][1])
    M[i][num_cols-1] = occupancy_probability[i][num_cols-1] + min(M[i-1][num_cols-2], M[i-1][num_cols-1])

    """
    num_rows = len(occupancy_probability)
    num_cols = len(occupancy_probability[0])
    max_value = 100 * num_rows + 1
    min_occupancy = None
    path = None
    min_occupancy, path = initialize(num_rows, num_cols, max_value)
    base_case_initialize(min_occupancy, occupancy_probability)
    update_min_occupancy_and_path(min_occupancy, path, occupancy_probability)
    min_total_occupancy, min_index = find_min_total_occupancy_and_index(min_occupancy)
    sections_location = construct_sections_location(path, min_index)
    return [min_total_occupancy, sections_location]

def initialize(num_rows, num_cols, max_value):
    """
    This function initilizes the arrays that are going to be used to solve the rest
    of the problem. This starts by creating two dimentional arrays using explicit
    for loops for readibility.
    
    Written By Myint Myat Thura

    Precondition: All the inputs are positive integers.
    Postcondition: Must return two 2D arrays called path and min_occupancy.

    Input:
        num_rows - the number of rows in the input
        num_columns - the number of columns in the input
        max_value - a calculated value that is used to represent the max occupany
    Return:
        min_occupancy - 2D array where all the elements are initialized to be max_value
        path - 2D array where all the elements are initialized to be None

    Time complexity: 
        Best: O(nm), where n is the number of rows and m is the number of columns.
        Worst: O(nm), where n is the number of rows and m is the number of columns.
    Space complexity: 
        Input: O(nm), where n is the number of rows and m is the number of columns.
        Aux: O(nm), where n is the number of rows and m is the number of columns.

    """
    # lets min_occupancy and path lists with all values set to max_value.
    min_occupancy = []
    rows_for_min = num_rows
    for row in range(rows_for_min):
        min_occupancy_row = []
        columns = num_cols
        for col in range(columns):
            min_occupancy_row.append(max_value)
        min_occupancy.append(min_occupancy_row)

    # The path list is initialized with all values set to None.
    path = []
    rows_for_path = num_rows
    for row in range(rows_for_path):
        path_row = []
        columns_for_path = num_cols
        for col in range(columns_for_path):
            path_row.append(None)
        path.append(path_row)


    return min_occupancy, path

def base_case_initialize(min_occupancy, occupancy_probability):
    """
    This function sets all the values of the first row of min_probability using the first row
    of occupancy_probabilty list. This will serve as the base case for dynamic programming.
    
    Written By Myint Myat Thura

    Precondition: Two 2D arrays with same number of columns
    Postcondition: Must update the first row of the min_probability list.

    Input:
        min_occupany - 2D array that represents the min total occupancy
        occupancy_probability - 2D array that contains the list of occupancy probability
    Return:
        No returns

    Time complexity: 
        Best: O(1)
        Worst: O(1)
    Space complexity: 
        Input: O(1)
        Aux: O(1)

    """
    min_occupancy[0] = occupancy_probability[0]

def update_min_occupancy_and_path(min_occupancy, path, occupancy_probability):
    """
    This function updates the min_occupany and path arrays to find the minimum
    total occupany rate. This is where we use dynamic programming and use the base case
    that we have gotten from the base_case_initialize function.
    
    Written By Myint Myat Thura

    Precondition: All the inputs are 2D arrays with the same dimensions.
    Postcondition: min_occupany and path arrays are updated with new values and will shuffle.

    Input:
        min_occupancy - this is a 2D list representing the minimum total occupany rate fo each 
        row and column
        path - a 2D array representing the location of the selected section that represents the minimum
        total occupancy rate for each row and column
        occupany_probability - the main input 2D list where it represents every occupancy probability
        
    Return:
        No returns

    Time complexity: 
        Best: O(nm), where n is the number of rows and m is the number of columns.
        Worst: O(nm), where n is the number of rows and m is the number of columns.
    Space complexity: 
        Input: O(1)
        Aux: O(1)

    """
    # This function updates the values of the min_occupancy and path lists based on the occupancy_probability list.
    num_rows = len(occupancy_probability)
    num_cols = len(occupancy_probability[0])
    # iterates through the rows excluding base case
    for row in range(1, num_rows):
        path_func = path
        # iterates through each column
        for col in range(num_cols):
            min_occupancy[row][col], path_func[row][col] = get_min_occupancy_and_path(min_occupancy[row - 1], occupancy_probability[row][col], col, num_cols)

def get_min_occupancy_and_path(prev_row_min_occupancy, current_cell_occupancy_probability, col, num_cols):
    """
    This function checks the adjacent cells as per instructions
    
    Written By Myint Myat Thura

    Precondition: All the inputs are integers.
    Postcondition: min_occupany and path arrays are updated with new values and will shuffle.

    Input:
        prev_row_min_occupancy - an integer representing the minimum occupancy from the previous row
        row and column
        current_cell_occupancy_probability - an integer that represents the current minimum occupancy
        col - the current column index
        num_cols - the total number of columns in the original input
    Return:
        Returns min_occupancy which is a float and path with is a list

    Time complexity: 
        Best: O(1) because this inner loop runs a maximum of 3 times due to n>m
        Worst: O(1), because this inner loop runs a maximum of 3 times due to n>m
    Space complexity: 
        Input: O(1)
        Aux: O(1)

    """
    min_occupancy = float('inf')
    min_path = None
    prev_occu = prev_row_min_occupancy
    # finds the adjacent values and do comparison
    for prev_col in range(max(0, col - 1), min(num_cols, col + 2)):
        # loop runs at most 3 times due to n>m
        cell_occu_prob = current_cell_occupancy_probability
        current_occupancy = prev_occu[prev_col] + cell_occu_prob
        # keeps updating the minmum occupancy if a smaller value has been found
        if current_occupancy < min_occupancy:
            min_occupancy = current_occupancy
            min_path = prev_col
    return min_occupancy, min_path

def find_min_total_occupancy_and_index(min_occupancy):
    """
    This function is responsible to find and return the minimal total occupancy rate
    by iterating over a certain column in the min_occupancy table.
    
    Written By Myint Myat Thura

    Precondition: min_occupency is a 2D list
    Postcondition: Returns the minimum_total_occupancy and the index in a tuple.

    Input:
        num_rows - a 2D list that represents the minimum total occupancy rate for each row
        and column
    Return:
        min_total_occupancy - the minimum total occupancy rate
        min_index - index of the column that contains the minimum total occupancy rate.

    Time complexity: 
        Best: O(m), where m is the number of columns.
        Worst: O(m), where m is the number of columns.
    Space complexity: 
        Input: O(1)
        Aux: O(1)
        
    
    

    """
    # Loop through the last row of min_occupancy and find the index with the smallest value
    min_total_occupancy = float('inf')
    min_index = None
    for col in range(len(min_occupancy[0])):
        occupancy_table = min_occupancy
        if occupancy_table[-1][col] < min_total_occupancy:
            min_total_occupancy = occupancy_table[-1][col]
            min_index = col
    return min_total_occupancy, min_index
    # Return the minimum total occupancy value and index

def construct_sections_location(path, min_index):
    """
    This is the final part of the function. This will complie the results and add them to an array
    then it will print it out to get teh result.
    
    Written By Myint Myat Thura

    Precondition: Path must be a 2D list min_index is an integer 
    representing the column index of the minimum total occupancy
    Postcondition: returns a list of tuples to represent the location of each
    section in the path

    Input:
        path: a 2D list represennting the path of the minimum total occupancy
        min_index - an integer representing the column index of the minimum total occupancy
    Return:
        sections_location - a list of tuples representing the location of each section in 
        the path of minimum total occupancy

    Time complexity:
        Best: O(n), where n is the number of rows in path.
        Worst: O(n) where n is the number of rows in path
        
    Space Complexity:
        Input: O(n), where n is the number of elements in path
        Aux: O(n), where n is the number of rows in path.
        
    """
    # Traverse the path list in reverse order
    sections_location = []
    path_0 = path
    index = min_index
    for row in reversed(range(len(path_0))):
        # Update the column index based on the previous row's column index in the path
        sections_location.append((row, index))
        index = path_0[row][index]
    # Reverse the order of the sections_location list to match the order of the path list
    sections_location.reverse()
    # Return the list of tuples representing the locations of the sections in the optimal path
    return sections_location 









