from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "Jhon",
        "last_name": "Doe",
        "age": 27,
        "pet_id": 5
    })

    person_creator_validator(request)
    