from settings import Settings

# dialect+driver://username:password@host:port/database
DATABASE_URL = f'postgresql+asyncpg://{Settings.DATABASE_USER}:{Settings.DATABASE_PASSWORD}@' \
               f'{Settings.DATABASE_HOST}:{Settings.DATABASE_PORT}/{Settings.DATABASE_NAME}'
