Problem: EAD files won't upload into ArchivesSpace
  * Solution: Add ```<extent></extent>``` around content of ```<physdesc...>``` at collection level.

Problem: Duplicate headings in collection-level description
  * Solution: Remove ```<head>*</head>``` within ```<descgrp>```

Problem: Multiple abstracts.
  * Right now, there are multiple ```<abstract type="SOMETHING">*</abstract>```.
  *  Create a dictionary with everything that SOMETHING can be as keys, and LOC authories as the values. Example: {MUS:"Band music--United States--20th century--History and criticism."} Maybe multiple dictionaries, with one for LOC authorities, one for UMD subject guides, so {MUS:"Music"}
  *  Within ```<controlaccess>``` add ```<subject>SOMETHING_VALUE</subject>``` for each SOMETHING. If we go with the multiple dictionaries, you'd have ```<subject source="LOC">SOMETHING_VALUE_LOC</subject>``` and ```<subject source="UMD">SOMETHING_VALUE_UMD</subject>``` for each SOMETHING.
  *  Delete all but one instance of ```<abstract type="SOMETHING">*</abstract>```. For that one that you left, remove ```type="SOMETHING"```
  
Problem: Add clickable link to Duplication and Copyright Information
  * Within ```<userestrict>```, recognize the URL at the end [in SCPA's case, http://www.lib.umd.edu/scpa/contact] and add an ```<a href="URL">URL</a>``` around the URL. So it'll have to copy the URL into the <a href> while adding the tags.
  * Also within ```<publicationstmt>```
  * Also within ```<repository>```

Problem: ArchivesSpace takes the ```<arrangement>``` content and splits it into two separate elements - a text note with the series list and an ordered list note with the series list in a much more organized fashion. Need to figure out how to get it to only pull the content into the ordered list.

Problem: Related Material note refers to "Subject Guides" that will be taken care of elsewhere with Archivesspace.
  * Remove the ```<head>*</head>``` and ```<p>For other related archival and manuscript collections, please see the following <archref xpointer="rguide">subject guides</archref>.</p>``` within ```<related></related>```
  * Leave other content within this tag - we're only removing the default text.

Problem: Why is ArchivesSpace listing each series twice? Only the second listing is what we want. ~~Probably need to move the ```<scopecontent>``` for each series to right next to the ```<dsc>``` for that series.~~ 
  * ```<dsc type="analyticover" id="*">*</dsc>``` is what is messing this up. The ```<scopecontent>``` notes within the dsc-analyticover are useful, but they should go with the dsc-in-depth instead.
  * Move ```<scopecontent>``` notes to the following location: within ```<dsc type="in-depth" id="*">``` to the corresponding container, outside of the ```<did>``` for that container.
  * Remove ```<dsc type="analyticover" id="*">``` and everything within it.
  * Remove type="in-depth" from the other dsc tag.

Problem: Check to make sure chronologies are showing up right. Bencriscutto doesn't have one, so make one up for the purposes of the example.

Problem: Make sure the dates are working correctly. Make it pull start and end dates separately instead of as one big expression, make it list bulk and inclusive dates correctly, make normalized dates.
  * For every ```<date>``` tag, add the attribute ```normal="YYYYMMDD"``` or ```normal="YYYY/YYYY"``` with the values pulled from the content of the ```<date>``` tag.
