import io
import os
from PIL import Image
from database import *

def test_app_runs(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'Welcome to FoodFusion' in response.data

def test_database(app):
    with app.app_context():
        result = Recipe.query.all()

    assert result is not None

def test_detect(client):
    response = client.get("/detect")
    assert response.status_code == 200

def test_predict_test(client):
    img_bytes = io.BytesIO()
    Image.new('RGB', (100, 100)).save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    response = client.post('/detect', data={'file': (img_bytes, 'test.jpg')})

    assert response.status_code == 200

def test_predict(client):
    image = Image.new(mode='RGB', size=(100, 100))
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    response = client.post('/detect', data={'file': (image_bytes, 'test_image.png')})
    assert response.status_code == 200

    with client.session_transaction() as sess:
        assert sess['ingredients'] == {'ingredient_name': 1}


    response = client.get('/detect')
    assert response.status_code == 200
