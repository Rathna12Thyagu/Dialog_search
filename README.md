With subtitles of lot of movies as my dataset , built model that gets input as a movie dialog from user and gives you top5 similar results.
Embeddings for the dataset are stores in chromadb and whenever user gives input it is retrived from chromadb and displayed.
Embedding a whole movie's subtitle file is bad move there might be loss of information,so each subtitle file is chunked into 20-30 pieces and then embedded.
