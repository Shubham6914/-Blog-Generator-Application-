# Blog Generator App

## Overview
The Blog Generator App is a web application that allows users to generate text blogs from YouTube videos. By simply pasting the link of a YouTube video, the app fetches the transcript using the Assembly AI API and generates a well-structured blog using the OpenAI API. Users can save their generated blogs and access them later after logging in.

## Features
- **YouTube Video to Blog Conversion:** Users can paste a YouTube video link, and the app will generate a text blog based on the video content.
- **Save and Access Blogs:** Users can save their generated blogs and revisit them after logging in.
- **User Authentication:** The app supports user registration, login, and secure access to saved blogs.
- **Responsive Design:** The frontend is designed using HTML, CSS, and JavaScript, providing a user-friendly and responsive interface.

## Technologies Used
- **Frontend:**
  - HTML, CSS, JavaScript: For structuring, styling, and adding interactivity to the web pages.

- **Backend:**
  - Django: For backend development, handling user authentication, and routing.
  - Assembly AI API: Used for extracting transcripts from YouTube videos.
  - OpenAI API: Used for generating text blogs from video transcripts.

- **Database:**
  - MySQL: For storing user data and saved blogs.

## Installation

### Prerequisites
- Python 3.x
- Django
- MySQL

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog-generator-app.git
   cd blog-generator-app
