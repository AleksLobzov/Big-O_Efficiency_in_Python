# Big-O_Efficiency_in_Python
This simple program aims to examine efficiency of the basic python data structures such as Lists and Dictionaries.

To make an experiment:

1. Download 'efficiency.py' file.

2. Run the program by typing 'python efficiency.py' in your terminal.

3. Set the parameters required:

   * The range of experiments. <br>
     <b>Note</b>: The program uses the 'range' function. That means that if you type '100000, 1000001, 100000', it will generate the range(100000, 1000001, 100000)
   * The number of experiments which is used by 'timeit' function
   
With the current version of the program you should see the following Big-Os of the List methods:
   * index assignment has O(1)
   * append() has O(1)
   * pop() has O(1)
   * pop(i) has O(n)
   * insert(i, item) has O(n)
<br>

<b>Note</b>:
   * O(1) means that the execution time almost don't depend on the number of elements in a List
   * O(n) is the proterty of a method which execution time changes almost linearly depending on the number of elements in a List
