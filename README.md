#  CineAI – Intelligent Movie Recommendation System

CineAI is a lightweight, interactive, ML-powered web app that recommends movies based on content similarity.  
It analyzes movie metadata, computes similarity scores, and delivers personalized recommendations with posters and titles.

---

##  How It Works

1. **Load preprocessed movie dictionary + similarity matrix** (stored as pickle files with 2048+ embeddings).
2. **User selects a movie** from the Streamlit dropdown.
3. **Compute the top 5 most similar movies** using cosine similarity on movie embeddings.
4. **Fetch movie posters** in real-time using the TMDB API.
5. **Render results** in Streamlit using responsive column layouts with images and titles.

---

##  Impact

- Converts raw movie metadata into a fully interactive ML application.  
- Demonstrates **end-to-end machine learning deployment**, from data preprocessing to UI development.  
- Highlights skills in **API integration, model engineering, and frontend-backend linking**.  
- Provides a smooth and intuitive user experience powered by a clean Streamlit interface.

---
