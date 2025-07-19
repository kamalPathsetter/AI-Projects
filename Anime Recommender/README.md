# Anime Recommender

This project implements an Anime Recommender system.

## Features

-   **Data Processing Pipeline**: Processes anime data for recommendations.
-   **Vector Store**: Utilizes ChromaDB for efficient similarity search.
-   **Recommendation Engine**: Provides anime recommendations based on user input.
-   **Web Application**: A Flask-based web application for interacting with the recommender.
-   **Deployment Ready**: Includes configurations for Docker, GCP, and Kubernetes.

## Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/Anime-Recommender.git
    cd Anime-Recommender
    ```

2.  **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -e .
    ```

## Usage

To run the application:

```bash
streamlit run app/app.py
```

Then, open your web browser and navigate to `http://127.0.0.1:8501`.

## Deployment

This project includes:

-   `Dockerfile` for containerization.
-   `gcp-deployment.md` for Google Cloud Platform deployment instructions.
-   `anime-recommender-k8s.yaml` for Kubernetes deployment.

Refer to these files for detailed deployment steps.