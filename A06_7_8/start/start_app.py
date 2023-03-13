

from src.repository.activity_repo import Activity_Repo
from src.repository.person_repo import Person_Repo
from src.services.activity_services import ActivityServices
from src.services.person_services import PersonServices
from src.services.undo_redo import UndoRedoService
from src.test.test_activity import Test_Activity
from src.test.test_person import Test_Person
from src.ui.UI import UI


def start_menu():

    undo_service = UndoRedoService()
    #redo = UndoRedoService()

    person_repository = Person_Repo()
    person_repository.generate_people()
    #person_service = PersonServices(person_repository, undo_service)
    # if a person_id is deleted -> so the person_id from the activity list --> we need activity_service

    activity_repository = Activity_Repo()
    activity_repository.generate_activities()
    activity_service = ActivityServices(activity_repository, undo_service)
    person_service = PersonServices(person_repository, undo_service, activity_repository)
    Test_Person()
    Test_Activity()




    start_ui = UI(person_service, activity_service, undo_service)
    start_ui.start()

start_menu()
