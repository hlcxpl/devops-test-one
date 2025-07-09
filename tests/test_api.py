from app.api import app

def test_success():
    client = app.test_client()
    rest= client.post('/reservations', 
    json={"room": "A", "time": "14:00"})
    assert rest.status_code == 201
    
def test_failure():
    client = app.test_client()
    client.post('/reservations', json={"room": "A", "time": "10:00"})
    rest = client.post('/reservations', json={"room": "A", "time": "10:00"})
    assert rest.status_code == 409
                    