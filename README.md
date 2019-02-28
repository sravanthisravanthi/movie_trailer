# Movie_Trailer
Python NanoDegree Project

TITLE : Movie Trailer Website 
AUTHOR : Sravanthi Munnaluri
PYTHON VERSION : Python 3.7
PROJECT : A python file generating a html web page
CODE CHECKER: PEP8

Description: A server-side code that stores a list of movies, including box art, imagery, a movie trailer URL, and serve this data as web page; allowing visitors to review their movies and watch trailers.

In this readme file, I explain in detail how our website; fresh_tomatoes.py functions with movie_trailers.py and movieentertainments.py to display movie title, story_line, poster, movie_trailer.  Finally, i explained how to run this program.

PLAN
Programming Foundations with Python
We started off with a plan:

1. Go to the website
2. See all of the movies displayed
3. Click on one to play it's trailer

It's pretty simple in terms of concept, but how about implementation?

Class structure

We will need classes to build this movie website. We want our Movie class to be a template for a generic movie, and then create instances of that class like this:

rajarani=movie_trailers.Projects

and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:

title
storyline
poster
movie_trailer
                           
import fresh_tomatoes

Note:
The original fresh_tomatoes.py file was reconfigured by me, to display more content.

Changes Made to the orginal fresh_tomatoes.py file:
1.The header_title was changed from its original heading to "Movie Review"

         <head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
             
2. Added "About Udacity" navigation as my reference to this project under the main_page_content. This links user to the main Udaity page.

       main_page_content = '''
         <body>
         ......
           <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
                   
3. Added "movie storyline" to the code which enables the web page display the storyline of each movie.

  <div class="col-md-6 col-lg-4 movie-tile" data-trailer-youtube-id="wZm38_0aIXk" data-toggle="modal" data-target="#trailer">
    <div class="text-center">
      <img src="https://media5.picsearch.com/is?K1g3ElIDDJUN9rx1_Cf2yIR_zQbBjwe6bHiVC29NnFs&height=341" width="220" height="342">
      <h2 style="color:red">Raja Rani</h2>
       <p style="color:black">A story of life <br></p>
    </div>
   
</div>
   
HOW TO RUN THE PROGRAM!!!
  Ensure that you have Python 3.7 or later installed.

  To turn this program into a movie website, ensure that you download the fresh_tomatoes.py file. It is already available for download     here. However, make sure the files (movie_trailers.py, movieentertainmenst.py, and fresh_tomatoes.py) are present in the same folder.

  Open these files using IDLE.

  You can edit the file contents following the instructions here, or the ‘#’ and “”” comments given in the code.

  Save your work (if any editing was done), and run the entertainment.py file. It will generate the HTML page or Website [fresh_tomatoes.html], using the fresh_tomatoes.py file.
