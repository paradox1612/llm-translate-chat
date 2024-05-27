# app/routes.py
# Define API routes for document upload, translation, and text-to-speech (TTS).
# Use services from services module to handle the logic.
from flask import Blueprint, request, jsonify
from services.document_upload_service import upload_document
from services.translation_service import translate_document
from services.tts_service import generate_audio

def init_routes(app):
    api = Blueprint('api', __name__)

    @api.route('/upload', methods=['POST'])
    def upload():
        file = request.files['document']
        document_id = upload_document(file)
        return jsonify({"document_id": document_id}), 201

    @api.route('/translate', methods=['POST'])
    def translate():
        data = request.json
        document_id = data['document_id']
        target_language = data['language']
        translation_id = translate_document(document_id, target_language)
        return jsonify({"translation_id": translation_id}), 200

    @api.route('/tts', methods=['POST'])
    def tts():
        data = request.json
        translation_id = data['translation_id']
        audio_id = generate_audio(translation_id)
        return jsonify({"audio_id": audio_id}), 200

    app.register_blueprint(api, url_prefix='/api')
