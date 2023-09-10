from models.user import User

def test_creates_user_instance():
    name_object = User('Mister Mac')
    assert name_object.username == 'Mister Mac'
