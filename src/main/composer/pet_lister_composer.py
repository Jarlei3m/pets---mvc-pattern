from src.views.pet_lister_view import PetListerView
from src.controllers.pet_lister_controller import PetListerController
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler

def pet_lister_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetListerController(model)
    view = PetListerView(controller)

    return view
