# Noncompressed-Internet-Query

<p>
 
 
  <!-- Python -->
  
</p>
https://github.com/majdjb7/Noncompressed-Internet-Query

## 🚀 1. Overview

### INTRO 
In this project we receive a file containing a collection of product reviews (1000), each that look like this:
product/productId: B001E4KFG0
review/userId: A3SGXH7AUHU8GW
review/profileName: delmartian
review/helpfulness: 1/1
review/score: 5.0
review/time: 1303862400
review/summary: Good Quality Dog Food
review/text: I have bought several of the Vitality canned dog food products and have
found them all to be of good quality. The product looks more like a stew than a
processed meat and it smells better. My Labrador is finicky and she appreciates this
product better than most.

 ## 🚀 2. Project Requirements
Given the input file with the raw data, you need to create an index that will allow efficient access to the information.
The index must be stored on disk so that it can be used when querying various products. Therefore, index files should remain on disk even when your program does not want to.
Rules:
- Do not use a database system to store this information. You have to realize the storage yourself.
- You can use more than one file to store the index. However, the number of files to be created should be fixed and not dependent on the number of reviews or dictionary size and the like.
- The index should be created in such a way that after its creation the raw data files are no longer needed. That is, all the information required to address the methods should be in the index created.

## 🚀 3. NonCompressedIndexWriter.py
  - The NonCompressedIndexWriter.py:
      -Given raw data, the class will create an index on the disk that can be accessed later. All data that will be used later should be stored in an index on the disk.
      -The word "NonCompressed" in the class name indicates that the index being built is not compressed. In this exercise it can be assumed that when building the index, all the data can be stored in memory.
      -The class also allows you to delete the index from the disk by deleting all the files from the index directory.

## 🚀 4. IndexReader.py
  - The IndexReader.py:
      -Once an index is created on the disk the class can be used to access a wide variety of data existing in the index.
      Use methods defined as guidance and instruction for planning the structure of the index. That is, the index structure should support the effective implementation of these methods.
      It can be assumed that the methods will be activated only after the index is built by NonCompressedIndexWriter.
      The implementation should be in such a way that it will be effective even when the index contains huge amounts of data.

## 🚀 5. For further information please open the PDF attached to the Project (Project_Requirements.pdf), it contains more detailed instructions
