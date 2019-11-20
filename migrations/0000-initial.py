def apply(db):
    if 'meta' in db:
        return False

    meta_table = db.create_table('meta', 'id')
    meta_table.create_column('version', db.types.integer)
    meta_table.insert(dict(id=0, version=0))

    return True
