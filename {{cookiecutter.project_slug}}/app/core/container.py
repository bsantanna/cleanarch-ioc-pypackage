from dependency_injector import containers, providers

from app.application.services.user import UserService
from app.domain.repositories.user import UserRepository
from app.infrastructure.database.config import Database

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[
        "app.interface.api.users.endpoints"
    ])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

