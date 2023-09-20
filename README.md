# Movie Recommender System

This Streamlit-based Movie Recommender System allows you to select a movie you like and receive recommendations for similar movies.

## Usage

1. **Requirements**:
   - Python 3.x
   - Required libraries: `streamlit`, `pickle`, `pandas`, `requests`, `PIL` (Pillow)

2. **Installation**:
   - Ensure you have the required libraries installed using `pip`:
     ```bash
     pip install streamlit pandas requests Pillow
     ```

3. **Data**:
   - This system relies on the TMDb 5000 Movies Dataset, which has been preprocessed.
   - Ensure you have the following files in your project directory:
     - `movies_dict.pkl`: Pickle file containing movie data.
     - `similarity.pkl`: Pickle file containing movie similarity data.
   
4. **Running the Recommender**:
   - Run the Streamlit app by executing the script.
   - Select a movie from the dropdown menu.
   - Click the "Recommend" button to receive movie recommendations based on your selection.

## Screenshots

### Homepage
![Screenshot 2023-07-15 012103](https://github.com/Vortex-21/Movie-Recommender/assets/101874272/557e3705-bb53-4199-844a-b1fd77c777ab)


### Movie Selection Dropdown
![Screenshot 2023-07-15 012115](https://github.com/Vortex-21/Movie-Recommender/assets/101874272/22efb1cc-1ee5-490e-96fa-cc6c0178f06d)


### Recommended Movies
![Screenshot 2023-07-15 012202](https://github.com/Vortex-21/Movie-Recommender/assets/101874272/ea2e90bc-57b0-4632-b53d-8977cee939e4)


## Credits

This code is a simple implementation of a movie recommendation system using Streamlit and Python.


