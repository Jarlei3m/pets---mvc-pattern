from typing import Dict, List
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets_list = self.__get_pets_in_db()
        response = self.__format_response(pets_list)

        return response
    
    def __get_pets_in_db(self) -> List[PetsTable]:
        pets_list = self.__pet_repository.list_pets()

        if not pets_list:
            raise Exception('An internal error occurred!')
      
        return pets_list
    
    def __format_response(self, pets_list: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets_list:
            formatted_pets.append({
                "id": pet.id,
                "name": pet.name,
                "type": pet.type
            })
        
        return {
            "data": {
                "type": "Pets",
                "count": len(pets_list),
                "attributes": formatted_pets
            }
        }
            