##Doggett's Directory Parsing


###Project Objective
Clean text errors and transform directory entries into a dataframe.

 - Identify blocks of directory entries from the rest of the directory.
 - Correct "obvious" incorrect character translations resulting from the    OCR process. 
 - Make the approach reusable for other directories

There is a high likelihood that the cleaning and parsing will not handle all corrections required. It may be that the text cleaning and parsing will need a subsequent review, possibly using crowd-sourcing to provide sufficient accuracy for research purposes.

###Data Source
Image: https://archive.org/stream/doggettsnewyorkc1848dogg/#page/n3/mode/2up
Text: https://archive.org/stream/doggettsnewyorkc1848dogg/doggettsnewyorkc1848dogg_djvu.txt

Directory Text Structure:
Original is in two column format. Each directory column has a header that consists of three all cap letter column header that corresponds to last entry of the column
If a page starts with directory entries, then the page number appears between the two three-letter column headers.

Standard form of a single entry is Last_Name [space] First_Name [comma] Occupation [comma] Address

    Acker William, seaman, 84 Walnut

If there is a middle Initial it appears after the First_Name. It is followed by a period and there is no comma between the Initial and Occupation

    Ackerman John C. carman, 140 W. 20th

If there is a suffix, it is separated from First_Name or Initial by a comma and is not followed by a comma to separate it from Occupation.

    Belden Thomas, jr. sashmkr, W. 24tb b. A vs. 9 &.1C 

In the original directory, each entry is on a single line unless there is not enough space. The OCR text inserts a line break and usually a blank line.

    Ackerman John R. tailor, 111 Broadway, h. Hoyt n.
        
    Atlantic, Brooklyn
    
    BAYLIS HEN 11 V, importer, 131 William, h. 28 E.
    14th

Often two addresses are given. The first is a place of work and the second, preceded by "h." is the residence. Often only the town is given if the residence is not in New York.

Occupation may refer to a business rather than a profession.
Acker Henry C. & Co. fruits. 100 Wall, h. Williamsb'g

The "&" often indicates an entry is not in a Last_Name First_Name format, generally in the case of business names.  All-cap entries generally refer to businesses but also include professionals. 

    ADAMS, MCHESNEY & CO. brokers, 71 Wall
    
    ADAMS ROBERT A. lawyer, 11 Nassau, h.261 W. 17th

However some business entries are not all-caps.

    Adams & Lienau, brokers, 87 Wall



Entries frequently use abbreviations and contractions in names, occupations, and addresses.

Some entries are followed by advertising copy.

    DUGAN' JAMES C. sexton and general furnishing un-
    dertaker for funerals, 614 Broadway, opposite St.
    Thomas's church. Lead & ice coffins of all size*
    on hand, Orders left at his residence any hour,
    night or day will be punctually attended to. His
    warehouse is connected with his dwelling.



###OCR Errors
Wrong character translation: BardweTl Robert = Bardwell Robert
Spurious character added: Bard Edmund H~. gold, = Bard Edmund H. gold,
Fractions: r. 3?.J Suffolk = r. 38 1/2 Suffolk
Ampersands: Bardon St Co. liquors = Bardon & Co. liquors
Non-ASCII characters: â€” = double-length dash 
W frequently rendered as VV

###Initial Approach
- Separate directory entries by removing other text such as advertisements and tables.
     -- Find lines that only have three all-cap letters
     -- Remove all lines before and after if the line is blank, or only contains a number, or only contains three all-cap letters. 
- Remove extraneous line breaks so there is one entry per line and no blank lines
     -- Remove blank lines
     -- Isolate first token in each line
     + If token contains non letter character(s): Remove non-letter characters (function)
     + If all-letter token matches previous line: do nothing
- Categorize each entry as: Person or Business
-- Parse each entry into fields:
     + Person fields: Last_Name, First_Name, Other_Name, Occupation, [Business_Address], Home_Address
     + Business fields: Business_Name, Occupation, Business_Address fields

Also, need to create a lookup table of abbreviations: 

    al. for alley, b. between, bldgs. buildings, c. corner, com. commission, ct. court, e. r. east river, ex. exchange*
    forwdg. forwarding, h. house, la. lane, mer. merchant, mkr. maker, manf. manufacturer, n. r. north, river,
    op. opposite, pi. place, shipg. shipping, sq. square.

###Questions: 

 - Is an all caps entry just a function of whether the business pays a
   extra for the listing to stand out, or does it actually have a
   specific meaning? 
 - What does it mean if the profession is "late"?
 

    Allen Henry, late gunsmith. 44 Forsyth