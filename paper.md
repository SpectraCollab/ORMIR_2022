---
title: 'ORMIR_XCT: A Python package for high resolution peripheral quantitative computed tomography image processing'
tags:
  - Python
  - XtremeCT
  - HR-pQCT
  - bone analysis
authors:
  - name: Michael T. Kuczynski
    orcid: 0000-0001-5671-1205
    equal-contrib: true
    affiliation: "1, 2"
  - name: Nathan J. Neeteson
    orcid: 
    equal-contrib: true
    affiliation: "1, 2"
  - name: Kathryn S. Stok
    orcid: 
    affiliation: 3
  - name: Andrew J. Burghardt
    orcid: 
    affiliation: 4
  - name: Michelle A.E. Espinosa
    orcid: 
    affiliation: "5, 6"
  - name: Andrew K.O. Wong
    orcid: 
    affiliation: "5, 6"
  - name: Serena Bonaretti
    orcid: 
    affiliation: 7
  - name: Big
    orcid: 
    affiliation: 3
  - name: Justin J. Tse
    orcid: 
    affiliation: "2, 8"
  - name: Jared Vicory
    orcid: 
    affiliation: 9
  - name: Steven K. Boyd
    orcid: 
    affiliation: "1, 2, 8"
  - name: Sarah L. Manske
    orcid: 
    corresponding: true
    affiliation: "1, 2, 8"
affiliations:
 - name: Department of Biomedical Engineering, Schulich School of Engineering, University of Calgary, Canada 
   index: 1
 - name: McCaig Institute for Bone and Joint Health, Cumming School of Medicine, University of Calgary, Canada 
   index: 2
 - name: Department of Biomedical Engineering, The University of Melbourne, Parkville, Australia
   index: 3
- name: Department of Radiology and Biomedical Imaging, University of California, San Francisco, San Francisco, CA, United States
   index: 4
 - name: Joint Department of Medical Imaging, University Health Network, Toronto, ON, Canada
   index: 5
 - name: Toronto General Hospital Research Institute, University Health Network, Toronto, ON, Canada
   index: 6
 - name: Joint Department of Medical Imaging, University Health Network, Toronto, ON, Canada
   index: 7
 - name: Department of Radiology, Cumming School of Medicine, University of Calgary, Calgary, Canada
   index: 8
 - name: Department of Radiology, Cumming School of Medicine, University of Calgary, Calgary, Canada
   index: 9
date: 30 November 2022
bibliography: paper.bib
---

# Summary

Image processing of high resolution peripheral quantitative computed tomography
(HR-pQCT) scans has largely been limited to the use of the scanner manufacturer's
processing language (Image Processing Lanuague, IPL, Scanco Medical). In an attempt
to expand on exisiting IPL workflows developed for HR-pQCT data, the ORMIR_XCT
package was created. This package reimplements existing IPL scripts and workflows
in Python and add additional functionality to improve current image processing
techniques applied to HR-pQCT data.

The ORMIR_XCT package contains several modules for processing HR-pQCT data of
bones and joints, including: joint space analysis, bone mineral density calculations,
bone morphometric analysis of cortical and trabecular bone, automatic contouring
of the periosteal surface, registration of image stacks from HR-pQCT, and segmentation
of trabecular bone. Comparisions between IPL and ORMIR_XCT generated results are
provided using Bland-Altman plots to show the reliability of the ORMIR_XCT
package when compared to the current HR-pQCT standard measures. Jupyter Notebook 
examples are provided to descibe some of the workflows reimplemented in ORMIR_XCT.

# Statement of need

While HR-pQCT data can be processed using the manufacturer's provided scripting
language (IPL), users are limited in the available image processing functionality.
The ORMIR_XCT package was developed to reimplement existing IPL workflows currently
used around the world and to provide an open and reproducible package to allow
for the development of more advanced image processing workflows for HR-pQCT data.

The development of this package began during the Jupyter Community Workshop in
Maastricht, Netherlands in June 2022, hosted by the Open and Reproducibile 
Musculoskeletal Imaging Research (ORMIR) group. During this workshop, the 
conceptualization and initial development of the ORMIR_XCT package began with 
support from members of the Kitware team.

# Workflows

The ORMIR_XCT package contains several IPL workflows reimplemented in Python:
1. Automatic Periosteal Contouring
2. Joint Space Width Analysis
3. Bone Morphometry
4. Bone Mineral Density
5. Stack Registration

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge support from Jared Vicory and Dzenan Zukic during the development of this project.

# References