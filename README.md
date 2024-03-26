# PDFia

## Hosted on: (Only partitioner)
https://bloggyweb.pythonanywhere.com/


## Overview 
This application provides comprehensive functionality for interacting with PDF documents, catering to various user needs such as extracting specific sections, converting PDFs to Word documents, merging multiple PDF files and converting word document into pdf seamlessly all in one place.




## Description:
This flask based web application is designed for:
1. Extract pages from a PDF from a specified range. eg- From a 100 page PDF, extract page 2 to 17.   &#x2611;
2. Convert PDF into words.                                                                           &#x2611;
3. Merge PDF files.                                                                                  &#x2611;
4. Convert Word document into PDF.                                                                   &#x2611;

The project follows MVC architecture, industry level coding standards, feature branching (for Github), unit testing and as well as hosted in a remote server.

## Flow Chart

[![PDFia-7.png](https://i.postimg.cc/G2qMkbjn/PDFia-7.png)](https://postimg.cc/1nVcShTv)

## User Guide:
1. Home Screen:

   [![PDFia-5.png](https://i.postimg.cc/t41vP0jG/PDFia-5.png)](https://postimg.cc/v4svFNT0)
   
2. Upload file/files:
   
   a. Partitioner:

      [![PDFia-2.png](https://i.postimg.cc/QtZbYnTP/PDFia-2.png)](https://postimg.cc/FfG37pGg)

   b. For Word/Merger/Docx to PDF converter:

   [![PDFia-3.png](https://i.postimg.cc/QMQ5CNF4/PDFia-3.png)](https://postimg.cc/wtB3bpcL)
   [![PDFia-4.png](https://i.postimg.cc/nhtqJQzj/PDFia-4.png)](https://postimg.cc/tY2sdJFp)
   [![PDFia-6.png](https://i.postimg.cc/SRswjD7Z/PDFia-6.png)](https://postimg.cc/phw06QS8)
       
## Milestones:
Start Date:      18-Jan-2024

PDF Partitioner: 26-Jan-2024

Word Converter:  31-Jan-2024

Unit Test:       03-Feb-2024

Merger:          28-Feb-2024

Word to PDF:     01-Mar-2024


## Testing:
Unit tests to check status code for each API.





## Tools and Packages:

| Package            |  Usage                                              | 
| :-------------:    |:-------------:                                      | 
|  PyPDF2 3.0.1      | To read pdf and create a new pdf                    |  
|  pdf2docx 0.5.8    | To convert pdf into word                            |   
|  Flask 3.0.2       | To Create API endpoints and for overall hosting     |  
|  docx2pdf 0.1.8    | To convert docx into pdf                            |

## Future plans:
1. Can extend to some other pdf operations like, text extraction, pdf to ppt, pdf signature etc.
2. Improve exception handling. 
