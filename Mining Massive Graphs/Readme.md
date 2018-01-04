
# Abstract

Now a days the graphs for the real word networks are massive. Conventional exact computation techniques require unrealistic computation time and memory. To overcome this problem approximate computation techniques are used to find the statistics of graphs. In this project the time complexity of exact and approximate methods was compared for different real world graphs. The exact computation method was parallelized to reduce the time complexity.
The networks used were from the Stanford Network Analysis Project [SNAP](http://snap.stanford.edu/data/index.html)
in particular, we worked with the following social networks, listed in increasing size

1. wiki-Vote : 7 115 nodes
2. soc-Epinions1 : 75 879 nodes
3. ego-Gplus : 107 614 nodes
4. soc-Pokec : 1 632 803 nodes

The following libraries are required to run the exact computation part:
1. numpy
2. networkx

The following libraries are required to run the approximate computation part:
1. numpy
2. networkx
3. networkit

The packages could be easily installed using pip and pip3.

# COMPONENT EXTRACTION: 

To find the statistics for the provided graph, the subgraphs of LSCC and LWCC are extracted. The subgraphs are than used for exact and approximate computation of statistics.
For the extraction of subgraphs component_extraction.py file is used. The constants are set. The paths are relative to the directory in which component_extraction.py file is located


* STATS_FILE_NAME:	File path to save the running time of the program.
* DELIMITER:		Used to define the delimiter used in the graphs provided.
* EDGE_WRITE:		File path to write the extracted LSCC and LWCC edges. See the convention used in the sample file.
* FILE_PATH_PREFIX:	The directory in which the original graphs are stored.
* FILE_NAME:		Name of the original graph file without .txt extension.

Once the constants are set the file could be run from the terminal. The file with the LSCC and LWCC would be created in the directory defined in EDGE_WRITE constant

# EXACT COMPUTATION:

Once the edges for the subgraph LSCC and LWCC are extracted the exact computation or approximate computation could be used to find the statistics.
To compute the exact statistics the file exact_statistics.py is used. The file find the exact statistics for one connected component at a time. To find the statistics for LWCC and LSCC the program should be run 2 times using the appropriate settings. The file has some constants which needs to be set.

* STATS_FILE_NAME:	File path to save the running time of the program.
* DELIMITER:		Used to define the delimiter used in the graphs provided.
* FILE_PATH_PREFIX:	The directory in which the edges of subgraphs are stored.
* FILE_NAME:		Partial name of the edge files name. It should be without .txt extension. It should be similar to EDGE_WRITE in component_extraction.py. The only difference is that it does not have directory prefixed to the file name. See the sample for the example.
* PATH_DISTRIBUTION_PATH:	File Path where you want to store the path distribution.
* CONNECTED_COMPONENT:	Which path distribution do you want to extract the values of this constant could be 'lscc' or 'lwcc'.

## NOTE: The directories should be created in advanced otherwise the program would throw an error of directory not found.##

The directory_structure.png file is available to see the default directory structure used

# APPROXIMATION COMPUTATION:

The code is distributed into four jupyter notebooks, each representing each graph for which we have done approximations and exact computations:

* graph-stats.ipynb
* graph-stats+2.ipynb
* graph-stats+3.ipynb
* graph-stats+4.ipynb

Apart from the ANF Approximation which is in the following file, all approximation schemes are done in the jupyter notebooks:

* ANF- Hop Plot approximation.ipynb

The comparison graph and plots for each method is available in:

* Accuracy plots.ipynb

