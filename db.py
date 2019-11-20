import os
import logging
import importlib
import dataset

log = logging.getLogger()
db = dataset.connect('sqlite:///cp.db')

# Apply all migrations
def apply_migrations():
    log.info('Updating database...')

    # Get all migrations in migrations folder, sorted by name
    # (migrations should have the migration number as the first letters)
    migrations = [os.path.splitext(f)[0] for f in os.listdir('migrations') if f.endswith('.py')]
    migrations.sort()

    # Try to apply each migration
    for m in migrations:
        migration_module = importlib.import_module('migrations.' + m)
        if migration_module.apply(db):
            log.info('Migration ' + m + ' applied!')

    log.info('Database updated!')
