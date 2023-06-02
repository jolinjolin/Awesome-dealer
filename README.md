# Aweome dealer - A Car Dealership Review Platform

This is a comprehensive web application that serves as a review platform for car dealerships. It offers a wide range of features to enhance the car dealership searching experience, allowing users to explore an extensive collection of car models, access detailed specifications, read authentic user reviews, and leave comments. 

## Key Features

- Explore an extensive collection of car models
- Access detailed specifications and features of each car
- Read authentic user reviews
- Leave comments and interact with other users
- Perform sentiment analysis on reviews using IBM NLP (Natural Language Processing) tools
- Automatically add emojis to reviews based on sentiment
- User-friendly and intuitive interface

## Technologies Used

- Django framework for Full Stack development
- IBM NLP tools for sentiment analysis
- Docker for containerization
- Kubernetes for orchestration
- IBM Cloud for scalable deployment

## Setup Instructions

Clone the repository:

   ```bash
   git clone <repository_url>
   ```

Navigate to the server directory:

```bash
   cd server
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the server:

```bash
python manage.py migrate
python manage.py runserver
```

Create a superuser:
```bash
python manage.py createsuperuser
```
