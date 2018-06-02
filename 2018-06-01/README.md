- Requirement one: The index page displays position list according to the date (most recent first), and each of the position includes a variety of informations about the position, such as title, location, type, company name and created time. 
  - Extension One: The index page displays 10 positions initially, once the users click the 'Load More' button, it displays extra 10 positions.
- Requirements two: If the user clicks on one of the position in the index page, there will be a window pop up on the right side of the page, displaying the full details of the position. 
- Requirements three: The user can click the  ‘close’ icon on the top right of the popup window to close the window. 
- Requirements Four:  There is a form in the popup window that the users are able to submit their information directly. Once they fill the form and click the submit button, those information would be posted to the URL route /apply, and then the users can get response on a new page on the URL route /applysuccess. 
  - Extension Two: The new page will tell the users that the application has been submitted successfully and will get response in a short time, AND it provides a table for the users to see all the applications they have submitted.
- Requirements Five: There is a search box in the index page so that the user can enter some text to filter the position, the filter condition is based on the 'title'. The users can enter only one word or multiple words(seperated by space).  

##### Design

The web is based on Bootstrap framework, so it is also user friendly to mobile users due to its responsive feature.