import webbrowser
class Projects():
    def __init__(self,title,story_line,poster,movie_trailer):
        self.movie_title=title
        self.movie_theme=story_line
        self.movie_poster=poster
        self.movie_trailer=movie_trailer
        def playtrailer(self):
            webbrowser.open(self.movie_trailer)
        
