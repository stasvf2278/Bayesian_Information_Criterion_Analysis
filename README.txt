Project Name:

Bayesian Information Criterion Analysis

Description:

This script compares to power laws within a single x-y dataset by iterating through the x-y values to identify datapoints which mark statistically significant different power laws expressed by the data.

Every time instance of BICx_star-BICR in the data produces a print read out at the critical x value ('Porosity' in this script, see Ln 85)

	see:
		Main, I.G., Leonard, T., Papasouliotis, O., Hatton, O., Meredith, P.G., 1999. One slope or two, Detecting statistically significant breaks of slope in geophysical data with application to fracture scaling relationships. Geophys. Res. Lett. 26 (18), 2801–2804.
		
		Heap, M.J., Kennedy, B., Farquharson, J., Ashworth, J., Gilg, H.A., Scheu, B., Lavallée, Y., Siratovich, P.A., Cole, J., Jolly, A., Dingwell, D.B., 2017a. A multidisciplinary approach to quantify the permeability of a volcanic hydrothermal system (Whakaari/White Island, Taupo volcanic zone, New Zealand). J. Volcanol. Geotherm. Res. 332, 88–108.
		
		Farquharson, J., Heap, M.J., Varley, N.R., Baud, P., Reuschlé, T., 2015. Permeability and porosity relationships of edifice-forming andesites: a combined field and laboratory study. J. Volcanol. Geotherm. Res. 297, 52–68.

Usage:

Note: Written in Pyton 2.7 and tested in Pyton 3.7

Note: This script was written for Windows.

Note: The script is currently set up to compare the data found in PorPerm2ABLM.csv. Change the file name in Ln 19 for your own CSV file. I provide this .csv file in case you wish to see the necessary data structure to use this script.

Note: The columns for the x and y columns (porosity and permeability, respectively) must be relabeled in the code if the column labels are changed from 'porosity' and 'permeability' (Ln 21 and 22). In this version of the script, 'porosity' is the x column and permeability is the y column.

Note: On Ln 80, 'if ltslope > mtslope:' ensures that lower x-value power law was always greater than the higher x-value power law. This line was important for my rock mechanics study as the lower x-value power law needed to be greater than the higher x-value power law. Depending on your data, this line may need to be removed and identation corrected.

Installation:

The 'import' commands need to be placed at the start of the Python file. The 'main()' function can be relabeled and moved as appropriate.

Credits:

I, Stanley Mordesky, modeled this script of the explanation of Bayesian Information Criterion Analysis provided by Jamie Farquharson in Farquharson et al. (2015).

License:

MIT License

Copyright (c) 2020 Stanley Mordesky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
