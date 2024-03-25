# XML and Social Network Analyzer Project
## Overview
This is a python desktop application that is designed to parse and visualize XML files representing users in a social network. The system encapsulates user data, including names, posts, and followers. This interactive application provides a range of functionalities, from ensuring XML consistency and fixing errors to advanced network analysis, making it a versatile tool for managing and analyzing social network data.
### [Short demonstration video](https://www.youtube.com/watch?v=8KfUDB0blp8)
## Installation
#### pre-built exe program: [download](https://www.mediafire.com/file/sbhycydydncv0h9/tram6_XML_Analyzer.rar/file)<br>
to run the project source code:
* clone the repository
* run `pip install -r requirements.txt`
* run `main.py`
#### note: pyside2 requires python version between 2.7 and 3.11, but not 3.0, 3.1, 3.2, 3.3 or 3.4. 
## Program Manual
### File
![image](https://github.com/balbal1/Data-Structures-Project/assets/13494749/bf58eb42-5fba-4d4d-972f-d9108ad90e05)
* `Open XML` Opens an XML file
* `Save as XML` Saves the editor content as an XML file
* `Open Compressed` Opens a file that is compressed by this program (.comp file)
* `Save as Compressed` Saves the editor content as a compressed file (.comp file)
* `Help` Show help window
* `Close` Exits the program
### Edit
![image](https://github.com/balbal1/Data-Structures-Project/assets/13494749/e672b208-b922-406b-a13f-2d9c9e15561c)
* `Undo` Undo last operation
* `Redo` Redo last undo
* `Detect Errors` Detect if there are any inconsistency or missing tags in the XML file
* `Fix Errors` Fix the errors that are detected
* `Prettify` Prettifies the XML file by fixing indentations
* `Minify` Minifies the XML file by removing extra spaces and new lines
* `Convert to JSON` Converts the XML data format into JSON format
* `Visualize Network` Opens the window for network visualization
### Network
![image](https://github.com/balbal1/Data-Structures-Project/assets/13494749/74920748-353b-483c-bd22-8b871843babf)
* `Find most influencer user` Finds the user that is followed by most people
* `Find most active user` Finds the user that follows most other people
* `Find mutual users` Finds common followers between two users
* `Suggest users` Suggests new users for someone based on the followers of his followers
* `Search` Searchs the users post by author, content or topics
## Data Structures Implemented in the Project
* #### XML Tree:
  * Used to store the XML tags and their tree structure to manipulate and analyze it.
  * Contains useful methods that prettifies, minifies and converts the data to JSON format.
* #### Huffman Binary Tree:
  * When the user compresses the file, a huffman tree is constructed to encode each character to a certain huffman coding based on its frequency
  * When the user opens the compressed file, the huffman tree is re-constructed to decode the huffman coding into its original characters
* #### Users Graph:
  * Used to store the network of users in a graph structure to traverse and analyze it.
  * Contains useful methods that finds the most influencer or most active users and find mutual users. 
* #### Red-Black Binary Search Tree:
  * It is used as a hashmap to store the words and topics of posts and link them to their posts so the search function becomes faster.
## Program Features
* ### XML Consistency Checking and Correction
The program detects and visually presents inconsistencies in XML files. These may include missing opening or closing tags and mismatched tags. Furthermore, the application is equipped to resolve these errors, ensuring correct nesting of the XML tags.
* ### XML Formatting and Minification
To enhance readability and reduce file size, the application supports XML formatting by maintaining proper indentation for each level. Additionally, users can benefit from a minification feature that eliminates unnecessary whitespaces and indentations, resulting in smaller-sized XML files.
* ### XML to JSON Conversion
The utility extends its capabilities to converting XML files to JSON format, providing flexibility in data representation.
* ### Graph Data Structure Representation
Underlying the system is a graph data structure that efficiently represents the relationships between users, their posts, and followers. This structure facilitates network analysis, offering valuable insights into user influence, activity levels, mutual followers.
* ### Network Analysis
The application leverages the graph data structure to perform comprehensive network analysis. Users can identify the most influential and active users, explore mutual followers between two users, and receive personalized suggestions for new connections.
* ### Post Search
Effortlessly search for posts containing specific words or topics within the social network. This feature provides users with a quick and efficient way to extract relevant information from a vast pool of data.
* ### Undo/Redo Operations
The inclusion of undo and redo functionality enhances user experience by allowing seamless reverting or reapplication of changes made during the editing process. This feature adds a layer of flexibility to user interactions.
## Technical Implementation
To meet project constraints, the implementation adheres to a set of predefined data structures, including arrays, dynamic arrays (vectors), linked lists, stacks, queues, and priority queues (heap). Notably, the team had the challenge of implementing the map function from scratch.
## References
* [pyqt library documentation](https://doc.qt.io/qtforpython-6.2/)
* [networkx library documentation](https://networkx.org/documentation/stable/reference/introduction.html)