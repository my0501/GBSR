# Explanation of Example_for_Math19

The `Example_for_Math19` is an actual program, and we have retained its experimental results as well as the matrices used to construct the graph. It is noteworthy that due to its large matrix scale, with a total of 385 faulty test statements and 95 methods, we have preserved the data in the form of a pkl file.

# Fault Analysis with Traditional Methods and GBSR

We conducted a fault analysis using traditional methods and methods combined with GBSR and found that the fault ranking (Top-1) of the only error (Method 59) in Math19 was significantly improved by the suspicion ranking obtained by the new methods combined with GBSR. This greatly enhanced the accuracy of fault localization. Among them, the effect of the MBFL method combined with GBSR was the most significant, improving the traditional MBFL method ranking from 21 to 1, allowing for accurate and rapid fault localization when inspecting errors.

| Method Name | Top-1                        |
|-------------|-------------------------------|
| SBFL        | 30                            |
| PRFL        | 30                            |
| SBFL_G      | 28                            |
| MBFL        | 21                            |
| PRMA        | 12                            |
| MBFL_G      | 1                             |


# Explanation of Directories and Files

We can see multiple directories. The following is a detailed explanation of the directories and files:

1. **Math19.json**:
   - This file contains all the basic data for Math19, including information about faulty methods, statement information, mutation information, test cases, and internal associations.

2. **Matrix of Math19**:
   - This directory contains two subdirectories corresponding to matrices associated with passing tests and failing tests, respectively. The matrices are stored in the form of pkl files.

3. **PageRank Value of Math19**:
   - This directory stores the final calculated weight of each program entity, which is used to refine the final suspicion scores.

4. **Suspiciousness of Math19**:
   - This directory includes storage list files for the suspicion scores of six methods. These lists store each element's suspicion score, with the index representing the method number.
