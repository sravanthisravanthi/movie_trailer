import movie_trailers
import freshtomatoes
powerrangers=movie_trailers.Projects("power rangers",
                                      "A Story of warriors",
                                      "https://media3.picsearch.com/is?rRucEcuL0YfnaLcs5d-N3MgU23RNR7LcQ-1l9aWcvRA&height=341",
                                      "https://youtu.be/Km4YOsh92Io")
#print (powerrangers.movie_theme)
arundhathi=movie_trailers.Projects("Arundhathi",
                                   "A story of fiction",
                                   "https://media2.picsearch.com/is?smHBIj-McYLF39z7OuuZGxfk_zWbV0qPvOtQn67f0Io&height=288",
                                   "https://youtu.be/3OXhA30aJ7M")
kabhikushikabhigham=movie_trailers.Projects("kabhikushikabhigham ",
                                   "A story of relations",
                                   "https://media3.picsearch.com/is?QjmKmrUDqYNgQRTmkkH5jgXOhtR8bj0gnk9btB5o3vk&height=255",
                                   "https://youtu.be/7uY1JbWZKPA")
twilightsaga=movie_trailers.Projects("Twilight saga",
                                   "A story of wampire",
                                   "https://media2.picsearch.com/is?ed1ZRWNXyouSHUTHXJPhBgPxWLVMXHxhsXbjoOUa_CA&height=341",
                                   "https://youtu.be/QDRLSqm_WVg")
jabtakhaijaan=movie_trailers.Projects("Jab Tak Hai Jaan",
                                   "A story of love",
                                   "https://media2.picsearch.com/is?4Q_hlu5EhOzHvHW-qsP4dpLi_dI7dldLFVzsYlG_xVQ&height=341",
                                   "https://youtu.be/Z1kW1MbNI5Y")
rajarani=movie_trailers.Projects("Raja Rani",
                                   "A story of life",
                                   "https://media5.picsearch.com/is?K1g3ElIDDJUN9rx1_Cf2yIR_zQbBjwe6bHiVC29NnFs&height=341",
                                   "https://youtu.be/wZm38_0aIXk")
movies=[powerrangers,arundhathi,kabhikushikabhigham,twilightsaga,jabtakhaijaan,rajarani]
freshtomatoes.open_movies_page(movies)
