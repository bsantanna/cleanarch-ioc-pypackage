import logging
import os
from dependency_injector import containers, providers

from app.application.services.user import UserService
from app.domain.repositories.user import UserRepository
from app.infrastructure.database.config import Database


logger = logging.getLogger(__name__)
class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[
        "app.interface.api.users.endpoints"
    ])

    config_file = (
        "config-docker.yml" if os.getenv("DOCKER")
        else "config-test.yml" if os.getenv("TESTING")
        else "config.yml"
    )

    logger.info(f"Using configuration file: {config_file}")

    config = providers.Configuration(yaml_files=[config_file])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
