# Document Translation and Text-to-Speech System

This project is a comprehensive system for translating documents into multiple languages and converting translated text into speech. It leverages a Large Language Model (LLM) for accurate translations and a Text-to-Speech (TTS) engine for generating audio output.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload documents for translation
- Automatic language detection
- Translate documents into multiple languages using LLM
- Convert translated text to speech using TTS engine
- Download translated documents and audio files
- Secure API endpoints

## Architecture

The system is composed of the following components:

1. **User Interface (Web/Mobile Application)**
2. **Document Upload Service**
3. **Document Processing Service (including OCR)**
4. **Translation Service (using LLM)**
5. **Text-to-Speech Service**
6. **Output Service (for document download and audio playback)**
7. **Storage (Document Storage, Translation Metadata, Audio File Storage)**
8. **API Gateway**
9. **Authentication and Authorization**
10. **Monitoring and Logging**

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/document-translation-system.git
   cd document-translation-system
   ```
2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up the environment variables (you can use a `.env` file):

   ```env
   FLASK_APP=app/main.py
   FLASK_ENV=development
   ```

## Usage

1. Run the Flask application:

   ```bash
   flask run
   ```
2. Access the application through `http://localhost:5000`.

## API Endpoints

- **Upload Document**

  ```http
  POST /api/upload
  ```

  - **Body**: Multipart form-data with `document` field containing the file to upload.
  - **Response**: JSON with `document_id`.
- **Translate Document**

  ```http
  POST /api/translate
  ```

  - **Body**: JSON with `document_id` and `language` fields.
  - **Response**: JSON with `translation_id`.
- **Text-to-Speech**

  ```http
  POST /api/tts
  ```

  - **Body**: JSON with `translation_id`.
  - **Response**: JSON with `audio_id`.

## Configuration

Configuration settings for the application are managed in `app/config.py`. Ensure you have the necessary configuration for:

- Flask settings
- Database connections
- API keys for LLM and TTS services
- Storage paths

## Testing

1. To run the tests, ensure you are in the project directory and the virtual environment is activated.
2. Run the tests using `pytest`:

   ```bash
   pytest tests/
   ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
