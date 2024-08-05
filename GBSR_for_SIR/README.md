# Project Directory Structure

This folder has a directory structure similar to GBSR_2024. However, we have supplemented it with Data (including program code and analysis results from SIR).
# Program Data Overview

This table provides a summary of various metrics for the analyzed programs. The metrics include the number of programs, lines of code, methods, covered lines by failing tests, tests, mutations, and faults.

| Programs | Loc  | Methods | Covered Loc | Tests | Mutations | Faults |
|----------|------|---------|-------------|-------|-----------|--------|
| 23       | 3979 | 180     | 666         | 1208  | 3769      | 23     |

##### Explanation of the Table
###### Programs: Indicates that 23 programs were analyzed in this study.
###### Lines of Code: There are a total of 3979 lines of code across all the programs.
###### Methods: The programs contain a total of 180 methods.
###### Covered Lines: 666 lines of code are covered by the tests that failed.
###### Tests: A total of 1208 tests were executed.
###### Mutations: There were 3769 mutants generated for mutation testing purposes.
###### Faults: 23 faults were identified in the programs.
This table and explanation provide a clear and concise summary of the key metrics used in the analysis of the programs.



### Experimental Results
<table>
    <tr>
        <th></th>
        <th>Jaccard</th>
        <th>Tarantula</th>
        <th>Dstar</th>
        <th>Hamann</th>
        <th>Wong<sub>1</sub></th>
        <th>Hamming</th>
    </tr>
    <tr>
        <td rowspan="2">Top-1</td>
        <td>4</td>
        <td>2</td>
        <td>3</td>
        <td>2</td>
        <td>4</td>
        <td>3</td>
    </tr>
    <tr>
        <td>5</td>
        <td>4</td>
        <td>6</td>
        <td>2</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <td rowspan="2">Top-3</td>
        <td>14</td>
        <td>14</td>
        <td>14</td>
        <td>10</td>
        <td>14</td>
        <td>14</td>
    </tr>
    <tr>
        <td>17</td>
        <td>17</td>
        <td>14</td>
        <td>10</td>
        <td>17</td>
        <td>14</td>
    </tr>
    <tr>
        <td rowspan="2">Top-5</td>
        <td>18</td>
        <td>18</td>
        <td>18</td>
        <td>15</td>
        <td>18</td>
        <td>18</td>
    </tr>
    <tr>
        <td>18</td>
        <td>18</td>
        <td>18</td>
        <td>15</td>
        <td>18</td>
        <td>18</td>
    </tr>
</table>

- **SIR Dataset Analysis**:
  - We extended our analysis to 23 programs in the SIR dataset.
  - The TOP-N analysis, which measures the number of correct fault identifications within the top N ranked results, showed marked improvements with our method.
  - For instance, in TOP-1, TOP-3, and TOP-5 rankings, our approach consistently outperformed traditional MBFL.
# Example Explanation with \path\example.jpg

In this example, we analyze the code of Tacs8 and compare the results of traditional MBFL (Model-Based Fault Localization) techniques with those incorporating GBSR (Graph-Based Statistical Reasoning). We found a significant improvement in fault localization accuracy when using the combined approach. Additionally, by analyzing the TOP-N results across 23 programs from the selected SIR dataset, we observed that our method also shows substantial improvements in the SIR dataset.

## Example Analysis: Tacs8 Code


- **Tacs8 Analysis**:
  - In the Tacs8 code, traditional MBFL identified several potential faults with moderate accuracy.
  - When GBSR was incorporated, the accuracy of fault localization improved significantly, reducing the search space for developers.
![Example Analysis](example.jpg)

### Key Findings

- **Improved Accuracy**: The combination of MBFL with GBSR resulted in more precise fault localization.
- **Reduced Debugging Time**: Developers can locate faults faster due to the higher accuracy and reduced search space.
- **Robust Performance**: Our method demonstrated significant improvements across multiple programs in the SIR dataset.

## Conclusion

By analyzing the example of Tacs8 and comparing traditional MBFL with the enhanced MBFL incorporating GBSR, we have demonstrated the effectiveness of our approach. The substantial improvements observed in both the specific example and the broader SIR dataset analysis indicate the potential of GBSR to significantly enhance fault localization techniques.

