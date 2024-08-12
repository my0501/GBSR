# GBSR: Graph-Based Suspiciousness Refinement of Fault Localization

## Project Introduction:

GBSR is a strategy for refining the suspiciousness scores in fault localization. This method aims to assist developers in more accurately pinpointing and rectifying defects within code. By leveraging graph structures and associated algorithms, GBSR offers an enhanced measure of suspicion for potential fault locations.

## Provided Resources:

Within this open-source project, we offer essential resources for experimentation:


- **Data Folder**: Contains the necessary data files for conducting experiments.
- **Code Folder**: Includes the source code implementing the GBSR strategy.
- **Example Folder**:  The effectiveness of our approach is demonstrated through an example program containing a Lang1 program with critical information and another example program that includes a complete Math19 program.
- **GBSR_for_SIR Folder**: We also conducted further analysis on the SIR dataset, and the experimental results are presented in this folder.

These resources are made available to facilitate reference and reproducibility of the experimental process. Developers can clone the repository to access the code and data required for utilizing GBSR in fault localization experiments.



## Data Files
The project includes a dedicated "Data" folder, housing essential files required for experimentation. These data files are instrumental in supporting various aspects of fault localization strategies. Developers can find and utilize these files within the repository to conduct experiments, analyze results, and enhance their understanding of GBSR's effectiveness in refining fault localization.
   1. **Defects4J**

In our experimental process, we focused on five Defects4J subjects:

| Subject   | Name            | #Test | #Loc | #Version | #Faults |
|-----------|-----------------|-------|------|----------|---------|
| Lang      | commons-lang    | 2,245 | 22K  | 58       | 83      |
| Chart     | jfreechart      | 2,205 | 96K  | 24       | 37      |
| Cli       | commons-cli     | 361   | 4K   | 36       | 45      |
| JxPath    | commons-jxpath  | 401   | 21K  | 22       | 36      |
| Math      | commons-math    | 3,602 | 85K  | 103      | 137     |

These subjects collectively encompass a total of 243 versions and 338 faults.

2. **Data Acquisition Omission**

Due to the core focus of this project lying in the GBSR methodology, the data acquisition process has been omitted. Instead, pre-analyzed data is directly shared for experimentation purposes. This approach streamlines the project's emphasis on the GBSR method and provides readily available data for experimentation.

3. **Data Format**

The experiment data is provided in JSON format, offering a structured and versatile representation for ease of use. 

As an illustration, here is an example structure of the JSON data for the subject "Lang" with the version "Lang1":

```json
{   
   "proj": "Lang1", 
    "ans": [1], 
    "methods": {"org/apache/commons/lang3/StringUtils.java@isBlank.finalCharSequencecs": 0, "org/apache/commons/lang3/math/NumberUtils.java@createNumber.finalStringstr": 1, "org/apache/commons/lang3/math/NumberUtils.java@createInteger.finalStringstr": 2}, 
    "ftest": {"org.apache.commons.lang3.math.NumberUtilsTest#TestLang747": 0}, 
    "rtest": {"org.apache.commons.lang3.StringUtilsTest#testDefaultIfBlank_StringString": 0, "org.apache.commons.lang3.StringUtilsTest#testDefaultIfBlank_StringBuffers": 1, "org.apache.commons.lang3.StringUtilsTest#testDefaultIfBlank_StringBuilders": 2, "org.apache.commons.lang3.StringUtilsTest#testDefaultIfBlank_CharBuffers": 3, "org.apache.commons.lang3.StringUtilsTrimEmptyTest#testIsNotBlank": 4, "org.apache.commons.lang3.StringUtilsTrimEmptyTest#testIsBlank": 5, "org.apache.commons.lang3.ValidateTest#testNotBlankNotBlankStringWithNewlinesShouldNotThrow": 6, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgEmptyStringShouldThrow": 7, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgBlankStringShouldThrow": 8, "org.apache.commons.lang3.ValidateTest#testNotBlankReturnValues1": 9, "org.apache.commons.lang3.ValidateTest#testNotBlankReturnValues2": 10, "org.apache.commons.lang3.ValidateTest#testNotBlankBlankStringWithNewlinesShouldThrow": 11, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgNotBlankStringWithWhitespacesShouldNotThrow": 12, "org.apache.commons.lang3.ValidateTest#testNotBlankNotBlankStringShouldNotThrow": 13, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgNotBlankStringShouldNotThrow": 14, "org.apache.commons.lang3.ValidateTest#testNotBlankEmptyStringShouldThrow": 15, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgNotBlankStringWithNewlinesShouldNotThrow": 16, "org.apache.commons.lang3.ValidateTest#testNotBlankMsgBlankStringWithWhitespacesShouldThrow": 17, "org.apache.commons.lang3.ValidateTest#testNotBlankNotBlankStringWithWhitespacesShouldNotThrow": 18, "org.apache.commons.lang3.ValidateTest#testNotBlankBlankStringWithWhitespacesShouldThrow": 19, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumber": 20, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumberMagnitude": 21, "org.apache.commons.lang3.math.NumberUtilsTest#testLang300": 22, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateBigDecimal": 23, "org.apache.commons.lang3.math.NumberUtilsTest#testIsNumber": 24, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumberFailure_1": 25, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumberFailure_2": 26, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumberFailure_3": 27, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateNumberFailure_4": 28, "org.apache.commons.lang3.math.NumberUtilsTest#testCreateInteger": 29, "org.apache.commons.lang3.math.NumberUtilsTest#testStringCreateNumberEnsureNoPrecisionLoss": 30}, 
    "lines": {"org/apache/commons/lang3/StringUtils.java25": 0, "org/apache/commons/lang3/StringUtils.java27": 1, "org/apache/commons/lang3/StringUtils.java28": 2, "org/apache/commons/lang3/StringUtils.java29": 3, "org/apache/commons/lang3/math/NumberUtils.java81": 4, "org/apache/commons/lang3/math/NumberUtils.java83": 5, "org/apache/commons/lang3/math/NumberUtils.java85": 6, "org/apache/commons/lang3/math/NumberUtils.java86": 7, "org/apache/commons/lang3/math/NumberUtils.java87": 8, "org/apache/commons/lang3/math/NumberUtils.java88": 9, "org/apache/commons/lang3/math/NumberUtils.java89": 10, "org/apache/commons/lang3/math/NumberUtils.java90": 11, "org/apache/commons/lang3/math/NumberUtils.java91": 12, "org/apache/commons/lang3/math/NumberUtils.java92": 13, "org/apache/commons/lang3/math/NumberUtils.java93": 14, "org/apache/commons/lang3/math/NumberUtils.java95": 15, "org/apache/commons/lang3/math/NumberUtils.java97": 16, "org/apache/commons/lang3/math/NumberUtils.java201": 17, "org/apache/commons/lang3/math/NumberUtils.java203": 18}, 
    "ltype": {"0": "IfStatement", "1": "ForStatement", "2": "IfStatement", "3": "ReturnStatement", "4": "IfStatement", "5": "IfStatement", "6": "LocalVariableDeclaration", "7": "LocalVariableDeclaration", "8": "ForStatement", "9": "IfStatement", "10": "StatementExpression", "11": "BreakStatement", "12": "IfStatement", "13": "LocalVariableDeclaration", "14": "IfStatement", "15": "IfStatement", "16": "ReturnStatement", "17": "IfStatement", "18": "ReturnStatement"}, "edge": [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0]], "edge10": [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2], [0, 3], [1, 3], [2, 3], [3, 3], [0, 4], [1, 4], [2, 4], [3, 4], [0, 5], [1, 5], [2, 5], [3, 5], [0, 6], [1, 6], [2, 6], [3, 6], [0, 7], [0, 8], [1, 8], [2, 8], [0, 9], [1, 9], [2, 9], [3, 9], [0, 10], [1, 10], [2, 10], [3, 10], [0, 11], [1, 11], [2, 11], [0, 12], [1, 12], [2, 12], [3, 12], [0, 13], [1, 13], [2, 13], [3, 13], [0, 14], [1, 14], [2, 14], [3, 14], [0, 15], [0, 16], [1, 16], [2, 16], [3, 16], [0, 17], [1, 17], [2, 17], [0, 18], [1, 18], [2, 18], [3, 18], [0, 19], [1, 19], [2, 19], [0, 20], [1, 20], [2, 20], [3, 20], [4, 20], [5, 20], [6, 20], [7, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [17, 20], [18, 20], [0, 21], [1, 21], [2, 21], [3, 21], [4, 21], [5, 21], [6, 21], [7, 21], [8, 21], [9, 21], [10, 21], [11, 21], [12, 21], [13, 21], [14, 21], [15, 21], [16, 21], [17, 21], [18, 21], [0, 22], [1, 22], [2, 22], [3, 22], [4, 22], [5, 22], [6, 22], [7, 22], [8, 22], [9, 22], [12, 22], [0, 23], [1, 23], [2, 23], [3, 23], [0, 24], [1, 24], [2, 24], [3, 24], [4, 24], [5, 24], [6, 24], [7, 24], [8, 24], [9, 24], [10, 24], [11, 24], [12, 24], [13, 24], [14, 24], [15, 24], [16, 24], [17, 24], [18, 24], [0, 25], [1, 25], [2, 25], [3, 25], [4, 25], [5, 25], [6, 25], [7, 25], [8, 25], [9, 25], [12, 25], [0, 26], [1, 26], [2, 26], [3, 26], [4, 26], [5, 26], [6, 26], [7, 26], [8, 26], [9, 26], [12, 26], [0, 27], [1, 27], [2, 27], [3, 27], [4, 27], [5, 27], [6, 27], [7, 27], [8, 27], [9, 27], [12, 27], [0, 28], [1, 28], [2, 28], [3, 28], [4, 28], [5, 28], [6, 28], [7, 28], [8, 28], [9, 28], [12, 28], [17, 29], [18, 29], [0, 30], [1, 30], [2, 30], [3, 30], [4, 30], [5, 30], [6, 30], [7, 30], [8, 30], [9, 30], [12, 30]], "edge2": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16], [2, 17], [2, 18]], 
    "mutation": {"10": 0, "11": 1, "12": 2, "13": 3, "14": 4, "15": 5, "16": 6, "18": 7, "19": 8, "20": 9, "21": 10, "22": 11, "23": 12, "24": 13, "25": 14, "26": 15, "27": 16, "3376": 17, "3377": 18, "3378": 19, "3379": 20, "3380": 21, "3381": 22, "3382": 23, "3383": 24, "3384": 25, "3385": 26, "3386": 27, "3387": 28, "3388": 29, "3389": 30, "3390": 31, "3391": 32, "3392": 33, "3393": 34, "3394": 35, "3395": 36, "3396": 37, "3397": 38, "3398": 39, "3399": 40, "3400": 41, "3401": 42, "3402": 43, "3660": 44}, 
    "mtype": {"0": "ROR.==.FALSE", "1": "LVR.0.POS", "2": "LVR.0.NEG", "3": "ROR.==.<=", "4": "ROR.==.>=", "5": "COR.||.!=", "6": "COR.||.RHS", "7": "LVR.0.POS", "8": "LVR.0.NEG", "9": "ROR.<.!=", "10": "ROR.<.<=", "11": "ROR.<.FALSE", "12": "LVR.FALSE.TRUE", "13": "ROR.==.FALSE", "14": "ROR.==.LHS", "15": "ROR.==.RHS", "16": "LVR.FALSE.TRUE", "17": "ROR.==.FALSE", "18": "COR.StringUtils.isBlank.TRUE", "19": "COR.StringUtils.isBlank.FALSE", "20": "LVR.0.POS", "21": "LVR.0.NEG", "22": "COR.str.startsWith.TRUE", "23": "COR.str.startsWith.FALSE", "24": "STD.<ASSIGN>.<NO-OP>", "25": "LVR.0.POS", "26": "LVR.0.NEG", "27": "ROR.>.!=", "28": "ROR.>.>=", "29": "ROR.>.FALSE", "30": "AOR.-.%", "31": "AOR.-.*", "32": "AOR.-.+", "33": "AOR.-./", "34": "LVR.POS.0", "35": "LVR.POS.NEG", "36": "ROR.>.!=", "37": "ROR.>.>=", "38": "ROR.>.FALSE", "39": "LVR.POS.0", "40": "LVR.POS.NEG", "41": "ROR.>.!=", "42": "ROR.>.>=", "43": "ROR.>.FALSE", "44": "ROR.==.FALSE"}, 
    "edge12": [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 2], [13, 2], [14, 2], [15, 2], [16, 3], [17, 4], [18, 5], [19, 5], [20, 7], [21, 7], [22, 9], [23, 9], [24, 10], [25, 12], [26, 12], [27, 12], [28, 12], [29, 12], [30, 13], [31, 13], [32, 13], [33, 13], [34, 14], [35, 14], [36, 14], [37, 14], [38, 14], [39, 15], [40, 15], [41, 15], [42, 15], [43, 15], [44, 17]], 
    "edge13": [[4, 23], [8, 23], [11, 23], [12, 23], [13, 23], [14, 23], [15, 23], [16, 23], [4, 20], [8, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [19, 20], [22, 20], [24, 20], [29, 20], [31, 20], [34, 20], [35, 20], [36, 20], [8, 25], [8, 26], [8, 27], [8, 28], [4, 21], [8, 21], [11, 21], [12, 21], [13, 21], [14, 21], [15, 21], [16, 21], [19, 21], [21, 21], [22, 21], [24, 21], [29, 21], [31, 21], [32, 21], [34, 21], [35, 21], [36, 21], [39, 21], [40, 21], [42, 21], [4, 24], [8, 24], [11, 24], [12, 24], [13, 24], [14, 24], [15, 24], [16, 24], [19, 24], [4, 22], [8, 22], [11, 22], [12, 22], [13, 22], [14, 22], [15, 22], [16, 22], [19, 22], [4, 30], [8, 30], [11, 30], [12, 30], [13, 30], [14, 30], [15, 30], [16, 30], [19, 30]], 
    "edge14": [[4, 0], [8, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [19, 0], [21, 0], [22, 0], [24, 0], [29, 0], [31, 0], [32, 0], [34, 0], [35, 0], [36, 0], [39, 0], [40, 0], [41, 0], [42, 0]], 
}
```
**This detailed explanation provides a clearer understanding of each key's role in the dataset.**
| Key          | Description                                       |
|--------------|---------------------------------------------------|
| 'proj'       | Project version                                   |
| 'ans'        | Incorrect method identifier                      |
| 'methods'    | List of methods                                   |
| 'ftest'      | Incorrect test case                               |
| 'rtest'      | Correct test case                                 |
| 'lines'      | Statement number mapping: 'org.apache.commons.lang3.math.NumberUtils:463': 8 |
| 'ltype'      | AST (Abstract Syntax Tree) node type in method    |
| 'edge'       | Tuple: (statement, incorrect test case)          |
| 'edge10'     | Tuple: (statement, correct test case)            |
| 'edge2'      | Tuple: (method, statement)                       |
| 'mutation'   | Mutated AST node                                  |
| 'mtype'      | Type of mutation                                  |
| 'edge12'     | Tuple: (mutation, statement)                      |
| 'edge13'     | Tuple: (mutation, correct test case)             |
| 'edge14'     | Tuple: (mutation, incorrect test case)           |

The provided code has an additional feature where the data abstraction and function call relationships between functions are extracted and stored in a `{dataset}_M2M.txt` file. This file captures the mapping of functions and their corresponding datasets.

Please note that due to the large size of the files, only the data for Lang, Chart, and Cli has been uploaded. If you require the data for JxPath and Math, kindly contact the author directly to request the files separately.

Thank you for your understanding.

## Code Files

## Runtime Environment and Dependencies

To run the code for this project, ensure you have the following runtime environment:

1. **Python Version:** Python 3.X

Install the required dependencies using the following commands:

```bash
pip install numpy
pip install json
pip install pickle
# Add any other necessary dependencies
```
Please note that the provided list includes common dependencies like numpy, json, and pickle. Adjust the dependencies based on specific details within your code. If there are additional dependencies or specific versions required, update the installation commands accordingly.

2. **Code Flow Explanation**

 **1\)** **Build Overall Matrix (Kill Matrix)**

 Make sure to incorporate the logic for extracting necessary information from your pre-organized data file and then proceed with the construction of the kill matrix.

 **2\)** **Abstract Graph Structure for Weight Calculation**

Implement code to create an abstract graph structure for calculating weight matrices. This involves extracting the internal structure relationships from the data file and abstracting them into a graph structure. Nodes represent program entities, edges represent relationships, and the abstraction is then represented in matrix form.

 **3\)** **Suspiciousness Calculation Process**
 
 Comparison between Traditional MBFL and MBFL_G (Traditional MBFL with GBSR) Integrated with GBSR

 **4\)** **Save and Organize Results**


3. **Code File Explanation**

The provided code is designed to conduct experiments using the **Lang** as an example. If you wish to use a different experimental dataset, minor adjustments to the code may be necessary.

Follow the sequence below to execute each Python program in the provided method. Ensure that you run the programs in the specified order for a successful execution of the entire workflow.

<!-- ```bash
python Get_Killed_Matrix.py
python Get_Graph_Matrix.py
python PageRank_Value_Calculation.py
python Suspiciousness_Calculation.py
python Evaluate_Result.py
``` -->

## (1) Get_Killed_Matrix.py

Execute the script to obtain the killed matrix, capturing information related to the presence or absence of specific elements. This script generates data from the mutation analysis process, facilitating a more straightforward calculation of suspiciousness using the traditional MBFL method. The results of the execution are saved in the '***Killed_Matrix***' folder. Due to the large size of the graph structure, the data is saved in the pkl file format.

```bash
python Get_Killed_Matrix.py
```
## (2) Get_Graph_Matrix.py

Run the script to obtain the graph matrix, abstracting information such as function call relationships and internal structure relationships within program entities into a graph structure. The script considers two scenarios: passing and failing tests. The results of the execution are saved in the '***F_FIN_matrix***' and '***P_FIN_matrix***' folders. Due to the large size of the graph structure, the data is saved in the pkl file format.

```bash
python Get_Graph_Matrix.py
```

## (3) PageRank_Value_Calculation.py

Run the script to calculate PageRank values for the matrices corresponding to the two types of tests. The calculated PageRank values will be saved in the PR_Value folder.

```bash
python PageRank_Value_Calculation.py
```
For the Lang1, the first line provides the count of different categories of program entities, representing the number of methods（3）, statements（19）, mutants（45）, passed tests（31）, and failed tests（1）, respectively. The second line corresponds to the PageRank values of different program entities.

```
3 19 45 31 1
0.13711014507154012 0.2706443768564598 0.24295525446812183 ……
```

## (4) Suspiciousness_Calculation.py

Run the script to calculate suspiciousness scores using both traditional MBFL and MBFL integrated with the GBSR strategy. The results are stored in the SUS folder, where each file represents the calculation method (traditional MBFL or MBFL_G integrated with GBSR) for a specific project. Each file contains an array representing the suspiciousness values for different methods in the project.

```bash
python Suspiciousness_Calculation.py
```
## (5) Evaluate_Result.py

Run the script to perform the final evaluation using the Top metric. The evaluation results are saved in the Result folder as an Excel. The spreadsheet contains three sheets, each representing a comparison between traditional MBFL and MBFL integrated with the GBSR strategy using the TOP-1, TOP-3, and TOP-5 metrics. This provides a clear demonstration of the effectiveness of our method.

```bash
python Evaluate_Result.py
```


