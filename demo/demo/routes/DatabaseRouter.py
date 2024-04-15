class DatabaseRouter:
    route_app_mongoDB = {'mobile', 'book', 'clothes'}
    route_app_mySQL = {'manager', 'cart', 'checkout_and_order', 'search', 'shipment', 'payment'}
    route_app_postgreSQL = {'user'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_mongoDB:
            return 'mongodb'

        if model._meta.app_label in self.route_app_mySQL:
            return 'mysql'

        if model._meta.app_label in self.route_app_postgreSQL:
            return 'postgresql'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_mongoDB:
            return 'mongodb'

        if model._meta.app_label in self.route_app_mySQL:
            return 'mysql'

        if model._meta.app_label in self.route_app_postgreSQL:
            return 'postgresql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {"default", "mysql", "mongodb", "postgresql"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_mongoDB:
            return db == 'mongodb'

        if app_label in self.route_app_mySQL:
            return db == 'mysql'

        if app_label in self.route_app_postgreSQL:
            return db == 'postgresql'

        return None