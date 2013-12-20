1. Problem: EAD files won't upload into ArchivesSpace
  Solution: Add <extent></extent> around content of <physdesc...>

2. Problem: Duplicate headings in collection-level description
  Solution: Remove <head>*</head> within <descgrp>

3. Problem: Multiple abstracts.
  Right now, there are multiple <abstract type="SOMETHING">*</abstract>.
  Create a dictionary with everything that SOMETHING can be as keys, and LOC authories as the values. Example: {MUS:"Band music--United States--20th century--History and criticism."} Maybe multiple dictionaries, with one for LOC authorities, one for UMD subject guides, so {MUS:"Music"}
  Within <controlaccess> add <subject>SOMETHING_VALUE</subject> for each SOMETHING. If we go with the multiple dictionaries, you'd have <subject source="LOC">SOMETHING_VALUE_LOC</subject> and <subject source="UMD">SOMETHING_VALUE_UMD</subject> for each SOMETHING.
  Delete all but one instance of <abstract type="SOMETHING">*</abstract>. For that one that you left, remove type="SOMETHING">
  
4. Problem: Add clickable link to Duplication and Copyright Information
  Within <userestrict>, recognize the URL at the end [in SCPA's case, http://www.lib.umd.edu/scpa/contact] and add an <a href="URL">URL</a> around the URL. So it'll have to copy the URL into the <a href> while adding the tags.

5. Problem: ArchivesSpace takes the <arrangement> content and splits it into two separate elements - a text note with the series list and an ordered list note with the series list in a much more organized fashion. Need to figure out how to get it to only pull the content into the ordered list.

6. Problem: Related Material note refers to "Subject Guides" that will be taken care of elsewhere with Archivesspace. So remove the <head>*</head> and <p>For other related archival and manuscript collections, please see the following <archref xpointer="rguide">subject guides</archref>.</p> within <related></related>

7. Problem: Why is ArchivesSpace listing each series twice? Only the second listing is what we want. Probably need to move the <scopecontent> for each series to right next to the <dsc> for that series.

8. Problem: Check to make sure chronologies are showing up right. Bencriscutto doesn't have one, so make one up for the purposes of the example.

9. Problem: Make sure the dates are working correctly. Make it pull start and end dates separately instead of as one big expression, make it list bulk and inclusive dates correctly, make normalized dates.
